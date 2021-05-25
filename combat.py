
from timer import * 
from timerSound import *

from math import floor
from random import *
import winsound
from winsound import *
import threading
import time
import sys
import wave
import threading

def Combat(_timer, _beginTime):
    playerRecharge= True 
    beginPv = 4
    monsterPv = 2
    monsterRecharge = True
    

    while beginPv > 0 and monsterPv > 0 and Timer(_timer, _beginTime) > 0 : 
        playerChoice = int(input("Que choisis tu maintenant? "))
        if monsterRecharge : 
            monsterChoice = randint(1, 2)
        else: 
            monsterChoice = randint(1,3)

        if playerChoice == 1: 
            if monsterChoice == 1: 
                PlaySound("bouclier", SND_ASYNC | SND_FILENAME)
                print("Vous avez tous les deux choisis de vous protéger..")
            elif monsterChoice == 2 : 
                PlaySound("bouclier", SND_ASYNC | SND_FILENAME)
                print("il a essayé de t'attaquer, mais tu t'es protégé... ")
                monsterRecharge = False
            else: 
                PlaySound("gorge", SND_ASYNC | SND_FILENAME)
                print("il ne sest rien passé car tu te protegeais pendant qu'il se raclait la gorge")
                monsterRecharge = True
        elif playerChoice == 3:
                playerRecharge = True
                if monsterChoice == 1: 
                    PlaySound("recharge", SND_ASYNC | SND_FILENAME)
                    print("ta seringue est chargée et tu ne t'es pas fait attaquer car il a reculé...")
                elif(monsterChoice==2): 
                    PlaySound("cris", SND_ASYNC | SND_FILENAME)
                    print("mince tu t'es fait cracher dessus pendant que tu rechargeais ta seringue... ")
                    beginPv -=1
                    monsterRecharge = False
                else: 
                    monsterRecharge = True
                    PlaySound("gorge", SND_ASYNC | SND_FILENAME)
                    print("vous rechargé tous les deux vos armes de destruction massive ....")
        elif playerChoice == 2:
            if playerRecharge: 
                playerRecharge= False
                if monsterChoice == 1: 
                    PlaySound("rate", SND_ASYNC | SND_FILENAME)
                    print("tu as manqué ton coup car l'infecté a reculé...")
                elif(monsterChoice==2): 
                    PlaySound("cris", SND_ASYNC | SND_FILENAME)
                    print("vous vous êtes touché tous les deux...")
                    beginPv -=1
                    monsterPv -=1
                    monsterChoice = False
                else: 
                    PlaySound("youpi", SND_ASYNC | SND_FILENAME)
                    print("bravo tu l'as vacciné pendant qu'il se préparait à t'attaquer ....")
                    monsterPv -=1
                    monsterRecharge = True 
            else:
                if monsterChoice == 1: 
                    PlaySound("rate", SND_ASYNC | SND_FILENAME)
                    print("oupssss ta seringue est vide et l'infecté a reculé...")
                elif(monsterChoice==2): 
                    PlaySound("rate", SND_ASYNC | SND_FILENAME)
                    print("tu tentes de vacciner avec une seringue vide et tu as été touché par l'infecté")
                    beginPv -=1
                    monsterRecharge= False
                else: 
                    PlaySound("rate", SND_ASYNC | SND_FILENAME)
                    print("si ta séringue était chargé, tu aurais pu le vacciner pendant qu'il se préparait à t'attaquer ....")
                    monsterRecharge = True
        else:
            print("Veuillez choisir un chiffre comprie entre 1 et 3")
            continue
        Result(beginPv, monsterPv)
        print("Temps restant : ", Timer(_timer, _beginTime), " seconde(s).")
        if(Timer(_timer, _beginTime) <= 0):
            print("Game Over... Vous êtes trop longtemps exposé au virus...")
            return Timer(_timer, _beginTime)
    return Timer(_timer, _beginTime)




def Result(_beginPv, _monsterPv):
    print("il vous reste " + str(_beginPv) + " points de vie et il reste " + str(_monsterPv) + " points de vie à l'infecté " )
    if(_beginPv == 0 ):
        print(" Tu as été en contacte trop longtemps avec quelqu'un d'infecté.. tu vas donc sortir de l'hopital, les pieds devant! ") 
    elif(_monsterPv == 0):
        print("Victoire: Bravo!! Tu as guérris l'infecté, il va te montrer la sortie... \n Bon retour à la vie normale, n'oublie quand même pas les gestes barrières pour ne pas revenir ici!!")

