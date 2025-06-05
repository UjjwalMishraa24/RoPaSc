import random

suchak = { -1:"rock 🪨", 0 : "paper📃", 1 : "scissors✂️"}
computer = random.choice([-1, 0, 1])
try:
    your_num = int(input("Enter -1 for rock 🪨, 0 for paper 📃, and 1 for scissors ✂️   "))
    if your_num not in suchak:
        raise ValueError
    print(f"you choose {suchak[your_num]} and computer choose {suchak[computer]}")

    if (your_num == computer):
        print("It's a tie!")

    elif (your_num == -1 and computer == 0) or \
         (your_num == 0 and computer == 1)  or \
         (your_num == 1 and computer == -1):
        print("you loose, you snooze 🤡🤡🤡")

    elif (your_num == 0 and computer == -1) or\
         (your_num == 1 and computer == 0) or\
        (your_num == -1 and computer == 1):
        print("you Win, Sherrrrrrr !!!!!!!🦁🦁🦁🔥🔥")

except (ValueError, KeyError):
    print('''you have entered a wrong input please only choose between
          -1:"rock 🪨"
           0 : "paper📃"
          1 : "scissors✂️" ''')



