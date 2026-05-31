import random

total_rolls = 0

num_dice = int(input("How many dice do you want to roll? "))

while True:
    command = input("\nType 'roll' or 'exit': ").lower()

    if command == "roll":
        results = []

        for i in range(num_dice):
            roll = random.randint(1, 6)
            results.append(roll)

        total_rolls += 1

        print("\n🎲 You rolled:")
        for i, value in enumerate(results, start=1):
            print(f"Dice {i}: {value}")

        print(f"Total sum: {sum(results)}")
        print(f"Session rolls: {total_rolls}")

    elif command == "exit":
        print("\nGame ended!")
        print(f"Total times rolled: {total_rolls}")
        break

    else:
        print("Invalid command. Type 'roll' or 'exit'.")