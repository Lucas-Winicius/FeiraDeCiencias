import tkinter as tk

text_to_be_printed = None


def goToSed():
    global text_to_be_printed
    text_to_be_printed = "sed"
    print(text_to_be_printed)

def goToBoletim():
    global text_to_be_printed
    text_to_be_printed = "Boletim"
    print(text_to_be_printed)

root = tk.Tk()

results_label = tk.Label(root, text="")

sed = tk.Button(root, text="sed", command=goToSed)
boletim = tk.Button(root, text="Boletim", command=goToBoletim)

sed.pack()
boletim.pack()

root.mainloop()