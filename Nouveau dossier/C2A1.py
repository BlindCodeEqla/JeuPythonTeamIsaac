# On peut voir le "while" comme un "if". Sauf qu'à la différence du if, le code se trouvant dans un while
# est executé en boucle le temps que l'expression booléenne passe à false. On a donc un code comme ceci
# while (condition):
#	CodeSExecutantEnBoucle()
# Le problème de ce code, c'est qu'il n'y a rien qui permet de modifier la condition pour avoir la possibilité
# une fois qu'elle passe à false, ce qui fait donc une boucle infinie. Et notre programme va donc planter !
# Il faut donc agir au sein du while sur la condition pour qu'elle se modifie et passe après un certain nombre
# de cycle à false. Un while ressemble donc souvent à ceci
# while(condition):
# 	CodeSExecutantEnBoucle()
# 	ModificationDeLaCondition()
# Voilà pour la théorie, en sachant ça, essayez d'écrire un bout de code qui va écrire 5 fois Hello World.
# Ensuite, posez vous la question de comment vous devriez modifier ce code si vous vouliez écrire 5000 fois Hello World
# Si vous avez réussi, une seule ligne devrait être à modifier !

i=0
while(i<5):
	print("Hello World")
	i=i+1