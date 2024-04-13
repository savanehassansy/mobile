# fonction Python qui prend une chaîne et renvoie un dictionnaire contenant le nombre de chaque caractère de la chaîne.

def compteur_caractere():
    compteur = {}
    chaine = input("entrez une chaine :")
    for element in chaine:
        if element in compteur:
            compteur[element] += 1
        else:
            compteur[element] = 1
    print(compteur)
    return compteur

compteur_caractere()