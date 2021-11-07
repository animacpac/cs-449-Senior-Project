from tkinter import *
import os

def delete2():
    screen3.destroy()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
def delete4():
    screen10.destroy()

def logout():\
    print = "screen7.destroy()"
def saved():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Saved")
    screen10.geometry("100x100")
    Label(screen10, text = "Saved").pack()
    Button (screen10, text = "OK").pack()


def save():
    filename = raw_filename.get()
    notes = raw_description.get()
    data = open(filename, 'w')
    data.write(notes)
    data.close()
    saved()
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
    filename1 = raw_filename1.get()
    data = open(filename1, "r")
    data = data.read()
    screen12 = Toplevel(screen)
    screen12.title("Info")
    screen12.geometry("400x400")
    Label(screen12, text = "Business description")
  
 
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
    Button (screen11, text = "View Description", command= view_description).pack()



def session():
    screen8 = Toplevel(screen)
    screen8.title("dashboard")
    screen8.geometry("400x400")
    Label(screen8, text = "Welcome to the dashboard")
    Button (screen8, text = "Create business description", command= create_description).pack()
    Button (screen8, text = "View description", command= view_description).pack()
    Button (screen8, text = "Delete description").pack()


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