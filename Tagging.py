from tkinter import *

# Tạo cửa sổ
my_w = Tk()
my_w.geometry("400x300")

#Thêm một label
l1 = Label(my_w,text='Your Name', width=10)
l1.grid(row=1,column=1)

#Thêm một text box
t1 = Text(my_w,width=35,height=4)
t1.grid(row=1,column=2,columnspan=2,pady=30)
font1=('Times',16,'underline')
t1.insert(END, "Hello word")

# Tạo tag_name 'my_hg'
t1.tag_add("my_hg", "1.0", "1.9")
t1.tag_config("my_hg",background="yellow",foreground="red",font=font1)

# xóa tag_name('my_hg') bằng button
b1=Button(my_w,text='Remove tag',command=lambda :t1.tag_remove('my_hg','1.0','1.9'))
b1.grid(row=2,column=2,pady=10)


my_w.mainloop()