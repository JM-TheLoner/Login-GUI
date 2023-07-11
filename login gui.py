from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("390x300")
root.resizable(False,False)
root.config(bg="#CBD6EE")

name = "1234"
passcode = "1234"


def login():
    username = text_1.get()
    password = code.get()

    if username == name and password == passcode:
        messagebox.showinfo("INFO", "Login Successful")
    elif username == "" and password != "":
        messagebox.showinfo("INFO", "Enter USERNAME")
    elif password == "" and username != "":
        messagebox.showinfo("INFO", "Enter PASSWORD")
    elif username == "" and password == "":
        messagebox.showinfo("INFO", "Blank Not Allowed")
    else:
        messagebox.showinfo("INFO", "Login Failed")


heading = Label(root, text="User Login", fg="black", font=("calibri", 28, "bold"), bg="#CBD6EE").place(x=110, y=5)

Label(root, text="Username", font=("arial", 14), bg="#CBD6EE").place(x=20, y=50)
text_1 = Entry(root, width=26, border=3, bg="white", font=("arial", 18, "bold"))
text_1.place(x=20, y=80)

Label(root, text="Password", font=("arial", 14), bg="#CBD6EE").place(x=20, y=120)
code=StringVar()
Entry(width=20, font=("arial", 23), textvariable=code, bd=0, show="*", border=2, bg="white").place(x=20, y=150)

button = Button(root, width="33", height="1", bg="blue", text="Login", font=("arial", 12, "bold"), fg="white", command=login)
button.place(x=30,y=220)

mainloop()