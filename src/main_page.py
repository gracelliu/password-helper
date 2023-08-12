import tkinter as tk
from pwd_checker import open_password_checker
from pwd_generator import open_password_generator

def open_home():
    root = tk.Tk()
    root.title("Password Tools")

    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.configure(bg='#f2f2f2')

    title_label = tk.Label(root, text="Password Tools", font=("Helvetica", 20), bg='#f2f2f2')
    title_label.pack(pady=10)

    check_button = tk.Button(root, text="Password Strength Checker", command=open_password_checker, font=("Helvetica", 12), bg='#4caf50', fg='white')
    check_button.pack(pady=10)

    generate_button = tk.Button(root, text="Password Generator", command=open_password_generator, font=("Helvetica", 12), bg='#4caf50', fg='white')
    generate_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    open_home()
