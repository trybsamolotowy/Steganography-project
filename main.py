from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Steganography - Hide a Secret Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#CCE5FF")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                    title='Select Image File',
                                    filetypes=(("PNG file","*.png"),
                                               ("JPG file","*.jpg"),
                                               ("All files","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
def save():
    secret.save("hidden.png")

def hide():
    global secret
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename), message)

def show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)


#icon
image_icon=PhotoImage(file="logo_1.png")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="broken_glass_smaller.png")
Label(root,image=logo,bg="#CCE5FF").place(x=10,y=0)

Label(root, text="Steganography",fg="black",bg="#CCE5FF",font="arial 50 bold").place(x=180, y = 12)

#first frame
f1=Frame(root,bd=3,bg="black",width=300, height= 280, relief=GROOVE)
f1.place(x=30,y=125)

lbl=Label(f1,bg="black")
lbl.place(x=20,y=10)

#second frame
f2=Frame(root,bd=3,bg="black",width=300, height= 280, relief=GROOVE) 
f2.place(x=370,y=125)

lbl2=Label(f2,bg="black")
lbl2.place(x=40,y=10)

text1=Text(f2,font="arial 20",bg="#CCE5FF",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=294,height=275)

scrollbar1=Scrollbar(f2)
scrollbar1.place(x=277,y=0,height=275)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third frame
#f3=Frame(root, bd=3,bg="#CCE5FF",width=330,height=100,relief=GROOVE)
#f3.place(x=10,y=370)

Button(root,text="Open Image", width=10,height=2, font="arial 12 bold",command=showimage).place(x=58,y=420)
Button(root,text="Save Image", width=10,height=2, font="arial 12 bold",command=save).place(x=188,y=420)

Button(root,text="Hide Data", width=10,height=2, font="arial 12 bold",command=hide).place(x=400,y=420)
Button(root,text="Show Data", width=10,height=2, font="arial 12 bold",command=show).place(x=530,y=420)


root.mainloop()


