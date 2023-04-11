from tkinter import *

root = Tk()
root.title("GUI")
label = Label(root, text="this is test label")
label.place(x=20, y=20)

label = Label(root, text="this is second test label")
label.place(x=20, y=50)
root.mainloop()
