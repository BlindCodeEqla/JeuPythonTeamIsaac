from math import floor
from random import *
import winsound
from winsound import *
import threading
import time
import sys
import wave
import threading

from enigma import * 
from combat import * 
from labyrinthe import *


def Hopython(_timer):
    beginChoice = int(input("AH-AH DOMMAGE POUR TOI! Tu es coincé dans l'unité infecté par le virus Covid, ta mission, si tu l'acceptes (sinon tape \"5\" pour quitter le jeu), est de sorir vivant de l'unité Covid en X minutes.Tu peux essayer de quitter l'unité en prenant 3  chemains différents, mais attention, ce ne sera pas si simple, des épreuves t'y attendent...tapez: \n \"1\" - pour aller a gauche(Enigma), \n \"2\" - pour aller en avant(Combat) \n \"3\" - pour aller a droite (labyrinte) \n Votre choix : "))


    if beginChoice==1:
        Enigma()
    elif beginChoice==2:
        input("Hé qu'est ce que tu fais la?! Tu as osé rentrer dans MON couloir! Pour la peine, je vais te contaminer!!!!! \nSi tu arrives a me battre, je te laisserai sortir, sinon tu seras piégé, comme moi et la vieille folle d'a coté aura de la compagnie et arrêtera enfin de me poser la même énigme du matin au soir!\"\nHAUT PARLEUR: Combat dans le couloir de sortie!!!!:\nLes règles sont les suivantes:\n-Tu as 1 seringue chargé de vaccin pour guérrire ton attaqunt. (tape 2) \nSi tu le touches 2 fois, il sera guérrit et te laissera partir! \n-Pour te protégé de ses attaques, tu dois mettre ton bras devant tes voix respiratoires (tape 1) \n- Tu peux également recharger ta seringue (tape 3) \n Tape \"go\" pour commencer: ")

        _beginTime = time.time()
        # th1 = threading.Thread(target = Combat(_timer, _beginTime))
        # th2 = threading.Thread(target = TimerSound(_timer, _beginTime))

        # timer = th2.start()
        # timer = th1.start()
        timer = Combat(_timer, _beginTime)
        
    elif beginChoice==3:
        labyrintheSize = 5
        Labyrinthe(labyrintheSize)
    else:
        print("Vous n'avez pas le courage de combattre le virus")
        print("Vous etes une poule mouillé ")

# PARTIE EXECUTION DU PROGRAMME
restartGame = "y"
while restartGame == "y" or restartGame == "Y" : 
    timer = 90
    timer = Hopython(timer)
    restartGame = input("Désirez vous recommencer la partie ? pressez \"y\" pour oui : ")

print(" GoodBye....")

