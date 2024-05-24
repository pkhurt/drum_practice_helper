import unittest
import tkinter as tk
from tkinter import ttk
import helpers.button_functions as button_functions

# Funktion für den Button 'Convert'
def convert():
    output_label.config(text="Converted Value", fg="white", bg="#2c3e50")

# Testklasse für die GUI-Funktionen
class TestGUIFunctions(unittest.TestCase):

    def setUp(self):
        global root, output_label, input_entry, selected_option, options
        
        root = tk.Tk()
        root.title("GUI example")
        root.geometry("450x350")
        root.configure(bg="#34495e")

        options = ["Option 1", "Option 2", "Option 3"]
        selected_option = tk.StringVar(value=options[0])

        output_label = tk.Label(root, text="", borderwidth=2, relief="solid", width=30, height=10, font=('Arial', 12), bg="white")
        output_label.pack(pady=20)

        input_frame = tk.Frame(root, bg="#34495e")
        input_frame.pack(side=tk.RIGHT, padx=20)

        input_label = tk.Label(input_frame, text="Number of bars:", bg="#34495e", fg="white", font=('Arial', 10))
        input_label.pack(pady=5)

        input_entry = tk.Entry(input_frame, font=('Arial', 10))
        input_entry.pack(pady=5)

        dropdown_label = tk.Label(input_frame, text="Select Option:", bg="#34495e", fg="white", font=('Arial', 10))
        dropdown_label.pack(pady=5)

        dropdown_menu = ttk.Combobox(input_frame, textvariable=selected_option, state="readonly")
        dropdown_menu['values'] = options
        dropdown_menu.pack(pady=5)

        root.update()

    def tearDown(self):
        root.destroy()

    def test_clear_function(self):
        # Simulate input
        input_entry.insert(0, "Test Input")
        output_label.config(text="Converted Value", fg="white", bg="#2c3e50")
        selected_option.set(options[1])
        
        # Call clear function
        button_functions.clear(output_label, input_entry, selected_option, options)

        # Check if fields are cleared
        self.assertEqual(output_label.cget("text"), "")
        self.assertEqual(output_label.cget("fg"), "black")
        self.assertEqual(output_label.cget("bg"), "white")
        self.assertEqual(input_entry.get(), "")
        self.assertEqual(selected_option.get(), options[0])

if __name__ == '__main__':
    unittest.main()