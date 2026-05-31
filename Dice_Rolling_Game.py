import tkinter as tk
import random

# ---------------- STATE ----------------
total_rolls = 0
rolling = False

# ---------------- FUNCTIONS ----------------
def animate_roll(steps, current_step, num_dice, final_results):
    global rolling

    if current_step < steps:
        temp_results = []

        for _ in range(num_dice):
            temp_results.append(random.randint(1, 6))

        result_label.config(text="🎲 Rolling...\n" + str(temp_results))

        root.after(80, animate_roll, steps, current_step + 1, num_dice, final_results)

    else:
        rolling = False
        show_final_result(final_results)


def show_final_result(results):
    global total_rolls

    total_rolls += 1

    text = ""
    for i, value in enumerate(results, start=1):
        text += f"Dice {i}: {value}\n"

    text += f"\nTotal: {sum(results)}"
    text += f"\nSession Rolls: {total_rolls}"

    result_label.config(text=text)


def roll_dice():
    global rolling

    if rolling:
        return

    try:
        num_dice = int(entry.get())
        if num_dice <= 0:
            result_label.config(text="Enter number > 0")
            return
    except:
        result_label.config(text="Enter a valid number!")
        return

    rolling = True

    final_results = [random.randint(1, 6) for _ in range(num_dice)]

    animate_roll(10, 0, num_dice, final_results)


def exit_app():
    root.destroy()


# ---------------- UI ----------------
root = tk.Tk()
root.title("🎲 Dice Simulator (Animated)")
root.geometry("350x350")

tk.Label(root, text="Number of Dice:").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Roll Dice 🎲", command=roll_dice).pack(pady=10)
tk.Button(root, text="Exit ❌", command=exit_app).pack()

result_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()