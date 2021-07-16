from tkinter import *
from random import randint
import pyperclip

root = Tk()
root.title('Password generator')
root.geometry("500x300")

def new_rand():
	password_entry.delete(0, END)
	pw_length = int(my_entry.get())
	my_password = ''

	for x in range(pw_length):
		my_password += chr(randint(33,126))

	password_entry.insert(0, my_password)

def copytoclipboard():
    pyperclip.copy(password_entry.get())

labelframe = LabelFrame(root, text="How Many Characters?")
labelframe .pack(pady=20)

my_entry = Entry(labelframe, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

password_entry = Entry(root, text='', font=("Helvetica", 24))
password_entry.pack(pady=20)


my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboad", command=copytoclipboard)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
