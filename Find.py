ListeMotsAVerifier = ["bonjour", "salut", "yo", "coucou"]
phrase = "coucou flute baltringue"
isMotDansLaPhrase = False
for mot in ListeMotsAVerifier :
    if mot in phrase :
        isMotDansLaPhrase = True
if isMotDansLaPhrase :
    print("trouvé!!")
else:
    print("Heu...non")
