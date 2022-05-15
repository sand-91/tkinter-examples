from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("10x10")
root.resizable(0,0)
root.config(bg="yellow")
root.title("Greetings!")
def click():
	messagebox.showinfo("Hello World","Welcome to Python")
btn=Button(root,text="click me",command=click)
btn.pack()
root.mainloop()
