BeginChoice = int(input("AH-AH DOMMAGE POUR TOI! Tu es coincé dans l'unité infecté par le virus Covid, ta mission, si tu l'accesptes (sinon tape \"5\" pour quitter le jeu), est de sorir vivant de l'unité Covid en X minutes.Tu peux essayer de quitter l'unité en prenant 3  chemis différents, mais attention, ce ne sera pas si simple, des épreuves t'y attendent...tape \"1\"  pour aller a gauche(Enigma), \"2\" pour aller en avant(Combat) et \"3\" pour aller a droite (labyrinte) et \"0\" pour reculer"))

if BeginChoice==5:
    print("Vous n'avez pas le courage de combattre le virus")

if beginChoice==1:
    Enigma()
if beginChoice==2:
    print(
if beginChoice==3:
    print("")
beginTime = 90 
BeginPV= 4


def Enigma(): 
    # from random import 
    numberTry=5
    numberSmall=0
    numberBig=100
    enigmaChoice = randint(numberSmall, numberBig)
    addingTime=15
    addingPv=2

    print("GENIAL! De la compagnie, je n'ai vu personne depuis que je susi malade (13 mars 2020) Tu resteras avec moi temps que tu n'auras pas résolu mon enigme, mais attention, car si tu restes trop longtemps, tu seras contaminé!\n Voici l'énigme:\n Je pense a un chiffre entre" , numberSmall , "et" , numberBig , "tu as le droit à " , numberTry , "propositions, en fonction des tes réponses je te donnerai un indice.")

    # global beginTime
    # global beginPv 	

    i=1
    playerChoice = int(input("Donne ton choix numéro " + str(i) + " : "))
    while i < 5 and playerChoice != enigmaChoice: 
        if(playerChoice < enig maChoice):
            # numberSmall = playerChoice
            numberTry -= 1
            playerChoice = int(input("plus haut! il te reste " + str(numberTry) + " choix, quel chiffre choisis tu ?:"))
        elif playerChoice > enigmaChoice: 
            numberTry -= 1
            playerChoice = int(input("plus bas! il te reste " + str(numberTry) + " choix, quel chiffre choisis tu ?:"))
        i +=1
    else: 
        if playerChoice == enigmaChoice: 
            print("OOOOOh dommage, tu vas devoir quitter ma chambre. \n Comme récompense, je t'offre" + str(addingTime) + " secondes ou pv. \n courage pour trouver ton chemin....")
        else:
            print("Super tu as été infecté, On va partager ma chambre pour la vie ") 
