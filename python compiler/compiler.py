from lexer import get_tokens
from parser import parse_expression

def analyze_expression(expression):
    
    print("Tokens générés :")
    tokens = get_tokens(expression)
    for token in tokens:
        print(f"Type: {token[0]}, Valeur: {token[1]}")

    # Analyser l'expression et obtenir le résultat
    result = parse_expression(expression)
    print("\nRésultat de l'évaluation :")
    print(result)

# Exemples de tests
if __name__ == "__main__":
    analyze_expression("(1+2)*3 %%islaaaaaaaaaaaaaaaaaaammayawww")