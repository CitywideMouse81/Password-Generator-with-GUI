import tkinter as tk
from tkinter import messagebox
import string
import random

# --- Character Set Setup ---
def get_character_sets():
    return {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase,
        'digits': string.digits,
        'special': string.punctuation
    }

# --- Password Generator Logic ---
def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    if not any([use_uppercase, use_lowercase, use_numbers, use_special]):
        return ""

    sets = get_character_sets()
    chars = set()
    required = []

    if use_lowercase:
        chars.update(sets['lowercase'])
        required.append(random.choice(sets['lowercase']))
    if use_uppercase:
        chars.update(sets['uppercase'])
        required.append(random.choice(sets['uppercase']))
    if use_numbers:
        chars.update(sets['digits'])
        required.append(random.choice(sets['digits']))
    if use_special:
        chars.update(sets['special'])
        required.append(random.choice(sets['special']))

    if len(required) > length:
        return "Length too short."

    all_chars = list(chars)
    password = required[:]
    for _ in range(length - len(required)):
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

# --- Password Strength Evaluation ---
def evaluate_strength(password, prefs):
    score = 0
    if len(password) >= 12:
        score += 1
    if sum([prefs['uppercase'], prefs['lowercase'], prefs['numbers'], prefs['specials']]) >= 3:
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score == 3:
        return "Strong", "green"
    elif score == 2:
        return "Medium", "orange"
    else:
        return "Weak", "red"

# --- GUI Update Logic ---
def update_passwords():
    try:
        length = int(length_var.get())
        if length < 8 or length > 128:
            messagebox.showerror("Error", "Password length must be between 8 and 128")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for length.")
        return

    try:
        count = int(count_var.get())
        if count < 1 or count > 20:
            messagebox.showerror("Error", "Please enter a number between 1 and 20")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number of passwords.")
        return

    prefs = {
        "uppercase": uppercase_var.get(),
        "lowercase": lowercase_var.get(),
        "numbers": numbers_var.get(),
        "specials": specials_var.get()
    }

    for widget in passwords_frame.winfo_children():
        widget.destroy()

    for _ in range(count):
        password = generate_password(length, prefs["uppercase"], prefs["lowercase"], prefs["numbers"], prefs["specials"])
        strength, color = evaluate_strength(password, prefs)

        pw_var = tk.StringVar(value="•" * len(password))
        actual_pw = [password]

        block = tk.Frame(passwords_frame, bg="#f4f4f4", padx=5, pady=5)
        block.pack(padx=10, pady=6, fill="x")

        entry = tk.Entry(block, textvariable=pw_var, font=("Courier", 12), width=30, state="readonly", justify="center")
        entry.pack(side="left", padx=5)

        def make_toggle(pw_var=pw_var, actual_pw=actual_pw, btn=None):
            def toggle():
                if pw_var.get().startswith("•"):
                    pw_var.set(actual_pw[0])
                    btn.config(text="Hide")
                else:
                    pw_var.set("•" * len(actual_pw[0]))
                    btn.config(text="Show")
            return toggle

        show_btn = tk.Button(block, text="Show")
        show_btn.pack(side="left", padx=5)
        show_btn.config(command=make_toggle(btn=show_btn))

        def copy_pw(pw=actual_pw[0]):
            root.clipboard_clear()
            root.clipboard_append(pw)
            root.update()
            copy_btn.config(text="Copied!")
            copy_btn.after(1200, lambda: copy_btn.config(text="Copy"))

        copy_btn = tk.Button(block, text="Copy", bg="#4caf50", fg="white", command=copy_pw)
        copy_btn.pack(side="left", padx=5)

        strength_label = tk.Label(block, text=f"Strength: {strength}", fg=color, bg="#f4f4f4", font=("Arial", 9))
        strength_label.pack(side="left", padx=10)

# --- Main App Setup ---
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x650")
root.configure(bg="#eaf6fd")
root.resizable(True, True)

tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#eaf6fd").pack(pady=15)

# Length Input
length_frame = tk.Frame(root, bg="#eaf6fd")
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length (8–128):", bg="#eaf6fd").pack(side="left")
length_var = tk.StringVar(value="12")
tk.Entry(length_frame, textvariable=length_var, width=5, justify="center").pack(side="left", padx=5)

# Password Count Input
count_frame = tk.Frame(root, bg="#eaf6fd")
count_frame.pack(pady=5)
tk.Label(count_frame, text="How many passwords?", bg="#eaf6fd").pack(side="left")
count_var = tk.StringVar(value="3")
tk.Entry(count_frame, textvariable=count_var, width=5, justify="center").pack(side="left", padx=5)

# Character Set Options
options_frame = tk.Frame(root, bg="#eaf6fd")
options_frame.pack(pady=5)

uppercase_var = tk.IntVar(value=1)
lowercase_var = tk.IntVar(value=1)
numbers_var = tk.IntVar(value=1)
specials_var = tk.IntVar(value=1)

tk.Checkbutton(options_frame, text="Uppercase", variable=uppercase_var, bg="#eaf6fd").pack(side="left", padx=10)
tk.Checkbutton(options_frame, text="Lowercase", variable=lowercase_var, bg="#eaf6fd").pack(side="left", padx=10)
tk.Checkbutton(options_frame, text="Numbers", variable=numbers_var, bg="#eaf6fd").pack(side="left", padx=10)
tk.Checkbutton(options_frame, text="Specials", variable=specials_var, bg="#eaf6fd").pack(side="left", padx=10)

# Generate Button
tk.Button(root, text="Generate Passwords", command=update_passwords, bg="#2196f3", fg="white", font=("Arial", 11)).pack(pady=10)

# Scrollable Canvas for Password Display
canvas = tk.Canvas(root, bg="#eaf6fd", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#eaf6fd")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(fill="both", expand=True, side="left")
scrollbar.pack(fill="y", side="right")

passwords_frame = scrollable_frame

root.mainloop()
