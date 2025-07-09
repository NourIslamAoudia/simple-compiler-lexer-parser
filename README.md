# Compilateur Simple - Analyseur Lexical et Syntaxique

Ce projet implémente un compilateur simple avec deux versions distinctes : une version en **C** utilisant Flex/Bison et une version en **Python** utilisant PLY (Python Lex-Yacc). Le compilateur peut analyser des expressions arithmétiques, logiques et des structures de programme avec des sections définies.

## 🚀 Fonctionnalités

### Version C (Flex/Bison)
- **Analyse lexicale** : Reconnaissance des nombres, opérateurs (+, -), espaces
- **Analyse syntaxique** : Évaluation d'expressions arithmétiques simples
- **Gestion d'erreurs** : Détection des caractères invalides
- **Interaction en temps réel** : Entrée utilisateur depuis la console

### Version Python (PLY)
- **Analyse lexicale avancée** : Support des opérateurs arithmétiques, logiques, de comparaison
- **Analyse syntaxique complexe** : Gestion des précédences, expressions parenthésées
- **Analyseur de structure** : Parsing de fichiers avec sections VAR_GLOBAL, DECLARATION, INSTRUCTION
- **Gestion complète d'erreurs** : Exceptions personnalisées et validation

## 📁 Structure du Projet

```
Compiler/
├── C compiler/           # Version C avec Flex/Bison
│   ├── lexer.l          # Définition de l'analyseur lexical
│   ├── parser.y         # Grammaire et analyseur syntaxique
│   ├── main.c           # Point d'entrée du programme
│   ├── lex.yy.c         # Code généré par Flex
│   ├── parser.tab.c     # Code généré par Bison
│   └── parser.tab.h     # Headers générés par Bison
└── compiler.py/          # Version Python avec PLY
    ├── lexer.py         # Analyseur lexical Python
    ├── parser.py        # Analyseur syntaxique Python
    ├── compiler.py      # Programme principal et analyseur de structure
    ├── code.txt         # Fichier d'exemple à analyser
    ├── parser.out       # Fichier de debug PLY
    ├── parsetab.py      # Tables de parsing générées
    └── __pycache__/     # Cache Python compilé
```

## 🛠️ Installation et Configuration

### Prérequis

#### Pour la version C :
```bash
# Windows (avec MinGW/MSYS2)
pacman -S flex bison gcc

# Linux (Ubuntu/Debian)
sudo apt-get install flex bison gcc

# macOS (avec Homebrew)
brew install flex bison gcc
```

#### Pour la version Python :
```bash
pip install ply
```

### Compilation

#### Version C :
```bash
cd "C compiler"
# Générer l'analyseur lexical
flex lexer.l

# Générer l'analyseur syntaxique
bison -d parser.y

# Compiler le programme
gcc -o compiler main.c lex.yy.c parser.tab.c
```

#### Version Python :
Aucune compilation nécessaire, Python est interprété.

## 🎯 Utilisation

### Version C - Calculateur d'expressions

```bash
# Exécuter le programme
./compiler

# Exemple d'utilisation
Entrez une expression :
5 + 3
Nombre: 5
Nombre: 3
Résultat: 8

10 - 7
Nombre: 10
Nombre: 7
Résultat: 3
```

**Expressions supportées :**
- Nombres entiers : `123`, `456`
- Addition : `5 + 3`
- Soustraction : `10 - 4`
- Expressions imbriquées : `2 + 3 - 1`

### Version Python - Analyseur avancé

#### 1. Analyse d'expressions simples
```python
from lexer import get_tokens
from parser import parse_expression

# Expressions arithmétiques
result = parse_expression("(5 + 3) * 2")
print(result)  # 16

# Expressions logiques
result = parse_expression("5 > 3 && 2 < 4")
print(result)  # 1 (True)

# Expressions de comparaison
result = parse_expression("10 == 10")
print(result)  # 1 (True)
```

#### 2. Analyse de fichiers structurés
```python
python compiler.py code.txt
```

**Format du fichier d'entrée (`code.txt`) :**
```
VAR_GLOBAL {
    variable1
    variable2
}
DECLARATION {
    fonction1
    fonction2  
}
INSTRUCTION {
    5 + 3 * 2
    10 > 5
}
```

**Sortie attendue :**
```
Analyse réussie !

Contenu de la section VAR_GLOBAL :
variable1
variable2

Contenu de la section DECLARATION :
fonction1
fonction2

Contenu de la section INSTRUCTION :
5 + 3 * 2
10 > 5

Résultat: 11
```

## 📝 Exemples Détaillés

### Version C - Exemples d'expressions

