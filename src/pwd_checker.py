import tkinter as tk
import re

def open_password_checker():

    def is_strong_password(password):
        criteria_met = {
            'length': len(password) >= 8,
            'uppercase': re.search(r'[A-Z]', password) is not None,
            'lowercase': re.search(r'[a-z]', password) is not None,
            'digit': re.search(r'\d', password) is not None,
            'special': re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password) is not None
        }

        return criteria_met

    def update_checkmarks(criteria):
        length_var.set('✔' if criteria['length'] else '✘')
        uppercase_var.set('✔' if criteria['uppercase'] else '✘')
        lowercase_var.set('✔' if criteria['lowercase'] else '✘')
        digit_var.set('✔' if criteria['digit'] else '✘')
        special_var.set('✔' if criteria['special'] else '✘')

    def check_password_strength():
        password = password_entry.get()
        criteria = is_strong_password(password)
        update_checkmarks(criteria)

        criteria_count = sum(criteria.values())

        if criteria_count == 5: # If all criteria are met
            password_label.config(text="You slayed!", fg="green")
        elif 3 <= criteria_count <= 4:
            password_label.config(text="Could be better", fg="orange")
        else:
            password_label.config(text="nuh uh", fg="red")

    # Create the src window
    root = tk.Tk()
    root.title("Password Strength Checker")

    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.configure(bg='#f2f2f2')

    # Create UI elements
    title_label = tk.Label(root, text="Password Strength Checker", font=("Helvetica", 18), bg='#f2f2f2')
    title_label.pack(pady=10)

    password_label = tk.Label(root, text="Enter a Password:", font=("Helvetica", 12), bg='#f2f2f2')
    password_label.pack()

    password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
    password_entry.pack()

    check_button = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Helvetica", 12), bg='#4caf50', fg='white')
    check_button.pack(pady=10)

    criteria_frame = tk.Frame(root, bg='#f2f2f2')
    criteria_frame.pack()

    # Create checkmarks for criteria
    length_var = tk.StringVar(value='✘')
    uppercase_var = tk.StringVar(value='✘')
    lowercase_var = tk.StringVar(value='✘')
    digit_var = tk.StringVar(value='✘')
    special_var = tk.StringVar(value='✘')

    tk.Label(criteria_frame, text="Length (>= 8):", bg='#f2f2f2').grid(row=0, column=0)
    tk.Label(criteria_frame, textvariable=length_var, bg='#f2f2f2').grid(row=0, column=1)

    tk.Label(criteria_frame, text="Uppercase:", bg='#f2f2f2').grid(row=1, column=0)
    tk.Label(criteria_frame, textvariable=uppercase_var, bg='#f2f2f2').grid(row=1, column=1)

    tk.Label(criteria_frame, text="Lowercase:", bg='#f2f2f2').grid(row=2, column=0)
    tk.Label(criteria_frame, textvariable=lowercase_var, bg='#f2f2f2').grid(row=2, column=1)

    tk.Label(criteria_frame, text="Digit:", bg='#f2f2f2').grid(row=3, column=0)
    tk.Label(criteria_frame, textvariable=digit_var, bg='#f2f2f2').grid(row=3, column=1)

    tk.Label(criteria_frame, text="Special Character:", bg='#f2f2f2').grid(row=4, column=0)
    tk.Label(criteria_frame, textvariable=special_var, bg='#f2f2f2').grid(row=4, column=1)

    root.mainloop()

if __name__ == '__main__':
    open_password_checker()
