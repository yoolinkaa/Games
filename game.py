""" game """

class Room:
    """
    class Room
    """
    def __init__(self, name, linked_rooms = {}, items = None, enemy = None, friend = None) -> None:
        self.name = name
        self.items = items
        self.enemy = enemy
        self.linked_rooms = linked_rooms
        self.friend = friend

    def set_description(self, des) -> None:
        """
        set description about room
        """
        self.room_description = des

    def link_room(self, room, direct) -> None:
        """
        set a directory
        """
        self.linked_rooms[direct] = [room, self.name]

    def move(self, direct):
        """
        change a directory
        """
        return self.linked_rooms[direct][0]

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, __o: object) -> bool:
        return self.name == __o

    def get_character(self):
        """
        return enemy
        """
        if self.enemy:
            return self.enemy
        return None
    def get_friend(self):
        """
        return friend
        """
        if self.friend:
            return self.friend
        return None

    def get_details(self) -> str:
        """
        return details about room
        """
        places = []
        details = [self.name, "--------------------", self.room_description]
        for i in list(self.linked_rooms.keys()):
            if self.linked_rooms[i][1] == self.name:
                places += [i]
        for i in places:
            details += [f"{self.linked_rooms[i][0]} -> {i}"]
        if self.get_character() is not None:
            details += [f"{self.enemy.name} тут!"]
            details += [self.enemy.describe()]
        if self.friend is not None:
            details += [f"{self.friend.name} тут!"]
            details += [self.friend.describe()]
        if self.get_item() is not None:
            details += [f"{self.items.name} тут! - {self.items.describe()}"]
        return "\n".join(details)

    def set_item(self, item) -> None:
        """
        add items to room
        """
        self.items = item

    def set_character(self, character) -> None:
        """
        add characters to room
        """
        if isinstance(character, Friend):
            self.friend = character
        else:
            self.enemy = character

    def get_item(self) -> None:
        """
        return item
        """
        return self.items if self.items else None

class Enemy:
    """
    class Enemy
    """
    count = 0
    def __init__(self, name, des) -> None:
        self.name = name
        self.enemy_description = des
        # self.count = count

    def describe(self) -> str:
        """
        return enemy describtion
        """
        return self.enemy_description

    def set_conversation(self, sent) -> None:
        """
        set enemy conversation
        """
        self.conversation = sent

    def set_weakness(self, weakness) -> None:
        """
        set enemy weakness
        """
        self.weakness = weakness

    def talk(self):
        """
        return enemy conversation
        """
        return f"[{self.name} каже]: {self.conversation}"

    def get_defeated(self) -> int:
        """
        return amount of killed inhaitan
        """
        return Enemy.count

    def fight(self, fight_with):
        """
        fight
        """
        if fight_with == self.weakness:
            Enemy.count += 1
            return True
        return False

class Item:
    """
    class Item
    """
    def __init__(self, name) -> None:
        self.name = name

    def set_description(self, des) -> None:
        """
        set item's desctiption
        """
        self.item_description = des

    def describe(self) -> str:
        """
        return item description
        """
        return self.item_description

    def get_name(self) -> str:
        """
        return item's name
        """
        return self.name

class Friend:
    """
    class Friend
    """
    def __init__(self, name, des) -> None:
        self.name = name
        self.friend_description = des

    def set_conversation(self, sent) -> None:
        """
        set friend conversation
        """
        self.conversation = sent

    def describe(self) -> str:
        """
        return enemy describtion
        """
        return self.friend_description

    def talk(self):
        """
        return enemy conversation
        """
        return f"[{self.name} каже]: {self.conversation}\n\
у Сомі з собою 50 грам"