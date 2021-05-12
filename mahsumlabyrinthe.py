left = 1
front = 2 
right = 3
goBack = 0 
beginpPv= 4

playerChoice = int(input("Tu es piégé dans un labyrinthe, tu dois en sortir en ouvrant 5 portes maximum, si tu en ouvres plus, cela voudra dire que ca fait trop longtemps que tu es dansle labyrinthe et tu vas mourir. \n Utilise la tourch \"1\" pour aller à gauche, \"2\" pour aller tout droit,\"3\" pour aller à droite et \"0\" pour retourner en arrière. \nMaintenant, choisis une porte: "))

i=0
while i<5 and (playerChoice==1 or playerChoice==2 or playerChoice==3):
	if playerChoice == 1:
		int(input("te voilà dans un couloir et 3 choix s'offre à toi:"))
		if playerChoice == 2:
			int(input("te voilà dans un couloir et 3 choix s'offre à toi."))
			if playerChoice==1:
				print("Félicitation, tu t'es échapé du Donjon, et tu es vivant!!!!")
	elif playerChoice == 2:
		int(input("tu es dans une chambre de contaminé! sort vite en tappant 0: "))
	elif playerChoice == 3:
		int(input("tu es dans une chambre de contaminé! sort vite en tappant 0: "))
	if playerChoice == 0:
		int(input("tu es revenu à l'endroit ou tu te trouvai. quel chois vas tu prendre?"))
	i+=1
