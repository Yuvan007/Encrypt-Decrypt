from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()

    if password == "1234":
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#48b521")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="DECRYPTED TEXT:",font="arial",fg="white",bg="#48b521").place(x=10,y=0)
        text2=Text(screen2,font="arial 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=14,y=40,width=370,height=150)

        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password!="1234":
        messagebox.showerror("encryption","Invalid Password") 

def encrypt():
    password=code.get()

    if password == "1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#e64322")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPTED TEXT:",font="arial",fg="white",bg="#e64322").place(x=10,y=0)
        text2=Text(screen1,font="arial 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=14,y=40,width=370,height=150)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password!="1234":
        messagebox.showerror("encryption","Invalid Password")        

def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("400x400")

    #icon
    image_icon=PhotoImage(file="Key.png")
    screen.iconphoto(False,image_icon)
    screen.title("Encrypt/Decrypt App")

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter text for Encryption and Decryption: ",fg="black",font=("times new roman",15)).place(x=10,y=10)
    text1=Text(font="poppins 15",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=380,height=100)

    Label(text="Enter Secret key for Encryption and Decryption: ",fg="black",font=("times new roman",13)).place(x=10,y=170)
    
    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",27),show="*").place(x=10,y=200)

    Button(text="ENCRYPT",height="2",width="25",bg='#d13313',fg='white',bd=0,command=encrypt).place(x=10,y=260)
    Button(text="DECRYPT",height="2",width='25',bg='#947b2f',fg='white',bd=0,command=decrypt).place(x=210,y=260)
    Button(text="RESET",height="2",width='54',bg='#08629e',fg='white',bd=0,command=reset).place(x=10,y=310)

    screen.mainloop()
main_screen()