
# une boucle "for in" te permets de faire un print sur chaque mot:
print("-----------------------------------------------------------------")
print("Afficher le contenu de la liste ListeMotsAVerifier :")
ListeMotsAVerifier = ["bonjour", "salut", "yo", "bonsoir"]
for motAVerifier in ListeMotsAVerifier:
    print(motAVerifier)

# Tu peux ajouter une nouvelle valeur:
print("-----------------------------------------------------------------")
print("Ajout de la valeur flute :")
ListeMotsAVerifier.append("flute")
for motAVerifier in ListeMotsAVerifier:
    print(motAVerifier)

# ou la supprimert :
print("-----------------------------------------------------------------")
print("Suppresion de la valeur flute :")
ListeMotsAVerifier.remove("flute")
for motAVerifier in ListeMotsAVerifier:
    print(motAVerifier)


