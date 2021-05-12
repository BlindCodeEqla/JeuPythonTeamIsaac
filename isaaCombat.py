from random import *

input("Hé qu'est ce que tu fais la?! Tu as osé rentrer dans MON couloir! Pour la peine, je vais te contaminer!!!!! \nSi tu arrives a me battre, je te laisserai sortir, sinon tu seras piégé, comme moi et la vieille folle d'a coté aura de la compagnie et arrêtera enfin de me poser la même énigme du matin au soir!\"\nHAUT PARLEUR: Combat dans le couloir de sortie!!!!:\nLes règles sont les suivantes:\n-Tu as 1 seringue chargé de vaccin pour guérrire ton attaqunt. (tape 2) \nSi tu le touches 2 fois, il sera guérrit et te laissera partir! \n-Pour te protégé de ses attaques, tu dois mettre ton bras devant tes voix respiratoires (tape 1) \n- Tu peux également recharger ta seringue (tape 3) \n Tape \"go\" pour commencer: ")

playerRecharge= True 
beginPV = 4
monsterPv = 2
monsterRecharge = True
timeRemain = 90


while beginPV != 0 and monsterPv !=0 and timeRemain != 0 : 
    playerChoice = input("Que choisis tu maintenant? ")
    if playerChoice == 1: 
        if monsterRecharge : 
            monsterChoice = randint(1, 2)
        else: 
            monsterChoice = randint(1,3)
        print(monsterChoice)
        if monsterChoice == 1: 
            print("Vous avez tous les deux choisis de vous protéger..")
        elif monsterChoice == 2 : 
            print("il a essayé de t'attaquer, mais tu t'es protégé... ")
            monsterRecharge = False
        else: 
            print("il ne s'est rien passé car tu te protegeais pendant qu'il se raclait la gorge")
    elif playerChoice == 3:
        monsterRecharge = True
        if monsterRecharge : 
            monsterChoice = randint(1, 2)
        else: 
            monsterChoice = randint(1,3)
        if monsterchoice == 1: 
            print("ta seringue est chargée et tu ne t'es pas fait attaqué car il a reculé...")
        elif(monsterchoice==2): 
            print("mince tu t'es fait cracher dessus pendant que tu rechargeais ta seringue... ")
            beginPV -=1
            print("il vous reste " + str(beginPV) + " points de vie. ")
            monsterRecharge = False
        else: 
            print("vous rechargé tous les deux vos armes de destruction massive ....")


    elif playerChoice == 2:
        if playerRecharge: 
            monsterRecharge = True
            if monsterRecharge : 
                monsterchoice = randint(1, 2)
            else: 
                monsterChoice = randint(1,3)
            if monsterchoice == 1: 
                print("ta seringue est chargée et tu ne t'es pas fait attaqué car il a reculé...")
            elif(monsterchoice==2): 
                print("tu as manqué ton coup car l'infecté a reculé...")
                beginPV -=1
                print("vous vous êtes touché tous les deux  ")
                beginPV -=1
                monsterPV -=1
                print("il vous reste " + str(beginPV) + "points de vie et il reste" + str(monsterPV) + " points de vie à l'infecté " )
            else: 
                print("bravo tu l'as vacciné pendant qu'il se préparait à t'attaquer ....")
                monsterPv -=1
        playerRecharge = False


