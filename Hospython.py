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
from timer import * 
from timerSound import *

def Hopython():
    beginChoice = int(input("AH-AH DOMMAGE POUR TOI! Tu es coincé dans l'unité infecté par le virus Covid, ta mission, si tu l'acceptes (sinon tape \"5\" pour quitter le jeu), est de sorir vivant de l'unité Covid en X minutes.Tu peux essayer de quitter l'unité en prenant 3  chemains différents, mais attention, ce ne sera pas si simple, des épreuves t'y attendent...tapez: \n \"1\" - pour aller a gauche(Enigma), \n \"2\" - pour aller en avant(Combat) \n \"3\" - pour aller a droite (labyrinte) \n Votre choix : "))
    if beginChoice==1:
        Enigma()
    elif beginChoice==2:
        Combat()
    elif beginChoice==3:
        labyrintheSize = 5
        Labyrinthe(labyrintheSize)
    else:
        print("Vous n'avez pas le courage de combattre le virus")
        print("Vous etes une poule mouillé ")

# PARTIE EXECUTION DU PROGRAMME


timer = 90
beginTime = time.time()

Hopython()

input("")

