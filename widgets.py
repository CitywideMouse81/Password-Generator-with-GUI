import tkinter as tk

def create_password_block(root, password, strength, color):
    pw_var = tk.StringVar(value="•" * len(password))
    actual_pw = [password]

    block = tk.Frame(root, bg="#f4f4f4", padx=5, pady=5)
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
