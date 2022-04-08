from random import *
import time

#Idée :
#-Utiliser le code ASCII pour chiffrer le code de Déchiffrement

print("\n")
print("  #####   #######  ##  ##   ##  ##              ####   ##   ##   ####      ####   #######")
print(" ##   ##   ##   #  ##  ##   ##  ##             ##  ##  ##   ##    ##      ##  ##  #   ##")
print(" #         ## #     ####    ##  ##            ##       ##   ##    ##     ##          ##")
print("  #####    ####      ##      ####             ##       ##   ##    ##     ##         ##")
print("      ##   ## #     ####      ##              ##  ###  ##   ##    ##     ##  ###   ##")
print(" ##   ##   ##   #  ##  ##     ##               ##  ##  ##   ##    ##      ##  ##  ##    #")
print("  #####   #######  ##  ##    ####               #####   #####    ####      #####  #######")
print("\n \n")



def Compte_A_Rebour(seconde):
    """The Compte_A_Rebour function allows you to pause the execution of the code.
    The pause time depends on the second variable. The variable second is of type int."""
    while seconde:
        m, s = divmod(seconde, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        time.sleep(1)
        seconde -= 1

def Chiffrement_ASCII(mot):
    """The Chiffrement_ASCII function takes a str text value
     and returns a tuple consisting of the crypted text and the key used to decrypt it.
     This function will take the ASCII code of each letter and then add and multiply by
      a random value chosen between 1 and 100."""
    ListeMot = []

    #Creating variables
    Addition = randint(1,100)
    Multiplication = randint(1,100)

    #Creating a list containing ASCII numbers
    for i in mot:
        ListeMot.append(ord(i))
    for i in range(len(ListeMot)):
        ListeMot[i] = (ListeMot[i] + Addition) * Multiplication

    #Creating the word Encrypt
    MotChiffrer = ""
    for i in range(len(ListeMot)):
        MotChiffrer = MotChiffrer + str(ListeMot[i]) + "."

    #Creation of the key
    Clé = str(Multiplication) + "." + str(Addition)
    return (MotChiffrer,Clé)

def Déchiffrement_ASCII(Mot_Chiffrer,Clé):
    """The function Déchiffrement_ASCII takes as parameters a encrypted text provided
     by the function Chiffrement_ASCII and a key provided by the function Chiffrement_ASCII.
      This function will return the text Decrypt. """

    #Using the key to create the variables Addition and Multiplication
    Addition = ""
    Multiplication = ""
    cpt = True
    for i in Clé:
        if i == ".":
            cpt = False
        elif (cpt):
            Multiplication = Multiplication + i
        else:
            Addition = Addition + i

    #Creation of a list containing the cipher words
    ListeLettre = []
    while len(Mot_Chiffrer) != 0 :
        cpt = 0 
        Lettre = ""
        while Mot_Chiffrer[cpt] != ".":
            Lettre = Lettre + Mot_Chiffrer[cpt]
            cpt = cpt + 1
        ListeLettre.append(Lettre)
        Mot_Chiffrer = Mot_Chiffrer[cpt + 1 :]
    

    #Decoding numbers
    for i in range(len(ListeLettre)):
        ListeLettre[i] = int((int(ListeLettre[i]) / int(Multiplication)) - int(Addition))

    #Converting Numbers to Letters and Creating the Word Decipher
    Mot_Déchiffrer = ""
    for i in range(len(ListeLettre)):
        ListeLettre[i] = chr(int(ListeLettre[i]))
        Mot_Déchiffrer = Mot_Déchiffrer + str(ListeLettre[i])

    return Mot_Déchiffrer




def action():
    file = "Vie1.txt" #Replace Vie1 with the name of the file you wish to encrypt
    fichier = open(file,"r")
    variable = fichier.read()
    fichier.close()
    Bool = int(input("Do you want to Encrypt or Decrypt the file ? \n Encryption - 1                  Decryption - 2 \n answer : "))
    if Bool == 1 :
        #File encryption
        mot = Chiffrement_ASCII(variable)
        fichier = open(file,"w")
        fichier.write(mot[0])
        fichier.close()
        print("Encryption in progress ...")
        Compte_A_Rebour(2)
        print("The file has been encrypted")
        Compte_A_Rebour(1)
        print("Thank you for encrypting your file with SexyGuigz software")
        print("Your decryption code is : ", mot[1])
    else: 
        #File decryption
        clé = input("Enter the encryption key : ")
        fichier = open(file,"w")
        fichier.write(Déchiffrement_ASCII(variable,clé))
        fichier.close()
        print("Decryption in progress ...")
        Compte_A_Rebour(2)
        print("The file has been decrypted")
        Compte_A_Rebour(1)
        print("Thank you for decrypting your file with SexyGuigz software")

action()
print(" \n --------------- Touch a button to exit ---------------")


#Allows you not to close the python shell when the program has finished running.
x = input()
