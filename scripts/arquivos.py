from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count+=1
    print(count)

window = Tk()

# photo = PhotoImage(file='qrcode.png')

button = Button(window,text="Sed", command=click, font=("Comic Sans",30), fg="#00FF00", bg="black", activeforeground="#00FF00", activebackground="black", state=ACTIVE, compound='bottom')
button2 = Button(window,text="Boletim", command=click, font=("Comic Sans",30), fg="#00FF00", bg="black", activeforeground="#00FF00", activebackground="black", state=ACTIVE, compound='bottom')
button3 = Button(window,text="Home", command=click, font=("Comic Sans",30), fg="#00FF00", bg="black", activeforeground="#00FF00", activebackground="black", state=ACTIVE, compound='bottom')


# state=ACTIVE,
# image=photo,


button.pack()
button2.pack()
button3.pack()

window.mainloop()
