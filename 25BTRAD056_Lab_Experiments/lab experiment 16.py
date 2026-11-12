import random

while True:
    roll = random.randint(1, 6)
    print("Dice Result:", roll)

    choice = input("Roll again? (y/n): ")

    if choice.lower() != "y":
        break

print("Game Over!")
