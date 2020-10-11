import sys
import random

def askMot():
    nPlayer = input("Vous voulez jouer a combien de joeur ?\n1 = 1 Joueur  |  2 = 2 Joueur\n=>")
    if (nPlayer == "1"):
        mots = open("mots.txt", "r")
        number_of_lines = len(open('mots.txt').readlines(  ))
        arrayMots = mots.readlines()
        return(arrayMots[random.randint(1, number_of_lines)].lower().replace('\n', ''))
    elif(nPlayer == "2"):
        mot = input("Quel mot voulez vous faire devniner ?\n=>")
        confirmation = input("Vous voulez faire devenier le mot: " + mot + " ?\n1 = Oui 2 = Non\n=>")
        if (confirmation == "1"):
            return mot
        elif(confirmation == "2"):
            return(askMot())
        else:
            print("Vous devez répondre par 1 ou 2.")
            return(askMot())
    else:
        print("Vous devez répondre par 1 ou 2.")
        return(askMot())
        
def askLetter():
    letter = input("Proposez une lettre =>")
    if(len(letter) > 1 or len(letter) <= 0):
        print("Vous pouvez seulement proposer une seul lettre.")
        return(askLetter())
    else:
        return(letter)

def pendu(erreur, mot):
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
        print("Le mot étais:",mot)
        sys.exit()
        
def main():
    erreur = 0
    sucess = 0
    _ = []
    letterTest = []
    mot = askMot()
    for i in range(len(mot)):
        _.append("_")
    while sucess+1 <= len(mot):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        pendu(erreur, mot)
        tempLetterTest = ""
        for l in letterTest:
            tempLetterTest += l + ","
        print("Lettres testé:",tempLetterTest)
        temp_ = ""
        for l in _:
            temp_ += l
        print(temp_)
        letter = askLetter()
        count = 0
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
    print("Félécitation vous avez gagnez !")

main()