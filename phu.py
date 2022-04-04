from tkinter import *
window = Tk()
window.title ("Welcome to our app")
lbl=Label(window,text= "Hello everyone")
lbl.pack()
window.mainloop()

# from tkinter import *
# window =Tk()
# var1 = IntVar()
# Checkbutton(window,text = 'male', variable = var1). grid(row = 0, sticky=W)
# var2 = IntVar()
# Checkbutton(window, text='female', variable=var2). grid (row=1,sticky=W)
# window.mainloop()

# from tkinter import *
# window = Tk()
# scrollbar = Scrollbar(window)
# scrollbar.pack(side=RIGHT, fill=Y)
# ds = Listbox(window, yscrollcommand=scrollbar.set)
# for line in range(100):
#    ds.insert(END, 'This is line number' + str(line))
# ds.pack( side = LEFT, fill=BOTH)
# scrollbar.config( command=ds.yview)
# mainloop()



from tkinter import *
window= Tk()
pane = Frame(window)
pane.pack(fill=BOTH, expand=True)

# Button 1
b1 = Button(pane, text="Click me !",
            background="black", fg="white")
b1.pack(side=TOP, expand=True, fill=BOTH)

# Button 2
b2 = Button(pane, text="Click me too",
            background="blue", fg="white")
b2.pack(side=TOP, expand=True, fill=BOTH)

# Button 3
b3 = Button(pane, text="I'm also button",
            background="green", fg="white")
b3.pack(side=TOP, expand=True, fill=BOTH)

# Execute Tkinter
window.mainloop()
