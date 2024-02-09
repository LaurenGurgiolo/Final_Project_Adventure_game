import time
import random


items = []


def evil_one():
    evil = ["wicked witch", "evil troll", "dark sorcerer", "wicked fairie"]
    global x
    x = random.choice(evil)


def tt(text):
    print(text)
    time.sleep(1.5)


def intro():
    tt("You find yourself standing in an open field,")
    tt("filled with grass and yellow wildflowers.")
    print("Rumor has it that a", x)
    tt("is somewhere around here,")
    tt("and has been terrifying the nearby village.\n")


def choice():
    tt("You find yourself next to two paths.")
    tt("One path leads to a house, the other to a cave.")
    tt("Enter 1 to knock on the door of the house.")
    tt("Enter 2 to peer into the cave.")
    tt("What would you like to do?")
    u = input("(Please enter 1 or 2)\n")
    if u == '1':
        door()
    elif u == '2':
        cave()
    else:
        tt("I do not understand.")
        choice()


def door():
    tt("You walk up to the door and knock.")
    print("The", x, "appears!")
    tt("It is their house!")
    n = input("Do you want to fight?\n"
              "yes or no\n")
    if "y" in n:
        tt("OK, let's fight!")
        if x == "wicked witch":
            witch()
        elif x == "evil troll":
            troll()
        elif x == "dark sorcerer":
            sorcerer()
        elif x == "wicked fairie":
            fairie()
    elif "n" in n:
        tt("OK! Let's leave!")
        choice()
    else:
        tt("That is not an option.")
        door()


def cave():
    tt("You walk up to the cave.")
    tt("You find two items, a sword and a magic potion.")
    y = input("Which item would you like? Pick one.\n")
    if "sword" in y and "sword" in items:
        tt("You already have the sword")
        choice()
    elif "sword" in y and "sword" not in items:
        tt("You found the sword!")
        items.append("sword")
        if "sword" in items and "potion" in items:
            tt("Now you have both the sword and magic potion!")
        choice()
    elif "potion" in y and "potion" in items:
        tt("You already have the potion")
        choice()
    elif "potion" in y and "potion" not in items:
        tt("You found the magic potion!")
        items.append("potion")
        if "sword" in items and "potion" in items:
            tt("Now you have both the sword and magic potion!")
        choice()
    else:
        tt("I'm sorry that is not a option")
        cave()


def s_or_p():
    t = input("Would you like to use the sword or magic potion"
              " to defend yourself?\n")
    if "potion" in t and x == "wicked witch":
        potion_witch()
    elif "sword" in t and x == "wicked witch":
        sword_witch()
    elif "potion" in t and x == "evil troll":
        potion_troll()
    elif "sword" in t and x == "evil troll":
        sword_troll()
    elif "potion" in t and x == "dark sorcerer":
        potion_sorcerer()
    elif "sword" in t and x == "dark sorcerer":
        sword_sorcerer()
    elif "potion" in t and x == "wicked fairie":
        potion_fairie()
    elif "sword" in t and x == "wicked fairie":
        sword_fairie()
    else:
        tt("That is not an option.")
        s_or_p()


def game_over():
    tt("GAME OVER\n\n")
    items.clear()
    p = input("Would you like to play again? (y/n)\n")
    if "y" in p:
        run_game()
    elif "n" in p:
        tt("Goodby")
    else:
        tt("I do not understand")
        game_over()


def no_weapons():
    tt("But you have no weapons!")
    tt("This will be a hard battle!")


def potion_witch():
    tt("Good thing you have that magic potion!")
    tt("You open the bottle and throw it at the witch")
    tt("She melts away!")
    tt("Yay! You win!")
    tt("The village is saved!")
    game_over()


def sword_witch():
    tt("Luckly you have the sword!")
    tt("You try to stab the witch,")
    tt("but the witch is too powerful!")
    tt("With her magic she melts the sword.")
    tt("You are defeated.")
    game_over()


def witch():
    if "sword" in items and "potion" not in items:
        sword_witch()
    elif "sword" not in items and "potion" in items:
        potion_witch()
    elif "sword" not in items and "potion" not in items:
        no_weapons()
        tt("The witch touches you with her wand,")
        tt("and you disapear!")
        tt("You lost.")
        game_over()
    elif "sword" in items and "potion" in items:
        s_or_p()


def potion_troll():
    tt("Good thing you have that magic potion!")
    tt("You open the bottle and throw it at the troll,")
    tt("but the troll just laughs,")
    tt("and bashes you with his club.")
    tt("You lost.")
    game_over()


def sword_troll():
    tt("Luckly you have the sword!")
    tt("You cut the troll in half.")
    tt("The sword is so powerful!")
    tt("Yay! You saved the village!")
    game_over()


def troll():
    if "sword" in items and "potion" not in items:
        sword_troll()
    elif "sword" not in items and "potion" in items:
        potion_troll()
    elif "sword" not in items and "potion" not in items:
        no_weapons()
        tt("The troll hits you with his club.")
        tt("You lost.")
        game_over()
    elif "sword" in items and "potion" in items:
        s_or_p()


def potion_sorcerer():
    tt("Good thing you have that magic potion!")
    tt("You open the bottle and throw it at the sorcerer.")
    tt("The sorcerer begins to melt away!")
    tt("Yay, you saved the village!")
    game_over()


def sword_sorcerer():
    tt("Luckly you have the sword!")
    tt("But the sorcerer just laughs.")
    tt("'The sword is powerful, but not as powerful as me!', he says")
    tt("And he makes you disapear with a wave of his wand.")
    tt("You lose.")
    game_over()


def sorcerer():
    if "sword" in items and "potion" not in items:
        sword_sorcerer()
    elif "sword" not in items and "potion" in items:
        potion_sorcerer()
    elif "sword" not in items and "potion" not in items:
        no_weapons()
        tt("The sorcerer waves his wand,")
        tt("and you disapear, you lose.")
        game_over()
    elif "sword" in items and "potion" in items:
        s_or_p()


def potion_fairie():
    tt("Good thing you have that magic potion!")
    tt("You open the bottle and throw it at the fairie,")
    tt("The fairie begins to melt away!")
    tt("Yay, you saved the village!")
    game_over()


def sword_fairie():
    tt("Luckly you have the sword.")
    tt("But the farie is too fast!")
    tt("He sprinkels his evil fairie dust on you,")
    tt("and he makes you disapear.")
    tt("You lose.")
    game_over()


def fairie():
    if "sword" in items and "potion" not in items:
        sword_fairie()
    elif "sword" not in items and "potion" in items:
        potion_fairie()
    elif "sword" not in items and "potion" not in items:
        no_weapons()
        tt("The fairie sprinkles his evil dust,")
        tt("and you disapear. You lose.")
        game_over()
    elif "sword" in items and "potion" in items:
        s_or_p()


def run_game():
    evil_one()
    intro()
    choice()


run_game()
