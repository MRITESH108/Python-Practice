import  random

options=["Rock", "Paper", "Scissors"]

while True:
    user_choice =input("Rock, Paper, Scissors, Exit?").title()
    if user_choice=="Exit":
        print("Jb khelai k time Nahi ba t kahe aawathya")
        break
    if user_choice not in options:
        print("Sahi input dala marde.")
        continue

    system_choice = random.choice(options)
    print(f"System choice is : {system_choice}")

    if system_choice == user_choice:
        print("It's a tie.")
    if (user_choice == "Rock" and system_choice== "Scissors") or (user_choice == "Scissors" and system_choice== "Paper") or (user_choice=="Paper" and system_choice=="Rock") :
        print("You win!!. Yeee")

    else:
        print("System wins.")



