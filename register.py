from tkinter import *
from tkinter import filedialog

import subprocess
import os
import Asymmetric
import caesar
import rsa
import rc4
import fernet
import des
import time


def delete2():
    print("ok")
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
def delete5():
    screen10.destroy()
def delete13():
    screen13.destroy()
def delete14():
    screen14.destroy()
def delete15():
    screen15.destroy()
def delete16():
    screen16.destroy()
def delete17():
    screen17.destroy()
def delete18():
    screen18.destroy()
def delete20():
    screen20.destroy()

def logout():\
    print("screen7.destroy()")
def saved():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Saved")
    screen10.geometry("100x100")
    Label(screen10, text = "Saved").pack()
    Button (screen10, text = "OK").pack()


def save():
    filename = raw_filename.get()
    notes = raw_filename.get()
    data = open(filename, 'w')
    data.write(notes)
    data.close()
    saved()


def businestype():
    screen19 = Toplevel(screen)
    screen19.geometry("400x400")
    def show():
        suggestion = StringVar()
        if clicked.get() == "Small":
            suggestion = "AES"
        if clicked.get() == "Medium":
            suggestion = "DES"
        if clicked.get() == "Large":
            suggestion = "AES, DES, RSA" 
            
    
        label.config( text = suggestion )

    options = [
        "Small",
        "Medium",
        "Large",
    ]
    clicked = StringVar()
         
    drop = OptionMenu( screen19 , clicked , *options )
    drop.pack()
    Button( screen19 , text = "Suggestion" , command = show ).pack()
    label = Label( screen19 , text = " " )
    label.pack()

def create_description():
    global raw_filename
    raw_filename = StringVar()
    global raw_description
    raw_description = StringVar()

    screen9 = Toplevel(screen)
    screen9.title("Business description")
    screen9.geometry("300x250")

    Label(screen9, text = "Enter filename").pack()
    Entry(screen9, textvariable= raw_filename).pack()
   
  
    Label(screen9, text = "Enter description").pack()
    Entry(screen9, textvariable= raw_description).pack()
    Button (screen9, text = "Save", command= save).pack()
    
def view_description1():
    filename1 = raw_filename.get()
    data = open(filename1, "r")
    data1 = data.read()
    screen12 = Toplevel(screen)
    screen12.title("Info")
    screen12.geometry("400x400")
    Label(screen12, text = data1).pack()

def monitor():
    os.system("C:\Windows\System32\perfmon.exe /res")
    delete20() 

def execaes():
    global screen18
    screen18 = Toplevel(screen)
    screen18.title("Info")
    screen18.geometry("400x400")
    Label(screen18, text = "Time in senconds").pack()
    start = time.time()
    Asymmetric.main()
    Label(screen18, text = time.time() - start).pack()
    print(screen18, "% s seconds" % (time.time() - start))
    Button(screen18, text="OK", command= delete18).pack()
    f = open("times.txt", "a")
    f.write("\n AES: "+format(time.time() - start)+"\n")
    f.close()

def execdes():
    global screen17
    screen17 = Toplevel(screen)
    screen17.title("Info")
    screen17.geometry("400x400")
    Label(screen17, text = "Time in senconds").pack()
    start = time.time()
    des.main()
    Label(screen17, text = time.time() - start).pack()
    print(screen17, "% s seconds" % (time.time() - start))
    Button(screen17, text="OK", command= delete17).pack()
    f = open("times.txt", "a")
    f.write("\n DES: "+format(time.time() - start)+"\n")
    f.close()

def execceaser():
    global screen16
    screen16 = Toplevel(screen)
    screen16.title("Info")
    screen16.geometry("400x400")
    Label(screen16, text = "Time in senconds").pack()
    start = time.time()
    caesar.main()
    Label(screen16, text = time.time() - start).pack()
    print(screen16, "% s seconds" % (time.time() - start))
    Button(screen16, text="OK", command= delete16).pack()
    f = open("times.txt", "a")
    f.write("\n Ceaser: "+format(time.time() - start)+"\n")
    f.close()


def execrc4():
    global screen15
    screen15 = Toplevel(screen)
    screen15.title("Info")
    screen15.geometry("400x400")
    Label(screen15, text = "Time in senconds").pack()
    start = time.time()
    rc4.main()
    Label(screen15, text = time.time() - start).pack()
    print(screen15, "% s seconds" % (time.time() - start))
    Button(screen15, text="OK", command= delete15).pack()
    f = open("times.txt", "a")
    f.write("\n RC4: "+format(time.time() - start)+"\n")
    f.close()

def execrsa():
    global screen14
    screen14 = Toplevel(screen)
    screen14.title("Info")
    screen14.geometry("400x400")

    Label(screen14, text = "Time in senconds").pack()
    start = time.time()
    rsa.main()
    Label(screen14, text = time.time() - start).pack()
    print(screen14, "% s seconds" % (time.time() - start))
    Button(screen14, text="OK", command= delete14).pack()
    f = open("times.txt", "a")
    f.write("\n RSA: "+format(time.time() - start)+"\n")
    f.close()

