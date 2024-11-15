# Zoo en POO 🐾

Ce projet a pour but de modéliser un zoo en Python en utilisant les principes de la **Programmation Orientée Objet (POO)**. Il est conçu comme un exercice pédagogique permettant de développer des compétences en conception et implémentation d'objets.

## Fonctionnalités

### 🏛️ Gestion du Zoo
- Créer un zoo contenant plusieurs cages.
- Ajouter des cages au zoo.
- Afficher le nombre de cages présentes dans le zoo à tout moment.

### 🦁 Gestion des Animaux
- Ajouter des animaux dans les cages.
  - Chaque animal appartient à une espèce (ex. : "Lion", "Hyène").
  - Chaque animal a un nom unique attribué par le gardien.
- Lister les animaux présents dans chaque cage.

## Structure des Classes

### 1️⃣ **Classe `Zoo`**
- **Responsabilités :**
  - Stocker les cages.
  - Ajouter des cages au zoo.
  - Compter et afficher le nombre de cages présentes.

### 2️⃣ **Classe `Cage`**
- **Responsabilités :**
  - Représenter une cage contenant plusieurs animaux.
  - Ajouter des animaux dans la cage.
  - Lister les animaux présents dans la cage.

### 3️⃣ **Classe `Animal`**
- **Responsabilités :**
  - Représenter un animal avec les attributs suivants :
    - **Espèce** : Nom de l'espèce de l'animal (ex. : Lion, Hyène).
    - **Nom** : Nom attribué par le gardien.
  - Les sous-classes comme `Lion`, `Gazelle`, `Hyène` ou `Serpent` héritent de la classe `Animal`.

## Arborescence du Projet

```
zoo-en-poo/
├── .gitignore         # Fichiers à ignorer par Git
├── .venv/             # Environnement virtuel Python
├── .vscode/           # Configuration VS Code
├── main.py            # Point d'entrée principal
├── README.md          # Documentation du projet
└── src/               # Code source
    ├── zoo.py         # Définition de la classe Zoo
    ├── cage.py        # Définition de la classe Cage
    └── animal.py      # Définition de la classe Animal et ses sous-classes
```

## Installation et Exécution

### Pré-requis
- Python 3.8 ou supérieur
- [pipenv](https://pypi.org/project/pipenv/) pour gérer les dépendances

### Étapes

1. Clone le projet :
   ```bash
   git clone https://github.com/ton-repo/zoo-en-poo.git
   cd zoo-en-poo
   ```

2. Active l'environnement virtuel :
   ```bash
   pipenv install
   pipenv shell
   ```

3. Lance le script principal :
   ```bash
   python main.py
   ```

## Exemple d'Utilisation

Voici un exemple simple d'utilisation du zoo :

```python
from src.zoo import Zoo
from src.cage import Cage
from src.animal import Lion, Hyene

# Créer un zoo
mon_zoo = Zoo()

# Ajouter une cage
cage1 = Cage()
mon_zoo.ajouter_cage(cage1)

# Ajouter des animaux dans la cage
lion = Lion(nom="Simba")
hyene = Hyene(nom="Shenzi")
cage1.ajouter_animal(lion)
cage1.ajouter_animal(hyene)

# Afficher le contenu de la cage
print(cage1.lister_animaux())
```

## Objectifs Pédagogiques

- Comprendre et appliquer les concepts de la **Programmation Orientée Objet**.
- Structurer un projet Python avec des classes interconnectées.
- Apprendre à utiliser des sous-classes et l'héritage pour modéliser des entités.
