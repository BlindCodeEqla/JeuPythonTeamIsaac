# Tableau de données
tableau = [0,5,10,15,20,25]
for valeur in tableau: # Tableau peut être remplacé par range(0,30,5)
    print(valeur)

tableau = [1,3,5,7,11,13,17,19,23] # Pas de range pour les nombre premiers!
for valeur in tableau:
    print(valeur)

# Opération sur un tableau  
tableau = [1,3,5,7,11,13,17,19,23]
print("Taille du tableau:" + str(len(tableau)) )

tableau = [0,5,5,10,10,10,15,20]
print( tableau.count(5) ) # Compte le nombre de "5" (on peut faire reverse, remove, clear, append = ajout d'élément, ...)
print( tableau.count(10) ) # Compte le nombre de "10"

tableau.append("suite")
print(tableau)

tableau.append("\"suite\"")
print(tableau)

# Concatainer des listes
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l1.extend(l2)
print( l1 )

# Dupliquer une liste == l1 et l2 seront la même chose (on modifie l1 et l2 en même temps)
l1 = [1,2,3]
l2 = l1
l1.extend([4,5,6])
print(l1)
print(l2)

# Copier une liste == l1 et l2 sont différentes
l1 = [1,2,3]
l2 = l1[:]
l1.extend([4,5,6])
print(l1)
print(l2)

#Transformer​ une chaine en liste == " " est le séprateur!
chaine = "1 2 3 4 5"
tableau=chaine.split(" ")
print( tableau ) 

# Lister une partie d'un tableau
tableau = [0,1,2,3,4,5]
print(tableau[-2])
print(tableau[1:3])


tableau = ["Bonjour", "salut", "aurevoir"]
tab = ["heilo", "yes", "no"]
tab = tableau[: 1]

print(tab)