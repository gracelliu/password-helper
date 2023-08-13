import tkinter as tk
import random
import string

def open_password_generator():
    def generate_password():
        # Get the user inputs
        password_length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()

        # Validate the user inputs
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special_chars:
            characters += string.punctuation

        if not characters:
            result_label.config(text="Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(password_length))
        result_label.config(text="Generated Password: " + password)

    # Create the Tkinter window
    root = tk.Tk()
    root.title("Password Generator")

    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create UI elements
    root.configure(bg='#f2f2f2')

    title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 20), bg='#f2f2f2')
    title_label.pack(pady=10)

    length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12), bg='#f2f2f2')
    length_label.pack()

    length_entry = tk.Entry(root, font=("Helvetica", 12))
    length_entry.pack()

    # Initialize BooleanVar variables for the checkboxes
    uppercase_var = tk.BooleanVar()
    digits_var = tk.BooleanVar()
    special_chars_var = tk.BooleanVar()

    uppercase_check = tk.Checkbutton(root, text="Case sensitive", variable=uppercase_var, font=("Helvetica", 12), bg='#f2f2f2')
    uppercase_check.pack()

    digits_check = tk.Checkbutton(root, text="Digits", variable=digits_var, font=("Helvetica", 12), bg='#f2f2f2')
    digits_check.pack()

    special_chars_check = tk.Checkbutton(root, text="Special Characters", variable=special_chars_var, font=("Helvetica", 12), bg='#f2f2f2')
    special_chars_check.pack()

    generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12), bg='#4caf50', fg='white')
    generate_button.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Helvetica", 12), bg='#f2f2f2')
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    open_password_generator()
