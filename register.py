import tkinter as tk
from tkinter import *
import os
def main_screen():
    screen = tk.Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label (text = "Notes 1.0", bg = "grey", font = ("Calibri", 13)).pack()
    Label (text = "").pack()
    Button(text = "Login").pack()
    Button(text = "Register").pack()
    screen.mainloop()
main_screen()