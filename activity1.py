from tkinter import *

window = Tk()
window.title("Tkinter Sample Window")
window.geometry("300x300")

greeting = Label(text="Hello User", fg='white', bg='pink')
button = Button(text="Click me", bg='black', fg='white')
entry = Entry(fg='black', bg='teal', width=50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window , relief=RAISED , borderwidth=5)
frame.pack()
label = Label(master=frame , text='Sample frame')
label.pack()

text=Text(fg="teal" , bg="black")
text.pack()
window.mainloop()