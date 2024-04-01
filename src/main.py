import tkinter


def button_click():
    print("Button Clicked!")

def create_window():
    root = tkinter.Tk()
    root.title("Welcome to the Drum Practice Helper")
    root.geometry('350x200')
    return root


if __name__ == "__main__":
    print("Drum Practice Helper started.")

    root = create_window()

    # Create a button
    create_random_patter_button = tkinter.Button(root, text="Create Random Drum Letters", command=button_click)
    # create_random_patter_button.pack(pady=10, padx=20)  
    create_random_patter_button.grid(column=1, row=3)



    root.mainloop()