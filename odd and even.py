import random

print(" Odd or Even Game ")

player_inchoice = input("Choose 'odd' or 'even': ")

player_inhand = int(input("Show your hand (1-5): "))

computer_inhand = random.randint(1, 5)
print(f"Computer shows: {computer_inhand}")

total = player_inhand + computer_inhand
print(f"Total: {player_inhand} + {computer_inhand} = {total}")

if (total % 2 == 0 and player_inchoice == "even") or (total % 2 == 1 and player_inchoice == "odd"):
    print(" You win!")
else:
    print(" You lose!")