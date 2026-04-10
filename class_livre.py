class Livre:
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages

    def lire(self):
        print(f"Je lis : {self.titre} de {self.auteur}")

    def __str__(self):
        return f"Livre : {self.titre} - {self.auteur} ({self.pages} pages)"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.titre == other.titre and self.auteur == other.auteur


l1 = Livre("1984", "Orwell", 328)
l2 = Livre("1984", "Orwell", 400)

l1.lire()
l2.lire()

print(l1)
print(len(l1))
print(l1 == l2)