from lexer import get_tokens
from parser import parse_expression

# Fonction principale pour analyser une expression
def analyze_expression(expression):
    print("Tokens générés :")
    tokens = get_tokens(expression)
    for token in tokens:
        print(f"Type: {token[0]}, Valeur: {token[1]}")

    # Analyser l'expression et obtenir le résultat
    result = parse_expression(expression)
    print("\nRésultat de l'évaluation :")
    print(result)

# Exemple d'utilisation
if __name__ == "__main__":
    analyze_expression("2 + 3 * 4 - 5") # Doit afficher 9
    print("----------------------------------------")
    analyze_expression("2 * (3+4) - 6") # Doit afficher 8
    print("----------------------------------------")
    analyze_expression("6 / 2 + 2") # Doit afficher 5
    print("----------------------------------------")
    analyze_expression("2 > 1")
    print("----------------------------------------")
    analyze_expression("(2 i 1) && (3 < 4)")
    print("----------------------------------------")
    analyze_expression("!0")
