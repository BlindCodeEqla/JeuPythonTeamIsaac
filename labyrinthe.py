import enigma, combat, labyrinthe, timer, timerSound
from math import floor
from random import *
import winsound
from winsound import *
import threading
import time
import sys
import wave
import threading

def InsideLabyrinthe(_labyrintheSize): 
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
			#     idx -= 2
			#     print("Oupssss, vous êtes retournez dans le couloir précédent")
			if playerChoice == 1 or playerChoice == 2 or playerChoice == 3:
				PlaySound("fantomes", SND_ASYNC | SND_FILENAME)
				playerChoice = int(input("Vous êtes dans un cul de sac... Veuillez tapez \"0\" pour retourner!!!! "))
				while playerChoice != 0: 
					PlaySound("fantomes", SND_ASYNC | SND_FILENAME)
					playerChoice = int(input("mauvais choix, Vous êtes toujours dans un cul de sac, Veuillez tapez \"0\" pour retourner!!!! "))
				PlaySound("fermeture", SND_ASYNC | SND_FILENAME)
			else:
				PlaySound("faux", SND_ASYNC | SND_FILENAME)
				print("mauvais choix. Veuillez tapez \"1\", \"2\" ou \"3\"  ")
			print("Etape " + str(idx+1) + "/" + str(_labyrintheSize))
			playerChoice = int(input("te voilà dans un couloir et 3 choix s'offrent à toi. "))
		PlaySound("ouverture", SND_ASYNC | SND_FILENAME)
		print("Bravo, très bon choix")
		# i = labyrintheSize - 1
		if idx == i : 
			PlaySound("applaudissement", SND_ASYNC | SND_FILENAME)
			print("Bravo, vous avez réussi à quitter le labyrinthe vivant... ")



def Labyrinthe(_labyrintheSize): 
	beginChoice = input("Tu es piégé dans un labyrinthe, tu dois en sortir en ouvrant 5 portes maximum, si tu en ouvres plus, cela voudra dire que ca fait trop longtemps que tu es dansle labyrinthe et tu vas mourir. \n Utilise la tourch \"1\" pour aller à gauche, \"2\" pour aller tout droit,\"3\" pour aller à droite et \"0\" pour retourner en arrière. \n \n si vous êtes prêt, tapez \"go\" : ")
	if beginChoice == "go": 
		InsideLabyrinthe(_labyrintheSize)
	else: 
		print(" Vous êtes lâche ")

