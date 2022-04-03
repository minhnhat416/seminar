from tkinter import *

#Canvas
root = Tk()
root.title('Lập trình control canvas')
root.geometry("500x500")

# Tạo 1 canvas
cvFirst = Canvas(root, width=300, height=200,bg = 'blue')
cvFirst.pack(pady=20)

# Tạo đường thẳng
# cú pháp: create_line(x1,y1,x2,y2,fill='color'
cvFirst.create_line(0,100,300,100, fill = 'red')
cvFirst.create_line(150,0,150,200,fill = 'red')

# Tạo hình chữ nhật
# cú pháp: create_rectangle(x1,y1,x2,y2,fill = 'pink')
cvFirst.create_rectangle(50,150,250,50, fill='pink')

# Tạo hình elip
cvFirst.create_oval(50,150,250,50,fill='cyan')

# my_canvas.pack(pady=20)

root.mainloop()