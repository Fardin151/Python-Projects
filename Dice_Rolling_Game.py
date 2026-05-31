import tkinter as tk
import random

# ---------------- STATE ----------------
balance = 100
total_rolls = 0

# ---------------- FUNCTIONS ----------------
def flash(color):
    root.config(bg=color)
    root.after(200, lambda: root.config(bg="white"))


def roll_dice():
    global balance, total_rolls

    try:
        num_dice = int(entry.get())
    except:
        result_label.config(text="Enter a valid number!")
        return

    if balance < 10:
        result_label.config(text="💰 Not enough money!")
        return

    # cost per roll
    balance -= 10

    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, 6))

    total = sum(results)
    total_rolls += 1

    # ---------------- GAME LOGIC ----------------
    message = ""

    if total == 7 or total == 11:
        balance += 25
        message = "🏆 YOU WIN +$25!"
        flash("#00ff00")

    elif total in [2, 3, 12]:
        message = "💀 YOU LOSE!"
        flash("#ff0000")

    else:
        message = "⚖️ DRAW!"

    # ---------------- UI UPDATE ----------------
    dice_text = ""
    for i, v in enumerate(results, start=1):
        dice_text += f"Dice {i}: {v}\n"

    result_label.config(text=f"{dice_text}\nTotal: {total}\n{message}")

    balance_label.config(text=f"💰 Balance: ${balance}")
    rolls_label.config(text=f"🎲 Rolls: {total_rolls}")


def reset_game():
    global balance, total_rolls
    balance = 100
    total_rolls = 0

    balance_label.config(text="💰 Balance: $100")
    rolls_label.config(text="🎲 Rolls: 0")
    result_label.config(text="")


# ---------------- UI ----------------
root = tk.Tk()
root.title("🎰 Casino Dice Game")
root.geometry("350x400")
root.config(bg="white")

tk.Label(root, text="Casino Dice Game 🎲", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Number of Dice:").pack()
entry = tk.Entry(root)
entry.insert(0, "2")
entry.pack()

tk.Button(root, text="ROLL 🎲", command=roll_dice).pack(pady=10)
tk.Button(root, text="RESET 🔄", command=reset_game).pack()

balance_label = tk.Label(root, text="💰 Balance: $100", font=("Arial", 12))
balance_label.pack(pady=5)

rolls_label = tk.Label(root, text="🎲 Rolls: 0", font=("Arial", 12))
rolls_label.pack()

result_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()