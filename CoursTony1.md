### les notions importante a retenir :
- La boucle while true et les booléens
- Les listes et la boucle for in
- Saisir au clavier avec input
- Le find sur une chaine
- Le if any
- Les fonctions 

## La boucle «while True» et les booléens:
Pour bien comprendre la boucle while True, il faut déjà comprendre ce qu’est un booléen !  
C’est un mot un peu compliqué… pour pas grand-chose en réalité 😄  
En fait, c’est juste un type de variable qui peut prendre deux valeurs :  
-   La valeur True (vrai)
-   La valeur False (faux)

C’est tout ! Et le mot “while” veut dire “tant que”.  
Donc, quand tu écris while True, tu dis à Python :  
“Exécute ce code tant que la condition est vraie.”  
Or ici, la condition, c’est juste True tout court. Et comme True ne change jamais (c’est une valeur fixe),  
la boucle tourne à l’infini !  

➕ **Important** : le code qui dépend du while doit être indenté (c’est-à-dire écrit avec une tabulation ou 4 espaces devant),  
sinon Python ne saura pas quoi répéter.  

🎯 On appelle ça une boucle infinie parce qu’elle ne s’arrête jamais… sauf si tu rajoutes un break ou que tu coupes  
le programme manuellement.

Par exemple si tu execute ca :
``` python
while True:
    print ("coucou")
    print ("baltringue")
print ("flute qui fais saigner des oreilles")
```
>***Tu peux executer le programme BoucleWhileTrue.py pour tester***

le programme va se lancer et afficher une suite de "coucou baltringue" sans s'arreter et surtout sans JAMAIS passer  
par "print ("flute qui fais saigner des oreilles")" au passage c'est plutot une bonne chose 😂
``` python
coucou
baltringue
coucou
baltringue
coucou
baltringue
coucou
baltringue
...
```
Mais c'est surtout pour souligner l'importante de l'indentation !!  
Dans le programme InputTony.py on a utilisé la boucle "while true" en ligne 8 pour re-demander de rentrer une phrase  
une fois la précédente jouée !

## Les listes et les boucles "for in"
On a utilisé une liste en python pour stocker la liste de mots a verifier dans la phrase que l'on entre au clavier :  
bonjour, salut, yo et bonsoir  
en python ça donne :  
```python
ListeMotsAVerifier = ["bonjour","salut","yo","bonsoir"]
```
Une boucle "for in" te permet de faire un print (ou n'importe quoi) sur chaque mot de ListeMotsAVerifier :
``` python
ListeMotsAVerifier = ["bonjour", "salut", "yo", "bonsoir"]
for motAVerifier in ListeMotsAVerifier:
    print(motAVerifier)
```
>***Tu peux executer le programme Listes.py pour tester***

➕ **Important** : le code qui dépend du for doit être indenté (c’est-à-dire écrit avec une tabulation ou 4 espaces devant),  
sinon Python ne saura pas quoi répéter.  

## Saisir au clavier avec input
Bon ça tu le savais deja :) mais note juste comment on stocke la valeur :  
ici ça stocke la phrase que tu rentres au clavier dans la variable "phrase"
``` python
phrase = input("saisir ta phrase: ")
```
## Le find sur une chaine
au debut on a utiliser la methode find() pour trouver si un mot était contenu dans la variable phrase:
``` python
phrase = input("saisir ta phrase: ")
etat = phrase.find("bonjour")
```
Et find() renvoie -1 s'il ne trouve rien ! par contre s'il trouve le mot "bonjour" il renvoi la position du mot dans  
la phrase.  
par exemple :
``` python
phrase = "coucou bonjour baltringue"
etat = phrase.find("bonjour")
print (etat)
```
Donne :
``` python
8
```
Et par contre:
``` python
phrase = "coucou flute baltringue"
etat = phrase.find("bonjour")
print (etat)
```
Donne :
``` python
-1
```
Bon c'est une facon de faire mais c'est pas tres pratique a utiliser 😁 et surtout quand tu commences a avoir plusieurs  
mots a verifier ! il y a une facon bien plus élégante en utilisant un "if in" ou un "if any"

##  Le "if in" et "if any"

bon comme je t'ai dis precedement, il y a un facon plus élégante de chercher dans ta phrase.
Pour cela tu peux utiliser le "if in", c’est une façon très simple de vérifier si quelque chose est contenu dans une liste, une chaîne de caractères, etc.

