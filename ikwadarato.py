from tkinter import *

fen = Tk()

l=Label(fen, text="First label", font ="arial 18 italic", bg='orange')
#l.pack()

b = Button(fen, text="Bouger", command="", bg ='blue')
#b.pack()

value = StringVar()
value.set("napis")
entree=Entry(fen, width=40, bg='green')
entree.pack()

cb1 = Checkbutton(fen, text="Nouveau?")
cb2=Checkbutton(fen, text="Recent")

value=StringVar()
b1=Radiobutton(fen, text="Oui",  variable=value, value=1)
b2=Radiobutton(fen, text="Non",  variable=value, value=2)


liste=Listbox(fen)
liste.insert(1,"Napoléon")
liste.insert(2,"Pivoine")
liste.insert(3,"Napis")
liste.insert(4,"Napise")

can=Canvas(fen, width=300, height=300, bg='yellow')
boule = can.create_oval(50,100,150, width=2)
can.pack()
#liste.pack()
#b1.pack()
#b2.pack()
#cb1.pack()
#cb2.pack()
fen.mainloop()