```bash
# Expression simple
3 + 5
# Sortie:
# Nombre: 3
# Nombre: 5
# Résultat: 8

# Expression avec soustraction
10 - 7 + 2
# Sortie:
# Nombre: 10
# Nombre: 7
# Résultat: 3
# Nombre: 2
# Résultat: 5

# Gestion d'erreur
abc
# Sortie:
# Erreur : caractère invalide
```

### Version Python - Exemples avancés

#### Analyse lexicale
```python
from lexer import get_tokens

# Tokens d'une expression
tokens = get_tokens("(5 + 3) * 2 > 10")
print(tokens)
# [('LPAREN', '('), ('NUMBER', 5), ('PLUS', '+'), ('NUMBER', 3), 
#  ('RPAREN', ')'), ('TIMES', '*'), ('NUMBER', 2), ('GT', '>'), ('NUMBER', 10)]
```

#### Expressions complexes
```python
# Précédence des opérateurs
result = parse_expression("2 + 3 * 4")  # = 14 (pas 20)

# Expressions logiques
result = parse_expression("!(5 > 10) && (3 < 5)")  # = 1 (True)

# Expressions avec parenthèses
result = parse_expression("(2 + 3) * (4 - 1)")  # = 15
```

#### Fichier de test complet
```
VAR_GLOBAL {
    counter
    total
    isValid
}
DECLARATION {
    calculateSum()
    validateInput()
    processData()
}
INSTRUCTION {
    (10 + 5) * 2
    15 > 10 && 5 < 20
    !(3 == 5) || (7 >= 7)
}
```

## 🔧 Fonctionnalités Techniques

### Tokens supportés (Version Python)
| Token | Symbole | Description |
|-------|---------|-------------|
| NUMBER | `123` | Nombres entiers |
| PLUS | `+` | Addition |
| MINUS | `-` | Soustraction |
| TIMES | `*` | Multiplication |
| DIVIDE | `/` | Division |
| LPAREN | `(` | Parenthèse ouvrante |
| RPAREN | `)` | Parenthèse fermante |
| AND | `&&` | ET logique |
| OR | `\|\|` | OU logique |
| NOT | `!` | NON logique |
| LT | `<` | Inférieur |
| LE | `<=` | Inférieur ou égal |
| GT | `>` | Supérieur |
| GE | `>=` | Supérieur ou égal |
| EQ | `==` | Égalité |
| NE | `!=` | Différence |
| COMMENT | `%%` | Commentaires |

### Précédence des opérateurs
1. `!` (NOT) - Priorité la plus haute
2. `*, /` (Multiplication, Division)
3. `+, -` (Addition, Soustraction)
4. `<, <=, >, >=` (Comparaisons)
5. `==, !=` (Égalité, Différence)
6. `&&` (ET logique)
7. `||` (OU logique) - Priorité la plus basse

## 🐛 Gestion d'Erreurs

### Version C
- **Caractères invalides** : Le programme s'arrête avec un message d'erreur
- **Erreurs de syntaxe** : Affichage d'un message d'erreur générique

### Version Python
- **Erreurs lexicales** : Tokens non reconnus ignorés
- **Erreurs syntaxiques** : Messages d'erreur avec position
- **Erreurs de structure** : Validation des sections et accolades
- **Division par zéro** : Gestion spéciale avec message d'erreur

## 🧪 Tests

### Test de la version C
```bash
# Tester avec différentes expressions
echo "5 + 3" | ./compiler
echo "10 - 7" | ./compiler
echo "abc" | ./compiler  # Test d'erreur
```

### Test de la version Python
```python
# Script de test
def test_expressions():
    expressions = [
        "5 + 3",           # = 8
        "10 - 7",          # = 3
        "(2 + 3) * 4",     # = 20
        "5 > 3",           # = 1
        "!(5 == 3)",       # = 1
        "10 / 0"           # Erreur de division
    ]
    
    for expr in expressions:
        result = parse_expression(expr)
        print(f"{expr} = {result}")
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment contribuer :

1. **Fork** le projet
2. Créez une **branche** pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. **Committez** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une **Pull Request**

## 📋 TODO / Améliorations futures

- [ ] Support des variables nommées
- [ ] Ajout des fonctions mathématiques (sin, cos, sqrt, etc.)
- [ ] Interface graphique pour la version Python
- [ ] Génération de code assembleur
- [ ] Support des nombres flottants
- [ ] Optimisation des expressions
- [ ] Mode interactif pour la version Python
- [ ] Export des résultats en JSON/XML

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Auteurs

- **Aoudia Nour Islam** - *Développement initial* - Étudiant en informatique

## 🙏 Remerciements

- Documentation de [Flex & Bison](https://www.gnu.org/software/flex/)
- Documentation de [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/)
- Communauté des développeurs de compilateurs
- Cours de théorie des langages et compilation