``` python
ListeMotsAVerifier = ["bonjour", "salut", "yo", "coucou"]
phrase = "coucou flute baltringue"
for mot in ListeMotsAVerifier :
    if mot in phrase :
        print("trouvé!!")
```
ca donne :
``` python
trouvé!!
```
>***Tu peux executer le programme Find.py pour tester***

Le truc important la-dedans c'est la condition "if in" :
le code "if mot in phrase" permet de savoir si la valeur de "mot" et contenu dans la valeur "phrase" directement  
sans faire de find()
Mais tu peux aussi le faire plus court comme ca en utilisant le "if any":
C'est une fonction très pratique : elle regarde une liste de conditions, et retourne True si au moins une est vraie.

``` python
ListeMotsAVerifier = ["bonjour", "salut", "yo", "coucou"]
phrase = "coucou flute baltringue"
if any (mot in phrase for mot in ListeMotsAVerifier) :
   print("trouvé!!")
```
si on traduit ce bout de code :  
"if any (mot in phrase for mot in ListeMotsAVerifier) :"  
si un mot contenue dans ListeLotsAVerifier est present dans "phrase" alors la condition est vrai  
MAIS je trouve que la condition est un peu moins claire, donc pour des raisons pedagogique on conservera la premiere :)


## les fonctions
Si tu regardes bien le code qui génère la voix, tu verras qu’il est toujours le même : il ne change jamais, sauf pour la phrase à dire.  
Dans ce genre de situation, on ne copie-colle pas le même code à chaque fois : on crée une fonction !  
On va donc écrire une fonction qui prendra un paramètre (la phrase), et son rôle sera de jouer la phrase avec la voix.
Comme ça, dès qu’on veut dire quelque chose, il suffit d’appeler la fonction avec la phrase qu’on veut, et le tour est joué !  
on part du code d'origine:
``` python
while True :
    # construit la liste de mots a verifier dans la phrase
    # c'est une liste Python permettant de stocker plusieurs valeurs
    ListeMotsAVerifier = ["bonjour","salut","yo","bonsoir"]

    # permet de demander a un utilisateur de saisir un texte au clavier et de le stocker dans la variable "phrase"
    phrase = input("saisir ta phrase: ")

    # Permet de chercher si un mot contenu dans ListeMotsAVerifier est present dans la phrase
    for mot in ListeMotsAVerifier:
        if mot in phrase:
            phrase = "Bonjour egalement"

    #if any (mot in phrase for mot in ListeMotsAVerifier) :
    #   phrase = "Bonjour egalement"

    # code pour generer la voix:
    tts = gTTS(text=phrase, lang='fr') # on passe la variable "phrase" au generateur de voix
    tts.save("voix.mp3") # on enregistre le resultat sur le disque dur sous le nom "voix.mp3"
    os.system("afplay voix.mp3") # on lit le fichier "voix.mp3" avec l'utilitaire afplay
```
et on sort dans une fonction "lire_voix" le code pour generer la voix :
``` python
# code pour generer la voix:
def lire_voix(phrase):
    tts = gTTS(text=phrase, lang='fr') # on passe la variable "phrase" au generateur de voix
    tts.save("voix.mp3") # on enregistre le resultat sur le disque dur sous le nom "voix.mp3"
    os.system("afplay voix.mp3") # on lit le fichier "voix.mp3" avec l'utilitaire afplay
    
while True :
    # construit la liste de mots a verifier dans la phrase
    # c'est une liste Python permettant de stocker plusieurs valeurs
    ListeMotsAVerifier = ["bonjour","salut","yo","bonsoir"]

    # permet de demander a un utilisateur de saisir un texte au clavier et de le stocker dans la variable "phrase"
    phrase = input("saisir ta phrase: ")

    # Permet de chercher si un mot contenu dans ListeMotsAVerifier est present dans la phrase
    for mot in ListeMotsAVerifier:
        if mot in phrase:
            phrase = "Bonjour egalement"

    #if any (mot in phrase for mot in ListeMotsAVerifier) :
    #   phrase = "Bonjour egalement"

    #code pour appeler la fonction qui lit la phrase:
    lire_voix(phrase)
```
C'est beaucoup plus propre comme ca :) apres tu peux utiliser ta fonction lire_voix() partout dans ton code !  
Par contre ta fonction doit etre definie AVANT le code qui l'utilise sinon python ne sera pas quoi faire avec lire_voix :)  



