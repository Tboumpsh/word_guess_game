import tkinter as tk
from tkinter import messagebox
import random
from game.game_logic import load_words_by_topic

def start_game():
    topics = {
        "Animals": "data/animals.txt",
        "Countries": "data/countries.txt",
        "Fruits": "data/fruits.txt"
    }

    def choose_topic():
        topic_window = tk.Toplevel(root)
        topic_window.title("Choose a Topic")
        tk.Label(topic_window, text="Choose a topic to start the game:", font=("Arial", 14)).pack(pady=10)

        def select_topic(topic):
            topic_window.destroy()
            play_game(topic)

        for topic in topics.keys():
            tk.Button(topic_window, text=topic, font=("Arial", 14), command=lambda t=topic: select_topic(t)).pack(pady=5)

    def play_game(topic):
        """شروع بازی با موضوع انتخاب شده."""
        words = load_words_by_topic(topics[topic])
        target_word = random.choice(words)
        guessed_word = ['_'] * len(target_word)
        attempts_left = 6
        guessed_letters = []

        # به‌روزرسانی UI
        word_label.config(text="Word: " + " ".join(guessed_word))
        hint_label.config(text=f"Hint: The word is related to {topic}")
        attempts_label.config(text=f"Attempts Left: {attempts_left}")
        guessed_letters_label.config(text="Guessed Letters: ")

        def submit_guess():
            nonlocal attempts_left
            guess = guess_entry.get().strip().lower()

            if len(guess) != 1 or not guess.isalpha():
                messagebox.showwarning("Invalid Input", "Please enter a single valid letter.")
                return
            if guess in guessed_letters:
                messagebox.showwarning("Already Guessed", "You have already guessed this letter.")
                return

            guessed_letters.append(guess)
            guessed_letters_label.config(text=f"Guessed Letters: {', '.join(guessed_letters)}")

            if guess in target_word:
                for idx, letter in enumerate(target_word):
                    if letter == guess:
                        guessed_word[idx] = guess
                word_label.config(text="Word: " + " ".join(guessed_word))

                if '_' not in guessed_word:
                    messagebox.showinfo("Congratulations!", f"You guessed the word: {target_word}!")
                    root.quit()
            else:
                attempts_left -= 1
                attempts_label.config(text=f"Attempts Left: {attempts_left}")
                if attempts_left == 0:
                    messagebox.showerror("Game Over", f"You lost! The word was: {target_word}")
                    root.quit()

            guess_entry.delete(0, tk.END)

    
        submit_button.config(command=submit_guess)
        guess_entry.delete(0, tk.END)

  
    root = tk.Tk()
    root.title("Word Guess Game")
    root.geometry("600x500")
    root.configure(bg="#BDE4FF")


    tk.Label(root, text="Word Guess Game", font=("Arial", 24, "bold"), bg="#BDE4FF").pack(pady=10)
    hint_label = tk.Label(root, text="Choose a topic to start!", font=("Arial", 16), bg="#BDE4FF")
    hint_label.pack(pady=10)

    word_label = tk.Label(root, text="", font=("Arial", 18), bg="#BDE4FF")
    word_label.pack(pady=10)

    attempts_label = tk.Label(root, text="", font=("Arial", 14), bg="#BDE4FF")
    attempts_label.pack(pady=10)

    guessed_letters_label = tk.Label(root, text="", font=("Arial", 14), bg="#BDE4FF")
    guessed_letters_label.pack(pady=10)

    guess_entry = tk.Entry(root, font=("Arial", 14), justify='center')
    guess_entry.pack(pady=10)

    submit_button = tk.Button(root, text="Submit", font=("Arial", 14))
    submit_button.pack(pady=10)

    restart_button = tk.Button(root, text="Restart", font=("Arial", 14), command=lambda: root.destroy() or start_game())
    restart_button.pack(pady=10)

    choose_topic()
    root.mainloop()
