from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
def Result(accuracy,speed,second):    
    root=Tk()
    root.title("Typing Speed Tester")
    root.geometry("500x400")
    root.config(bg="firebrick1")

    
    lab_txt=Label(root,text="Your Result Page",font=("Time New Roman",25,"bold"),bg="firebrick1")
    lab_txt.place(x=15,y=10,height=90,width=450)
    sor_txt=Label(root,text=f"Accuracy :- {accuracy}%",font=("Time New Roman",20,"bold"),bg="firebrick1")
    sor_txt.place(x=15,y=100,height=30,width=500)
    Ttext_txt=Label(root,text=f"Speed :- {speed} (Word/minute)",font=("Time New Roman",20,"bold"),bg="firebrick1")
    Ttext_txt.place(x=15,y=140,height=30,width=500)
    text_txt=Label(root,text=f"Time :- {second} (Second)",font=("Time New Roman",20,"bold"),bg="firebrick1")
    text_txt.place(x=15,y=170,height=30,width=500)
    root.mainloop()



