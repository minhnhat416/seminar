import tkinter as tk

my_w = tk.Tk()
my_w.geometry("400x300")
l1 = tk.Label(my_w,text='Your Name', width=10) #added one Label
l1.grid(row=1,column=1)

t1 = tk.Text(my_w,width=35,height=4) #text box
t1.grid(row=1,column=2,columnspan=2,pady=30)

font1=('Times',16,'underline')
t1.insert(tk.END, "Welcome to plus2net\n Hello word")

# tag name my_hg is created
t1.tag_add("my_hg", "1.0", "1.9")
t1.tag_config("my_hg",background="yellow",foreground="red",font=font1)

#t1.tag_delete('my_hg')
b1=tk.Button(my_w,text='Remove tag',command=lambda :t1.tag_remove('my_hg','1.0','1.9'))
b1.grid(row=2,column=2,pady=10)


my_w.mainloop()