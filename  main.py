import game

shtolnja = game.Room("Штольня")
shtolnja.set_description("Підвальне приміщення з випивкою та п‘яними підлітками.")

puchka = game.Room("Пучка")
puchka.set_description("Піцерія з вечірньою музикою.")

millenium = game.Room("Міленіум")
millenium.set_description("Накриття в центрі міста.")

shtolnja.link_room(puchka, "південь")
puchka.link_room(shtolnja, "північ")
puchka.link_room(millenium, "захід")
millenium.link_room(puchka, "схід")

somi = game.Friend("Сомі", "Та мила дівчинка з місцевого кафе")
somi.set_conversation("Вечір відстій!")
millenium.set_character(somi)

misha = game.Enemy("Михась", "Старий спітнілий дід.")
misha.set_conversation("Ей ти!")
misha.set_weakness("50 грам")
shtolnja.set_character(misha)

halja = game.Enemy("цьоця Галя", "Сусідка брата мами твоєї двоюрідної сестри.")
halja.set_conversation("Добрий вечір, а чому ти ще не дома?!")
halja.set_weakness("пакет")
puchka.set_character(halja)

bag = game.Item("пакет")
bag.set_description("Пакет з продуктами. В разі чого сказати, що мама послала по молоко")
puchka.set_item(bag)

alco = game.Item("50 грам")
alco.set_description("Смердюча наливка")
# shtolnja.set_item(alco)

current_room = puchka
backpack = []

dead = False
talk_with_somi = False

while dead == False:

    print("\n")
    print(current_room.get_details())

    inhabitant = current_room.get_character()
    friend = current_room.get_friend()

    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["південь", "північ", "захід", "схід"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "побалакати":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant:
            print(inhabitant.talk())
                # print()
            if inhabitant.name == "цьоця Галя":
                print("Вона тебе побачила! Потрібно викручуватись")
                fight_with = input("використати ")
                # if backpack == None:
                if fight_with in backpack:
                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("Супер!")
                        current_room.enemy = None
                        if inhabitant.get_defeated() == 2:
                            print("Ти прожив цей вечір!")
                            dead = True
                    else:
                    # What happens if you lose?
                        print("Гайка тобі.")
                        print("Цьоця Галя все розкаже твоїм батькам")
                        dead = True
                elif backpack is None:
                    print("Твоя сумка порожня")
                    print("Гайка тобі.")
                    print("Цьоця Галя все розкаже твоїм батькам")
                    dead = True
                else:
                    print("У тебе немає " + fight_with)
        elif friend:
            print(friend.talk())
            talk_with_somi = True
    elif command == "взаємодіяти":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Супер!")
                    current_room.enemy = None
                    if inhabitant.get_defeated() == 2:
                        print("Ти прожив цей вечір!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("У тебе немає " + fight_with)
        else:
            print("Тут немає людей...")
    elif command == "взяти":
        if friend and talk_with_somi:
            print("Ти поклав " + alco.name + " у свою сумку")
            backpack.append(alco.name)
            current_room.set_item(None)
        elif item is not None:
            print("Ти поклав " + item.get_name() + " у свою сумку")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("Тут немає предметів!")
    else:
        print("Я не знаю як " + command)
