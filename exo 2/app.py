# Liste C contenant des dictionnaires pour  comptes bancaires slides 26 , 31 , 32  
C = [
    {"nom": "compte1", "solde": 1500},
    {"nom": "compte2", "solde": 800},
    {"nom": "compte3", "solde": 3000},
    {"nom": "compte4", "solde": 500}
]
# Fonction deposer pour validation du montant et modification du dictionnaire slides 31 , 35 , 40
def deposer(c: dict, somme: float):
    if somme > 0:
        c["solde"] = c["solde"] + somme
    return {"compte": c["nom"], "solde": c["solde"]}
# Fonction retirer pour validation du montant et du solde slides 35 , 40
def retirer(c: dict, somme: float):
    if somme > 0 and somme <= c["solde"]:
        c["solde"] = c["solde"] - somme
    return {"compte": c["nom"], "solde": c["solde"]}
# Fonction afficher la boucle sur les comptes et calcul du total slides 38 , 40
def afficher(c: list):
    total = 0
    for compte in c:
        total = total + compte["solde"]
    print(total)
    return {"total": total}
# Fonction filtre1000 retourne les comptes dont le solde est supérieur ou égal à 1000 slides 35 , 38 , 40 
def filtre1000(c: list):
    resultat = []
    for compte in c:
        if compte["solde"] >= 1000:
            resultat.append({"compte": compte["nom"], "solde": compte["solde"]})
    return resultat
# Tri des comptes par solde décroissant slide 42 c'est  sorted et lambda
def trier(c: list):
    resultat = sorted(c, key=lambda compte: compte["solde"], reverse=True)
    return resultat
# Appels des fonctions
print(deposer(C[0], 500))
print(retirer(C[1], 200))
print(afficher(C))
print(filtre1000(C))
print(trier(C))