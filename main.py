from src import Zoo, Cage, Animal, Lion, Gazelle, Hyene, Serpent

zoo = Zoo("inconnu")

def main():
    zoo.name = input("Tout commence à partir d'un nom.\nVeuillez rentrer le nom de votre zoo : ")
    is_continu = True 
    while is_continu:
        choix_zoo = gestionDuZoo()
        is_cages = False
        choix_cages = None
        match choix_zoo:
            case "1":
                afficherLeZoo()
            case "2":
                is_cages = True
            case "3":
                print(zoo.displayNbCages())
            case "4":
                is_continu = False
        
        if is_cages:
            choix_cages = None
            while choix_cages != "4":
                choix_cages = gestionDesCages()
                is_cage = False
                index_cage = None
                match choix_cages:
                    case "1":
                        afficherLesCages()
                    case "2":
                        is_cage = True
                        index_cage = input("Choisir une cage : ")
                    case "3":
                        zoo.cages.append(Cage())
                        print(f"La cage n° {len(zoo.cages) - 1} vient d'être crée")
                
                if is_cage:
                    choix_cage = None
                    while choix_cage != "3" and choix_cage != "4":
                        choix_cage = gestionDuneCage(index_cage)
                        is_animal = False
                        if choix_cage:
                            match choix_cage:
                                case "1":
                                    afficherLaCage(index_cage, zoo.cages[int(index_cage)])
                                case "2":
                                    is_animal = True
                                case "4":
                                    choix_cages = "4"

                        if is_animal:
                            choix_animal = None
                            choix_animal = gestionAnimal()
                            animal = None
                            choix_name = ""
                            while choix_name == "":
                                choix_name = input("Veuillez entrer un nom : ")
                            match choix_animal: 
                                case "1":
                                    animal = Lion(choix_name)
                                case "2":
                                    animal = Gazelle(choix_name)
                                case "3":
                                    animal = Hyene(choix_name)
                                case "4":
                                    animal = Serpent(choix_name)
                                case _:
                                    animal = Animal(choix_name)
                                    choix_espece = ""
                                    while choix_espece == "":
                                        choix_espece = input("Veuillez entrer une espece : ")
                                    animal.espece = choix_espece
                            zoo.cages[int(index_cage)].ajouterUnAnimaux(animal)

                            
def gestionDuZoo():
    print(f"Gestion du zoo {zoo.name} : ")
    print("1. Visiter le zoo")
    print("2. Gestion des cages")
    print("3. Afficher le nombre de cages")
    print("4. Partir du zoo !")
    return input("Entrez un choix : ")

def gestionDesCages():
    print("Gestion des cages : ")
    print("1. Visiter les cages")
    print("2. Visiter une cage")
    print("3. Ajouter une cage")
    print("4. Retourner dans la gestion du zoo")
    
    return input("Entrez un choix : ")

def gestionDuneCage(index):
    try:
        index = int(index)
        if index < 0 or index >= len(zoo.cages):
            raise IndexError("Index hors limite")
        cage = zoo.cages[index]
        print(f"Gestion de la cage n° {index} :")
        print("1. Vérifier les animaux")
        print("2. Ajouter un animal")
        print("3. Retourner dans la gestion des cages")
        print("4. Retourner dans la gestion du zoo")
        return input("Entrez un choix : ") 
    except (ValueError, IndexError):
        print(f"Le cage n° {index} n'existe pas")
        return "3"

def gestionAnimal():
    print("Quels animal souhaitez-vous ajouter?")
    print("1. Lion")
    print("2. Gazelle")
    print("3. Hyene")
    print("4. Serpent")
    print("5. Autre")
    return input("Entrez un choix : ") 

def personnalisationAnimal():
    choix_name = ""
    while choix_name == "":
        choix_name = input("Veuillez entrer un nom : ")
    return choix_name

def personnalisationEspece():
    choix_espece = ""
    while choix_espece == "":
        choix_espece = input("Veuillez entrer une espece : ")
    return choix_espece

def afficherLeZoo():
    print(f"Voici le zoo {zoo.name}")
    afficherLesCages()

def afficherLesCages():
    if len(zoo.cages) == 0:
        print("Il n'y a rien dans le zoo ! Veuillez circuler")
    else:
        for index, cage in enumerate(zoo.cages):
            afficherLaCage(index, cage)
            
def afficherLaCage(index, cage):
    print(f"Cage n° {index}:")
    print(cage)


if __name__ == "__main__":
    main()