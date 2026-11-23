# Liste students contenant des tuples slides 26 et 28
students = [
    (1000, "JOHN", "DOE", 14, 5),
    (2000, "BOB", "CARLTON", 7, 1),
    (3000, "RAYANE", "SMITH", 13, 3)
]
# Fonction B pour le calcule de la moyenne des 2 notes et retourner un booléen slide 40
# Condition if,else slide 35
def B(note1: float, note2: float) -> bool:
    moyenne = (note1 + note2) / 2
    if moyenne >= 10:
        return True
    else:
        return False
# Fonction A pour  parcourir la liste et appelle B et construir le résultat slides 26 , 33 , 38 , 40
def A(students: list):
    resultat = []
    for etudiant in students:
        if B(etudiant[3], etudiant[4]):
            resultat.append({"mat": etudiant[0], "result": "ADMIS"})
        else:
            resultat.append({"mat": etudiant[0], "result": "AJOURNE"})
    return resultat
# Fonction C pour appeller A et afficher les résultats slide 40
def C(students: list):
    resultat = A(students)
    for etudiant in resultat:
        print(etudiant["mat"], ":", etudiant["result"])
# Appel de la fonction C
C(students)

