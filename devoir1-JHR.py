### BONJOUR ÉLIANE, ICI JEAN-HUGUES ROY
### TOUS MES COMMENTAIRES SERONT EN MAJUSCULES ET PRÉCÉDÉS DE 3 # (HASHTAG

# coding: utf-8

### TU Y ES PRESQUE!

url = "https://montrealcampus.ca?p=" ### EXCELLENT DÉPART, ICI :)

print(url[url.rfind("=")+1:]) ### ÇA IMPRIME DU VIDE :)

liste = list(range(20000,30151)) ### PARFAIT!

### IL NE MANQUAIT QUE DE CRÉER UNE LISTE POUR CONTENIR TOUTES LES URLS QUE TA BOUCLE CI-DESSOUS VA GÉNÉRER. DONNONS-LUI UN NOM PERTINENT:

maSupercalifragilistiqueListe = []

n = 0
# for num in range(20000,30151): ### ICI, IL EST INUTILE DE REFAIRE UN "RANGE"
for num in liste: ### UTILISONS PLUTÔT LA VARIABLE "liste" QUE TU AS CRÉÉE CI-DESSUS.
    num1=str(num)
    url1=url+num1
    n += 1
    print(n, url1)

    ### EXCELLENT!
    ### IL NE MANQUE QUE DE METTRE CHAQUE "url1" DANS NOTRE SUPER LISTE

    maSupercalifragilistiqueListe.append(url1)
    
# print(len(liste)) ### ICI, ON CONNAÎT LA LONGUEUR DE CETTE LISTE PUISQUE TU L'AS CRÉÉE AVEC UN "RANGE"...

### AFFICHONS PLUTÔT, UNE FOIS QUE LA BOUCLE AURA FAIT SON TRAVAIL, LE CONTENU DE NOTRE SUPER LISTE, ET SA LONGUEUR:

print(maSupercalifragilistiqueListe, len(maSupercalifragilistiqueListe))

# liste = list 
# print(liste)

### ET VOILÀ :)
### IL MANQUAIT, PAR AILLEURS, DES COMMENTAIRES DANS TON CODE POUR QUE TU M'EXPLIQUES CE QUE TU SOUHAITAIS FAIRE.