def execfernet():
    global screen13
    screen13 = Toplevel(screen)
    screen13.title("Info")
    screen13.geometry("400x400")
    
    Label(screen13, text = "Time in senconds").pack()
    start = time.time()
    fernet.main()
    Label(screen13, text = time.time() - start).pack()
    print(screen13, "% s seconds" % (time.time() - start))
    Button(screen13, text="OK", command= delete13).pack()
    f = open("times.txt", "a")
    f.write("\n FERNET: "+format(time.time() - start)+"\n")
    f.close()

def view_description():
    screen11 = Toplevel(screen)
    screen11.title("Info")
    screen11.geometry("400x400")
    Label(screen11, text = "Business description")
    all_files = os.listdir()
    Label(screen11, text= all_files).pack()
    global raw_filename1
    raw_filename1 = StringVar()
    Entry(screen11, textvariable=raw_filename1).pack()
    Button (screen11, text = "View Description", command= view_description1).pack()
   
def view_log():
    screen19 = Toplevel(screen)
    screen19.title("Info")
   
    pathh = Entry(screen19)
    pathh.pack(side=LEFT, expand=True, fill=X, padx=20)
    txtarea = Text(screen19, width=40, height=20)
    txtarea.pack(pady=20)
  
    tf = filedialog.askopenfilename(
        initialdir=".\cs-449-Senior-Project", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

def run_test():
    screen12 = Toplevel(screen)
    screen12.title("Info")
    screen12.geometry("400x400")
    Label(screen12, text = "Encryptions")
   
    Label(screen12, text= 'Encryptions').pack()
      
    Button (screen12, text = "AES", command= execaes).pack()
    Button (screen12, text = "DES", command= execdes).pack()
    Button (screen12, text = "Caesar", command= execceaser).pack()
    Button (screen12, text = "RC4", command= execrc4).pack()
    Button (screen12, text = "RSA", command= execrsa).pack()
    Button (screen12, text = "Fernet", command= execfernet).pack()

def monitor_launch():
    global screen20
    screen20 = Toplevel(screen)
    screen20.title("Monitor")
    screen20.geometry("400x400")
    Label(screen20, text = "Monitor")
    Button(screen20, text = "Monitor", command= monitor).pack()
    

def session():
    screen8 = Toplevel(screen)
    screen8.title("dashboard")
    screen8.geometry("400x400")
    Label(screen8, text = "Welcome to the dashboard")
    Button (screen8, text = "Create business description", command= create_description).pack()
    Button (screen8, text = "View description", command= view_description).pack()
    Button (screen8, text = "Run Test", command= run_test).pack()
    Button (screen8, text = "Select Business", command= businestype).pack()
    Button (screen8, text = "View Log", command= view_log).pack()
    Button (screen8, text = "Monitor", command= monitor_launch).pack()



def login_sucess():
    session()



def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text = "Password not found").pack()
    Button(screen4, text="OK", command = delete3).pack()

def user_not_found():
    global screen5
    screen5= Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text = "Username not found").pack()
    Button(screen5, text="OK", command = delete4).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write (username_info+"\n")
    file.write (password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Successiful", fg = "green",font = ("Calibri", 13)).pack()

def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognized()
    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    
    username = StringVar()
    password = StringVar()

    Label (screen1, text = "Please enter details below").pack()
    Label (screen1, text = "").pack()
    Label (screen1, text = "Username * ").pack()
    username_entry = Entry (screen1, textvariable = username)
    username_entry.pack()
    Label (screen1, text = "Password * ").pack()
    password_entry = Entry (screen1, textvariable = password)
    password_entry.pack()
    Label (screen1, text = "").pack()
    Button(screen1, text = "Register", height="1", width="10", command= register_user).pack()
    Label (text = "").pack()
    

  
def login():
    global screen2
    global username_entry1
    global password_entry1


    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label (screen2, text = "Please enter details below to login").pack()
    Label (screen2, text = "").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    Label (screen2, text = "Username * ").pack()
    username_entry1 = Entry (screen2, textvariable = username_verify)
    username_entry1.pack()
    Label (screen2, text = "").pack()
    Label (screen2, text = "Password * ").pack()
    password_entry1 = Entry (screen2, textvariable = password_verify)
    password_entry1.pack()
    Label (screen2, text = "").pack()

    Button(screen2, text = "Login", height="1", width="10", command= login_verify).pack()


    print("Login session started")

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label (text = "Notes 1.0", bg = "grey",width= "300", height="2", font = ("Calibri", 13)).pack()
    Label (text = "").pack()
    Button(text = "Login", height="2", width="30", command = login).pack()
    Label (text = "").pack()
    Button(text = "Register", height="2", width="30", command = register).pack()

    screen.mainloop()

main_screen()