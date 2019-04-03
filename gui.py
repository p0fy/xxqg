from tkinter import *
from xxqg import XXQGBot

root = Tk()
root.geometry('450x300')

##################
## qrcode login ##
image = PhotoImage(file="code.png")
qrcode = Label(root, image=image)
info = Label(root, text='Scan code to login')
qrcode.pack(expand=2)
info.pack(expand=1)
##################


root.mainloop()
