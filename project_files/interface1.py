from tkinter import *
import ml1
def key(a):
    ml1.activate()
def interface():
    root=Tk()
    root.geometry("550x400+400+200")
    root.title("Your account")
    root.resizable(0,0)
    root.config(background="black")
    n=StringVar()


    l=Label(root,text="Welcome",background="black",foreground="white")
    l.config(font=("Times New Roman",35,"bold"))
    l.pack(fill="y",pady="40")
    l=Label(root,text="please enter your pin.",background="black",foreground="white")
    l.config(font=("Courier",12))
    l.pack(ipadx="5")

    E=Entry(root,text=n,relief="sunken")
    E.pack(pady="10")

    b=Button(root,text="ENTER",background="white",foreground="black",command=ml1.activate)
    b.pack()
    root.bind("<Return>",key)

    root.mainloop()
if __name__ == '__main__':
    interface()