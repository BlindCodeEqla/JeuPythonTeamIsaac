from random import *


def Combat():
    input("Hé qu'est ce que tu fais la?! Tu as osé rentrer dans MON couloir! Pour la peine, je vais te contaminer!!!!! \nSi tu arrives a me battre, je te laisserai sortir, sinon tu seras piégé, comme moi et la vieille folle d'a coté aura de la compagnie et arrêtera enfin de me poser la même énigme du matin au soir!\"\nHAUT PARLEUR: Combat dans le couloir de sortie!!!!:\nLes règles sont les suivantes:\n-Tu as 1 seringue chargé de vaccin pour guérrire ton attaqunt. (tape 2) \nSi tu le touches 2 fois, il sera guérrit et te laissera partir! \n-Pour te protégé de ses attaques, tu dois mettre ton bras devant tes voix respiratoires (tape 1) \n- Tu peux également recharger ta seringue (tape 3) \n Tape \"go\" pour commencer: ")

    playerRecharge= True 
    beginPv = 4
    monsterPv = 2
    monsterRecharge = True
    timeRemain = 90


    while beginPv != 0 and monsterPv !=0 and timeRemain != 0 : 
        playerChoice = int(input("Que choisis tu maintenant? "))
        if monsterRecharge : 
            monsterChoice = randint(1, 2)
        else: 
            monsterChoice = randint(1,3)

        if playerChoice == 1: 
            if monsterChoice == 1: 
                print("Vous avez tous les deux choisis de vous protéger..")
            elif monsterChoice == 2 : 
                print("il a essayé de t'attaquer, mais tu t'es protégé... ")
                monsterRecharge = False
            else: 
                print("il ne sest rien passé car tu te protegeais pendant qu'il se raclait la gorge")
                monsterRecharge = True
        elif playerChoice == 3:
            if monsterChoice == 1: 
                print("ta seringue est chargée et tu ne t'es pas fait attaquer car il a reculé...")
            elif(monsterChoice==2): 
                print("mince tu t'es fait cracher dessus pendant que tu rechargeais ta seringue... ")
                beginPv -=1
                monsterRecharge = False
            else: 
                monsterRecharge = True
                print("vous rechargé tous les deux vos armes de destruction massive ....")
        elif playerChoice == 2:
            if playerRecharge: 
                playerRecharge= False
                if monsterChoice == 1: 
                    print("tu as manqué ton coup car l'infecté a reculé...")
                elif(monsterChoice==2): 
                    print("vous vous êtes touché tous les deux...")
                    beginPv -=1
                    monsterPv -=1
                    monsterChoice = False
                else: 
                    print("bravo tu l'as vacciné pendant qu'il se préparait à t'attaquer ....")
                    monsterPv -=1
                    monsterRecharge = True 
            else:
                if monsterChoice == 1: 
                    print("oupssss ta seringue est vide et l'infecté a reculé...")
                elif(monsterChoice==2): 
                    print("tu tentes de vacciner avec une seringue vide et tu as été touché par l'infecté")
                    beginPv -=1
                    monsterRecharge= False
                else: 
                    print("si ta séringue était chargé, tu aurais pu le vacciner pendant qu'il se préparait à t'attaquer ....")
                    monsterRecharge = True
        Result(beginPv, monsterPv)



def Result(_beginPv, _monsterPv):
    print("il vous reste " + str(_beginPv) + " points de vie et il reste " + str(_monsterPv) + " points de vie à l'infecté " )
    if(_beginPv == 0 ):
        print(" Tu as été en contacte trop longtemps avec quelqu'un d'infecté.. tu vas donc sortir de l'hopital, les pieds devant! ") 
    elif(_monsterPv == 0):
        print("Victoire: Bravo!! Tu as guérris l'infecté, il va te montrer la sortie... \n Bon retour à la vie normale, n'oublie quand même pas les gestes barrières pour ne pas revenir ici!!")




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


def Hopython():
    beginChoice = int(input("AH-AH DOMMAGE POUR TOI! Tu es coincé dans l'unité infecté par le virus Covid, ta mission, si tu l'acceptes (sinon tape \"5\" pour quitter le jeu), est de sorir vivant de l'unité Covid en X minutes.Tu peux essayer de quitter l'unité en prenant 3  chemains différents, mais attention, ce ne sera pas si simple, des épreuves t'y attendent...tapez: \n \"1\" - pour aller a gauche(Enigma), \n \"2\" - pour aller en avant(Combat) \n \"3\" - pour aller a droite (labyrinte) \n Votre choix : "))
    if beginChoice==1:
        Enigma()
    elif beginChoice==2:
        Combat()
    elif beginChoice==3:
        print("")
    else:
        print("Vous n'avez pas le courage de combattre le virus")
        print("Vous etes une poule mouillé ")


# PARTIE EXECUTION DU PROGRAMME



beginTime = 90 
beginPV= 4

Hopython()

input("")

