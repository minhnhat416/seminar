from tkinter import*
root = Tk()

# radio button
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1)
R1.pack(anchor=W)

R2 = Radiobutton(root, text="Option 2", variable=var, value=2)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="Option 3", variable=var, value=3)
R3.pack(anchor=W)


# frame
frame = Frame(root)
frame.pack()
b1_button = Button(frame, text="Nút 1", fg="red")
b1_button.pack(side=LEFT)
b2_button = Button(frame, text="Nút 2", fg="green")
b2_button.pack(side=LEFT)
b3_button = Button(frame, text="Nút 3", fg="blue")
b3_button.pack(side=LEFT)

# TEXT
my_text = Text(root, width=60, height=20, font=("Helvetica", 16))
my_text.insert(INSERT, "Nhập văn bản :")
my_text.pack(padx=5, pady=5)
mainloop()

