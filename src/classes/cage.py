class Cage:
    def __init__(self, animaux = []):
        self.animaux = animaux

    def ajouterUnAnimaux(self, animal):
        self.animaux.append(animal)

    def __str__(self):
        return "\n".join([str(animal) for animal in self.animaux])