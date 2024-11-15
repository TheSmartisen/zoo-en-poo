class Zoo:
    def __init__(self, name, cages = []):
        self.name = name
        self.cages = cages     

    def displayNbCages(self):
        return f"Il y a actuellement {len(self.cages)} cages dans le zoo"
    