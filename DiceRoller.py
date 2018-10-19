import random


def main():
    dice_roll()
    play_again()


def dice_roll():
    print(random.randint(1,6))


def play_again():
    ask_for_play = input("Do you want to play again ")
    print(ask_for_play)
    if ask_for_play.lower() == "yes" or ask_for_play.upper() == "Y":
        print("Condition met")
        main()
    else:
        print("ByeBye")


if __name__ == "__main__":
    main()

