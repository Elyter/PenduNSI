import sys

def askLetter():
    letter = input("=>")
    if(len(letter) > 1 or len(letter) <= 0):
        print("Vous pouvez seulement proposer une seul lettre.")
        return(askLetter())
    else:
        return(letter)

mot="test"
sucess = 0
erreur = 0
_ = "____"
while sucess <= len(mot):
    for i in range(len(mot)):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if (erreur == 1):
            print("___\n\n")
        elif(erreur == 2):
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("___\n\n")
        elif(erreur == 3):
            print(" |---")
            print(" |")
            print(" |")
            print(" |")
            print("___\n\n")
        elif(erreur == 4):
            print(" |---")
            print(" |  o")
            print(" |")
            print(" |")
            print("___\n\n")
        elif(erreur == 5):
            print(" |---")
            print(" |  o")
            print(" |  |")
            print(" |")
            print("___\n\n")
        elif(erreur == 6):
            print(" |---")
            print(" |  o")
            print(" | -|")
            print(" |")
            print("___\n\n")
        elif(erreur == 7):
            print(" |---")
            print(" |  o")
            print(" | -|-")
            print(" |")
            print("___\n\n")
        elif(erreur == 8):
            print(" |---")
            print(" |  o")
            print(" | -|-")
            print(" | |")
            print("___\n\n")
        elif(erreur == 9):
            print(" |---")
            print(" |  o")
            print(" | -|-")
            print(" | | |")
            print("___\n\n")
            print("Vous avez perdu !")
            sys.exit()
        new_ = ""
        if(new_ == ""):
            print(_)
        else:
            print(new_)
        letter = askLetter()
        for i in range(len(mot)):
            if(mot[i] == letter):
                for o in range(len(_)):
                    if(o == i):
                        new_ += mot[i]
                        sucess += 1
                    else:
                        new_ += "_"
            else:
                erreur += 1
                break