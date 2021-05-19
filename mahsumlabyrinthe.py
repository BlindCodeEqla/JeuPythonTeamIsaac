from random import * 


def insideLabyrinthe(_labyrintheSize): 
	rightWay = []
	for i in range(1, _labyrintheSize):
		a = randint(1,3)
		b = i-1
		rightWay.append(a)
	for idx, goodChoice in enumerate(rightWay):
		print("Etape " + str(idx+1) + "/" + str(_labyrintheSize))
		playerChoice = int(input("te voilà dans un couloir et 3 choix s'offrent à toi. "))
		# print(goodChoice)
		while playerChoice != goodChoice : 
			# if playerChoice == 0 and idx > 0:
			# 	idx -= 1
			# 	print("Oupssss, vous êtes retournez dans le couloir précédent")
			if playerChoice == 1 or playerChoice == 2 or playerChoice == 3:
				playerChoice = int(input("Vous êtes dans un cul de sac... Veuillez tapez \"0\" pour retourner!!!! "))
				while playerChoice != 0: 
					playerChoice = int(input("mauvais choix, Vous êtes toujours dans un cul de sac, Veuillez tapez \"0\" pour retourner!!!! "))
			else:
				print("mauvais choix. Veuillez tapez \"1\", \"2\" ou \"3\"  ")
			print("Etape " + str(idx+1) + "/" + str(_labyrintheSize))
			playerChoice = int(input("te voilà dans un couloir et 3 choix s'offrent à toi. "))
		print("Bravo, très bon choix")
		# i = labyrintheSize - 1
		if idx == i : 
			print("Bravo, vous avez réussi à quitter le labyrinthe vivant... ")



def labyrinthe(_labyrintheSize): 
	beginChoice = input("Tu es piégé dans un labyrinthe, tu dois en sortir en ouvrant 5 portes maximum, si tu en ouvres plus, cela voudra dire que ca fait trop longtemps que tu es dansle labyrinthe et tu vas mourir. \n Utilise la tourch \"1\" pour aller à gauche, \"2\" pour aller tout droit,\"3\" pour aller à droite et \"0\" pour retourner en arrière. \n \n si vous êtes prêt, tapez \"go\" : ")
	if beginChoice == "go": 
		insideLabyrinthe(_labyrintheSize)
	else: 
		print(" Vous êtes lâche ")



labyrintheSize = 5
labyrinthe(labyrintheSize)