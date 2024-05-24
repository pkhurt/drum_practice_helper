import tkinter as tk

def clear(output_label, input_entry, selected_option, options):
    output_label.config(text="", fg="black", bg="white")
    input_entry.delete(0, tk.END)
    selected_option.set(options[0])