import tkinter as tk
import random
# Rock, Paper, Scissors Game 🎮

# Computer's Turns
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

# Winner
def who_wins(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Rock') or \
         (player == 'Scissors' and computer == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Play one round
def play_round(player_choice):
    global current_round, user_score, computer_score

    if current_round > total_rounds:
        result_label.config(text="Game over! Please reset.", fg="white")
        return

    computer_choice = get_computer_choice()
    outcome = who_wins(player_choice, computer_choice)

    user_choice_label.config(text=f"You chose: {player_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    # Show result 
    if "You win" in outcome:
        result_label.config(text=outcome, fg="#0b9343")  
        user_score += 1
    elif "Computer wins" in outcome:
        result_label.config(text=outcome, fg="#ae1f0f")  
        computer_score += 1
    else:
        result_label.config(text=outcome, fg="#efc105")  

    score_label.config(text=f"🏆 Score — You: {user_score} | Computer: {computer_score}")
    round_label.config(text=f"📊 Round: {current_round} / {total_rounds}")

    current_round += 1

    if current_round > total_rounds:
        show_final_result()

def show_final_result():
    if user_score > computer_score:
        result_label.config(text="🎉 You won the game!", fg="#ffd700")
    elif computer_score > user_score:
        result_label.config(text="😢 Computer won the game!", fg="#ae1f0f")
    else:
        result_label.config(text="🤝 It's a draw!", fg="#efc105")
    disable_buttons()

def reset_game():
    global user_score, computer_score, current_round
    user_score = 0
    computer_score = 0
    current_round = 1

    user_choice_label.config(text="You chose: -")
    computer_choice_label.config(text="Computer chose: -")
    result_label.config(text="", fg="white")
    score_label.config(text="🏆 Score — You: 0 | Computer: 0")
    round_label.config(text=f"📊 Round: {current_round} / {total_rounds}")
    enable_buttons()

def disable_buttons():
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")

def enable_buttons():
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")

# GUI Setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("460x480")
root.resizable(False, False)

# Theme colors
colors = {"bg": "#02183c","text": "#ecf0f1","button_text": "#01080e","rock": "#43d1cf",
    "paper": "#db8712", "scissors": "#82bb33","reset": "#f3d046","exit": "#A92719"
}
root.configure(bg=colors["bg"])
# Game Variables
user_score = 0
computer_score = 0
current_round = 1
total_rounds = 5

# Labels
title_label = tk.Label(root, text="Rock, Paper, Scissors!", font=("Helvetica", 20, "bold"), bg=colors["bg"], fg=colors["text"])
title_label.pack(pady=15)

instruction_label = tk.Label(root, text="Choose your weapon:", font=("Helvetica", 14), bg=colors["bg"], fg=colors["text"])
instruction_label.pack()

# Buttons (Rock / Paper / Scissors)
button_frame = tk.Frame(root, bg=colors["bg"])
button_frame.pack(pady=15)

rock_button = tk.Button(button_frame, text="🪨 Rock", font=("Helvetica", 12, "bold"),
                        bg=colors["rock"], fg=colors["button_text"], width=12,
                        command=lambda: play_round("Rock"))
rock_button.grid(row=0, column=0, padx=10, pady=5)

paper_button = tk.Button(button_frame, text="📄 Paper", font=("Helvetica", 12, "bold"),
                         bg=colors["paper"], fg=colors["button_text"], width=12,
                         command=lambda: play_round("Paper"))
paper_button.grid(row=0, column=1, padx=10, pady=5)

scissors_button = tk.Button(button_frame, text="✂️ Scissors", font=("Helvetica", 12, "bold"),
                            bg=colors["scissors"], fg=colors["button_text"], width=26,
                            command=lambda: play_round("Scissors"))
scissors_button.grid(row=1, column=0, columnspan=2, pady=8)

# Output Labels
user_choice_label = tk.Label(root, text="You chose: -", font=("Helvetica", 12), bg=colors["bg"], fg=colors["text"])
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer chose: -", font=("Helvetica", 12), bg=colors["bg"], fg=colors["text"])
computer_choice_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg=colors["bg"], fg="white")
result_label.pack(pady=10)

score_label = tk.Label(root, text="🏆 Score — You: 0 | Computer: 0", font=("Helvetica", 12, "bold"), bg=colors["bg"], fg=colors["text"])
score_label.pack(pady=5)

round_label = tk.Label(root, text=f"📊 Round: {current_round} / {total_rounds}", font=("Helvetica", 12), bg=colors["bg"], fg=colors["text"])
round_label.pack(pady=5)

# Control Buttons
control_frame = tk.Frame(root, bg=colors["bg"])
control_frame.pack(pady=10)

reset_button = tk.Button(control_frame, text="🔄 RESET", font=("Helvetica", 11), width=10,
                         bg=colors["reset"], fg=colors["button_text"], command=reset_game)
reset_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(control_frame, text="❌ EXIT", font=("Helvetica", 11), width=10,
                        bg=colors["exit"], fg="black", command=root.quit)
exit_button.grid(row=0, column=1, padx=10)

# Start the GUI
root.mainloop()
