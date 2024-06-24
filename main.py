import tkinter as tk
from tkinter import ttk
import helpers.button_functions as button_functions


def start_gui():
    root = tk.Tk()
    root.title("Drum Practice Helper")
    root.geometry("450x350")
    root.configure(bg="#34495e")

    title_label = tk.Label(root, text="Welcome to the Drum Practice Helper \n It creates practice syntax for you", font=("Helvetica", 16))
    title_label.pack(pady=10)

    # Styles für Buttons und Dropdown
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 10), padding=5)
    style.configure('TCombobox', font=('Arial', 10))
    style.map('TButton', background=[('active', '#2980b9'), ('!active', '#3498db')], foreground=[('active', 'white'), ('!active', 'white')])

    # Output Label
    output_label = tk.Label(root, text="", borderwidth=2, relief="solid", width=30, height=10, font=('Arial', 12), bg="white")
    output_label.pack(pady=20)

    # Frame für Buttons
    button_frame = tk.Frame(root, bg="#34495e")
    button_frame.pack(side=tk.LEFT, padx=20)

    # Convert Button
    convert_button = ttk.Button(button_frame, text="Convert", command= lambda: button_functions.convert(output_label))
    convert_button.pack(pady=5)

    # Frame für Eingabe und Dropdown
    input_frame = tk.Frame(root, bg="#34495e")
    input_frame.pack(side=tk.RIGHT, padx=20)

    # Label für Eingabefeld
    input_label = tk.Label(input_frame, text="Number of bars:", bg="#34495e", fg="white", font=('Arial', 10))
    input_label.pack(pady=5)

    # Eingabefeld
    input_entry = tk.Entry(input_frame, font=('Arial', 10))
    input_entry.pack(pady=5)

    # Label für Dropdown Menü
    dropdown_label = tk.Label(input_frame, text="Select Subdivision:", bg="#34495e", fg="white", font=('Arial', 10))
    dropdown_label.pack(pady=5)

    # Dropdown Menü
    options = ["16th", "8th"]
    selected_option = tk.StringVar()
    number_of_bars = ttk.Combobox(input_frame, textvariable=selected_option, state="readonly")
    number_of_bars['values'] = options
    number_of_bars.pack()

    # Set initial values
    selected_option.set(options[0])

    # Clear Button
    clear_button = ttk.Button(button_frame, text="Clear", command= lambda: button_functions.clear(output_label, input_entry, selected_option, options))
    clear_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    start_gui()