import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
comp_score = 0
high_score = 0

def play(user_choice):
    global user_score, comp_score, high_score
    comp_choice = random.choice(choices)

    user_label.config(text="You: " + user_choice)
    comp_label.config(text="Computer: " + comp_choice)

    if user_choice == comp_choice:
        result_label.config(text="It's a Tie!")
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        result_label.config(text="You Win!")
        user_score += 1
    else:
        result_label.config(text="You Lose!")
        comp_score += 1

    if user_score > high_score:
        high_score = user_score

    score_label.config(text=f"Score  You: {user_score}   Computer: {comp_score}")
    highscore_label.config(text=f"Highest Wins: {high_score}")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_label.config(text="You: -")
    comp_label.config(text="Computer: -")
    result_label.config(text="")
    score_label.config(text="Score  You: 0   Computer: 0")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x370")

tk.Label(root, text="Choose Your Move", font=("Arial",14)).pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

user_label = tk.Label(root, text="You: -", font=("Arial",12))
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer: -", font=("Arial",12))
comp_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial",14))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score  You: 0   Computer: 0", font=("Arial",12))
score_label.pack(pady=5)

highscore_label = tk.Label(root, text="Highest Wins: 0", font=("Arial",12))
highscore_label.pack(pady=5)

tk.Button(root, text="Reset Game", command=reset_game).pack(pady=10)

root.mainloop()