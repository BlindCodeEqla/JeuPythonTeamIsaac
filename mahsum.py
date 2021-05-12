# playerChoice=int(input(" "))
# nomberTry=5
# nomberSmall=0
# nomberBig=100
# enigmaChoice=randint(nomberSmall, nomberBig)
# addingTime=15
# addingPv=2

# print("GENIAL! De la compagnie, je n'ai vu personne depuis que je susi malade (13 mars 2020) Tu resteras avec moi temps que tu n'auras pas résolu mon enigme, mais attention, car si tu restes trop longtemps, tu seras contaminé!\n
	# Voici l'énigme:\n
	# Je pense a un chiffre entre" , nomberSmall , "et" , nomberBig , "tu as le droit à " , nomberTry , "propositions, en fonction des tes réponses je te donnerai un indice."

# global beginTime
# global beginPv 	

from random import *
numberTry=10
tryMax = numberTry
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
while i < tryMax and playerChoice != enigmaChoice: 
    if(playerChoice < enigmaChoice):
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