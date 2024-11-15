from src import Zoo, Cage, Animal, Lion, Gazelle, Hyene, Serpent

# Création d'une instance du Zoo avec un nom par défaut
zoo = Zoo("inconnu")

# Fonction principale qui exécute la gestion du zoo
def main():
    # Demande à l'utilisateur d'entrer un nom pour le zoo
    zoo.name = input("Tout commence à partir d'un nom.\nVeuillez rentrer le nom de votre zoo : ")
    is_continu = True  # Variable pour maintenir la boucle principale active
    while is_continu:
        # Menu principal pour la gestion du zoo
        choix_zoo = gestionDuZoo()
        is_cages = False  # Indique si l'utilisateur veut gérer les cages
        choix_cages = None
        match choix_zoo:
            case "1":  # Affiche les informations du zoo
                afficherLeZoo()
            case "2":  # Passe à la gestion des cages
                is_cages = True
            case "3":  # Affiche le nombre de cages dans le zoo
                print(zoo.displayNbCages())
            case "4":  # Quitte la gestion du zoo
                is_continu = False
        
        # Gestion des cages si sélectionné
        if is_cages:
            choix_cages = None
            while choix_cages != "4":  # Retourne au menu principal si "4"
                choix_cages = gestionDesCages()
                is_cage = False  # Indique si une cage spécifique est sélectionnée
                index_cage = None
                match choix_cages:
                    case "1":  # Affiche toutes les cages
                        afficherLesCages()
                    case "2":  # Sélectionne une cage à gérer
                        is_cage = True
                        index_cage = input("Choisir une cage : ")
                    case "3":  # Ajoute une nouvelle cage au zoo
                        zoo.cages.append(Cage())
                        print(f"La cage n° {len(zoo.cages) - 1} vient d'être crée")
                
                # Gestion d'une cage spécifique
                if is_cage:
                    choix_cage = None
                    while choix_cage != "3" and choix_cage != "4":  # Retour au menu des cages ou du zoo si "3" ou "4"
                        choix_cage = gestionDuneCage(index_cage)
                        is_animal = False  # Indique si l'utilisateur souhaite ajouter un animal
                        if choix_cage:
                            match choix_cage:
                                case "1":  # Affiche les informations de la cage
                                    afficherLaCage(index_cage, zoo.cages[int(index_cage)])
                                case "2":  # Passe à l'ajout d'un animal
                                    is_animal = True
                                case "4":  # Retour au menu des cages
                                    choix_cages = "4"

                        # Ajout d'un animal à la cage
                        if is_animal:
                            choix_animal = gestionAnimal()
                            animal = None  # Variable pour l'instance de l'animal
                            choix_name = ""
                            while choix_name == "":  # Demande un nom pour l'animal
                                choix_name = input("Veuillez entrer un nom : ")

                            # Crée une instance d'animal en fonction du choix
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
                                    while choix_espece == "":  # Demande une espèce pour un animal générique
                                        choix_espece = input("Veuillez entrer une espece : ")
                                    animal.espece = choix_espece

                            # Ajoute l'animal à la cage sélectionnée
                            zoo.cages[int(index_cage)].ajouterUnAnimaux(animal)
                            print(f"L'animal {choix_name} a été ajouté à la cage numéro {index_cage}")

# Menu pour gérer le zoo
def gestionDuZoo():
    print(f"Gestion du zoo {zoo.name} : ")
    print("1. Visiter le zoo")
    print("2. Gestion des cages")
    print("3. Afficher le nombre de cages")
    print("4. Partir du zoo !")
    return input("Entrez un choix : ")

# Menu pour gérer les cages
def gestionDesCages():
    print("Gestion des cages : ")
    print("1. Visiter les cages")
    print("2. Visiter une cage")
    print("3. Ajouter une cage")
    print("4. Retourner dans la gestion du zoo")
    
    return input("Entrez un choix : ")

# Menu pour gérer une cage spécifique
def gestionDuneCage(index):
    try:
        index = int(index)
        if index < 0 or index >= len(zoo.cages):  # Vérifie si l'index est valide
            raise IndexError("Index hors limite")
        cage = zoo.cages[index]
        print(f"Gestion de la cage n° {index} :")
        print("1. Vérifier les animaux")
        print("2. Ajouter un animal")
        print("3. Retourner dans la gestion des cages")
        print("4. Retourner dans la gestion du zoo")
        return input("Entrez un choix : ") 
    except (ValueError, IndexError):  # Gère les erreurs si l'index est invalide
        print(f"Le cage n° {index} n'existe pas")
        return "3"

# Menu pour ajouter un animal
def gestionAnimal():
    print("Quels animal souhaitez-vous ajouter?")
    print("1. Lion")
    print("2. Gazelle")
    print("3. Hyene")
    print("4. Serpent")
    print("5. Autre")
    return input("Entrez un choix : ") 

# Fonction pour personnaliser le nom d'un animal
def personnalisationAnimal():
    choix_name = ""
    while choix_name == "":
        choix_name = input("Veuillez entrer un nom : ")
    return choix_name

# Fonction pour personnaliser l'espèce d'un animal
def personnalisationEspece():
    choix_espece = ""
    while choix_espece == "":
        choix_espece = input("Veuillez entrer une espece : ")
    return choix_espece

# Affiche les informations générales du zoo
def afficherLeZoo():
    print(f"Voici le zoo {zoo.name}")
    afficherLesCages()

# Affiche les informations de toutes les cages
def afficherLesCages():
    if len(zoo.cages) == 0:  # Vérifie si des cages existent
        print("Il n'y a rien dans le zoo ! Veuillez circuler")
    else:
        for index, cage in enumerate(zoo.cages):
            afficherLaCage(index, cage)

# Affiche les détails d'une cage spécifique
def afficherLaCage(index, cage):
    print(f"Cage n° {index}:")
    print(cage)

# Exécute le programme si le fichier est lancé directement
if __name__ == "__main__":
    main()
