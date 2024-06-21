import random

def display_instructions():
    print("\n")
    print("                          Let's get started")
    print("\n")
    print("======================= Rock🗿 Paper📄 Scissors✂️ Game ===========================")
    print("\n\n")

    print("         Instructions :                                 ")

    print("\n \n \t \t \t      Rock🗿 \n \n \t \t \t ↗ \n \n \t \t Paper📄              ↘ \n \n \t \t \t    ↖ \n \t \t \t \t Scissors✂️")
    print("\n\n")

    print("\n \t \t \t ● Rock beats Scissors \n \t \t \t ● Scissors beats Paper \n \t \t \t ● Paper beats Rock")

    print("\n\n")
    print("\tEnter : ")
    print("\n \t \t \t ● 0 for Rock🗿 \n \t \t \t ● 1 for Paper📄 \n \t \t \t ● 2 for Scissors✂️")
    print("\n \n \t      -------------------------------")

def play_game():
    value = {0: "Rock🗿", 1: "Paper📄", 2: "Scissors✂️"}

    you = int(input("\n \n \t \t ➡   You : "))
    computer = random.randint(0, 2)

    print("\n \n \t \t ➡   Computer : ", computer)

    print("\n \n \t      -------------------------------")
  
    print("\n \n \t \t ➡   You chose: ", value[you])
    print("\n \n \t \t ➡   Computer chose: ", value[computer])

    print("\n \n \t      -------------------------------")

    if computer == 0 and you == 1:
        print("\n \n \t \t    Ohhh You lost ❌")
        print("\n \n \t \t    Computer Won")
    elif computer == 0 and you == 2:
        print("\n \n \t \t Congrates!! 🥳 🎊")
        print("\n \n \t \t    You Won")
    elif computer == 1 and you == 0:
        print("\n \n \t \t Congrates!! 🥳 🎊")
        print("\n \n \t \t    You Won")
    elif computer == 1 and you == 2:
        print("\n \n \t \t    Ohhh..You lost ❌")
        print("\n \n \t \t    Computer Won")
    elif computer == 2 and you == 0:
        print("\n \n \t \t    Ohhh You lost ❌")
        print("\n \n \t \t    Computer Won")
    elif computer == 2 and you == 1:
        print("\n \n \t \t Congrates!! 🥳 🎊")
        print("\n \n \t \t    You Won")
    else:
        print("\n \n \t \t      Ohhh Nooo 🙀")
        print("\n \n \t \t      Tie the GAME")

    print("\n\n")

def main():
    display_instructions()
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

print("\n\n")



