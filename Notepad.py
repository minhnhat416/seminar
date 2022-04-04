from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("600x600")
root.title("Notepad")
root.config(bg='lightpink')
root.resizable(False, False)


def save_file():
    open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if open_file is None:
        return
    text = str(box1.get(1.0, END))
    open_file.write(text)
    open_file.close()


def open_file():
    file = filedialog.askopenfile(mode='r', filetype=[('text files', ' *.txt')])
    if file is not None:
        noidung = file.read()
    box1.insert(INSERT, noidung)


Button1 = Button(root, width='20', height='2', bg='lightblue', text='save file', command=save_file)
Button1.place(x=50, y=5)
Button2 = Button(root, width='20', height='2', bg='lightblue', text='open file', command=open_file)
Button2.place(x=400, y=5)
box1 = Text(root, height='33', width='72', wrap=WORD)
box1.place(x=10, y=60)

root.mainloop()



