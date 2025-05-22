import os
from gtts import gTTS #import du module permettant de generer la voix

os.environ['http_proxy'] = 'http://55.225.55.6:3128'
os.environ['https_proxy'] = 'http://55.225.55.6:3128'
# Répertoire à ajouter
repertoire_binaires = r"C:\temp\CourTony1\bin"

# Ajout au PATH pour ce script seulement
os.environ["PATH"] = repertoire_binaires + os.pathsep + os.environ["PATH"]

# Le but etant de faire un programme qui lit a voix haute le texte entré au clavier
# MAIS si dans le texte on detecte les mmots "bonjour", "salut", yo" et "bonsoir" le programme doit repondre
# "Bonjour egalement"


# code de la fonction pour generer la voix:
def lire_voix(phrase):
    tts = gTTS(text=phrase, lang='fr') # on passe la variable "phrase" au generateur de voix
    tts.save("voix.mp3") # on enregistre le resultat sur le disque dur sous le nom "voix.mp3"
    os.system("ffplay -nodisp -autoexit voix.mp3") # on lit le fichier "voix.mp3" avec l'utilitaire afplay


# la boucle "while True" permet de relancer l'input une fois que la lecture de la voix est faite
# tout le code en dessous du while est pris dans la boucle à partir du moment où il y a une tabulation !!
# donc ici tout le code est re-executer tout le temps jusqu'à ce que tu coupes le programme
#
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

