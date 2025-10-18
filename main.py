import tkinter as tk
from tkinter import messagebox

from generator import generate_password, evaluate_strength
from widgets import create_password_block

# --- UI + App logic ---
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
        messagebox.showerror("Error", "Invalid count.")
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
        pw = generate_password(length, prefs["uppercase"], prefs["lowercase"], prefs["numbers"], prefs["specials"])
        strength, color = evaluate_strength(pw, prefs)
        create_password_block(passwords_frame, pw, strength, color)

# --- UI Setup ---
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x650")
root.configure(bg="#eaf6fd")
root.resizable(True, True)

tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#eaf6fd").pack(pady=15)

# Length input
length_frame = tk.Frame(root, bg="#eaf6fd")
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password Length (8–128):", bg="#eaf6fd").pack(side="left")
length_var = tk.StringVar(value="12")
tk.Entry(length_frame, textvariable=length_var, width=5, justify="center").pack(side="left", padx=5)

# Count input
count_frame = tk.Frame(root, bg="#eaf6fd")
count_frame.pack(pady=5)
tk.Label(count_frame, text="How many passwords?", bg="#eaf6fd").pack(side="left")
count_var = tk.StringVar(value="3")
tk.Entry(count_frame, textvariable=count_var, width=5, justify="center").pack(side="left", padx=5)

# Options
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

tk.Button(root, text="Generate Passwords", command=update_passwords, bg="#2196f3", fg="white", font=("Arial", 11)).pack(pady=10)

# Scrollable output area
canvas = tk.Canvas(root, bg="#eaf6fd", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#eaf6fd")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(fill="both", expand=True, side="left")
scrollbar.pack(fill="y", side="right")

passwords_frame = scrollable_frame

root.mainloop()
