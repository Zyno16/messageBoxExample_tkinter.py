import tkinter
from tkinter import ttk
from tkinter import messagebox

form=tkinter.Tk()
form.geometry("700x500")

btns = ttk.Style()
btns.configure("TButton" ,font =("tahoma",30),padding =10)
def mbox():
    messagebox.showerror("error","this is error")
    messagebox.showinfo("error","this is message-info")
    messagebox.askokcancel("error","this is message-askokcancel")
    messagebox.askquestion("error","this is message-askquestion")
    messagebox.askretrycancel("error","this is message-askretrycance")
    messagebox.showwarning("error","this is message-showwarning")
    messagebox.askyesnocancel("error","this is message-askyesnocancel")
   
    

btn =ttk.Button(form,text ="show message",command = mbox)
btn.pack()
               
 
