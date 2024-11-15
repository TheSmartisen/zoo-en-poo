class Cage:
    def __init__(self):
        self.animaux = []

    def ajouterUnAnimaux(self, animal):
        # Ajout d'une copie unique de l'animal dans la cage
        self.animaux.append(animal)
        print(f"Animal ajouté: {animal.name}, dans la cage {id(self)}")

    def __str__(self):
        if not self.animaux:
            return "Cette cage est vide."
        return "\n".join([str(animal) for animal in self.animaux])