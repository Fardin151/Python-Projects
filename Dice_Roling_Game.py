import tkinter as tk
import random

# ---------------- App State ----------------
total_rolls = 0

# ---------------- Functions ----------------
def roll_dice():
    global total_rolls

    try:
        num_dice = int(entry.get())
    except:
        result_label.config(text="Enter a valid number!")
        return

    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, 6))

    total_rolls += 1

    result_text = ""
    for i, value in enumerate(results, start=1):
        result_text += f"Dice {i}: {value}\n"

    result_text += f"\nTotal: {sum(results)}"
    result_text += f"\nSession Rolls: {total_rolls}"

    result_label.config(text=result_text)


def exit_app():
    root.destroy()


# ---------------- UI Setup ----------------
root = tk.Tk()
root.title("🎲 Dice Simulator")
root.geometry("300x300")

# Input
tk.Label(root, text="Number of Dice:").pack()
entry = tk.Entry(root)
entry.pack()

# Buttons
tk.Button(root, text="Roll Dice 🎲", command=roll_dice).pack(pady=10)
tk.Button(root, text="Exit ❌", command=exit_app).pack()

# Output
result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

# Run app
root.mainloop()