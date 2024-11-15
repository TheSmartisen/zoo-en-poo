class Animal:
    def __init__(self, name, espece = "Inconnu"):
        self.name = name
        self.espece = espece
    
    def __str__(self):
        return f"Nom : {self.name} ; Espèce : {self.espece}"

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

class Gazelle(Animal):
    def __init__(self, name):
        super().__init__(name, "Gazelle")

class Hyene(Animal):
    def __init__(self, name):
        super().__init__(name, "Hyène")

class Serpent(Animal):
    def __init__(self, name):
        super().__init__(name, "Serpent")