from tkinter import *
import random
from PIL import Image, ImageTk

def errorWindow(erreurMsg):
    errorWindow = Toplevel(mainWindow)
    errorWindow.geometry("500x500")

    errorWindow.title("Erreur")
    errorWindow.iconbitmap("pendu.ico")

    label = Label(errorWindow, text="Erreur: " + erreurMsg)
    label.pack()

def winWindow():
    winWindow = Toplevel(mainWindow)

    winWindow.title("Vous avez gagnez !")
    winWindow.iconbitmap("pendu.ico")

    label = Label(winWindow, text="Félécitations vous avez gagnez !", font=("Courrier", 40))
    label.pack()

def loseWindow():
    loseWindow = Toplevel(mainWindow)

    loseWindow.title("Vous avez perdu.")
    loseWindow.iconbitmap("pendu.ico")

    label = Label(loseWindow, text="Dommage, vous avez perdu.", font=("Courrier", 40))
    label.pack()

    motLabel = Label(loseWindow, text="Le mot était : " + mot, font=("Courrier", 40))
    motLabel.pack()

mots = open("mots.txt", "r")
number_of_lines = len(open('mots.txt').readlines(  ))
arrayMots = mots.readlines()
mot = arrayMots[random.randint(1, number_of_lines)].lower().replace('\n', '')
_ = []
letterTest = []
erreur = 0
sucess = 0
count = 0

for i in range(len(mot)):
    _.append("_")

def show_():
    temp_ = ""
    for l in _:
        temp_ += l + " "
    return(temp_)

def testLetter():
    global erreur
    global sucess
    global count
    global _
    global letterTest
    letter = entry.get()
    if(len(letter) > 1):
        errorWindow("Vous avez rentrer trop plus de une lettre !")
    else:
        if letter not in letterTest:
            letterTest.append(letter)
            for i in range(len(mot)):
                if(mot[i] == letter):
                    for o in range(len(_)):
                        if(o == i):
                            _[o] = mot[i]
                            sucess += 1
                else:
                    count += 1
            if(count >= len(mot)):
                erreur += 1
        temp_ = ""
        for l in _:
            temp_ += l + " "
        label.config(text = temp_)
        load = Image.open("erreur"+str(erreur)+".png") 
        render = ImageTk.PhotoImage(load)
        imageLabel.config(image=render)
        imageLabel.image = render
        tempLetterTest = ""
        for l in letterTest:
            tempLetterTest += l + ","
        letterTestLabel.config(text = "Lettres testé : " + tempLetterTest)
        if(sucess == len(mot)):
            winWindow()
        elif(erreur > 9):
            loseWindow()

mainWindow = Tk()

mainWindow.title("Pendu by Elyter")
mainWindow.geometry("1500x720")
mainWindow.minsize(480, 360)
mainWindow.iconbitmap("pendu.ico")

load = Image.open("erreur0.png") 
render = ImageTk.PhotoImage(load)
imageLabel = Label(mainWindow, image=render)
imageLabel.pack(side=RIGHT)

label = Label(mainWindow, text=show_(), font=("Courrier", 30))
label.pack(expand=YES)

letterTestLabel = Label(mainWindow, text="Lettres testé : ", font=("Courrier", 25))
letterTestLabel.pack(expand=YES)

entry = Entry(mainWindow, font=("Courrier", 25))
entry.pack(expand=YES)

enter = Button(mainWindow, text="Ok", font=("Courrier", 15), command=testLetter)
enter.pack(expand=YES)

mainWindow.mainloop()