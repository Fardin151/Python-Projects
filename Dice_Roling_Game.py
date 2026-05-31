import random

# Stats
total_rolls = 0
wins = 0
losses = 0
draws = 0

print("🎲 Dice Game CLI")
print("Type 'roll' to play or 'exit' to quit")

while True:
    command = input("\nEnter command: ").lower()

    if command == "roll":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2

        total_rolls += 1

        print(f"Dice 1: {dice1}")
        print(f"Dice 2: {dice2}")
        print(f"Total: {total}")

        if total == 7 or total == 11:
            print("🏆 You win!")
            wins += 1

        elif total in [2, 3, 12]:
            print("💀 You lose!")
            losses += 1

        else:
            print("⚖️ Draw!")
            draws += 1

    elif command == "exit":
        break

    else:
        print("Invalid command. Type 'roll' or 'exit'.")

# Final stats
print("\n📊 Game Over Stats:")
print(f"Total Rolls: {total_rolls}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Draws: {draws}")

if total_rolls > 0:
    win_rate = (wins / total_rolls) * 100
    print(f"Win Rate: {win_rate:.2f}%")
else:
    print("No games played.")