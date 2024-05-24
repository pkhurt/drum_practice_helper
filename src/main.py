import tkinter as tk
from tkinter import ttk
from helper.button_functions import clear

# Funktion für den Button 'Convert'
def convert():
    output_label.config(text="Converted Value", fg="white", bg="#2c3e50")

# Hauptfenster
root = tk.Tk()
root.title("GUI Beispiel")
root.geometry("450x350")
root.configure(bg="#34495e")

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
convert_button = ttk.Button(button_frame, text="Convert", command=convert)
convert_button.pack(pady=5)

# Clear Button
clear_button = ttk.Button(button_frame, text="Clear", command=clear)
clear_button.pack(pady=5)

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
options = ["8th", "16th"]
selected_option = tk.StringVar()
dropdown_menu = ttk.Combobox(input_frame, textvariable=selected_option, state="readonly")
dropdown_menu['values'] = options
dropdown_menu.pack()

# Set initial values
selected_option.set(options[0])

root.mainloop()