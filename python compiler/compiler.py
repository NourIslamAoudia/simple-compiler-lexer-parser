# main.py
from lexer import tokenize
from parser import parse_expression

def main():
    data =input("Entrez une expression arithmétique: ")
    # Utiliser le lexeur pour découper l'entrée en tokens
    print("Tokens:")
    tokens = tokenize(data)
    for token in tokens:
        print(f"Type: {token.type}, Valeur: {token.value}")

    # Utiliser le parser pour analyser l'expression
    result = parse_expression(data)
    print(f"Résultat de l'évaluation : {result}")

if __name__ == '__main__':
    main()
