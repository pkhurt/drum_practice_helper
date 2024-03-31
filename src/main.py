import tkinter

def button_click():
    print("Button Clicked!")



if __name__ == "__main__":
    print("Drum Practice Helper started.")

    # Create a main window
    root = tkinter.Tk()
    root.title("Simple GUI")

    # Create a button
    button = tkinter.Button(root, text="Click Me!", command=button_click)
    button.pack(pady=10, padx=20)  # Add some padding around the button

    # Run the application
    root.mainloop()