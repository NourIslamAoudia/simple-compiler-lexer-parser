from parser import parse_expression

def analyze_expression_from_file(file_path):
        # Lire l'expression depuis le fichier
        with open(file_path, "r", encoding="utf-8") as file:
            expression = file.read().strip()
            
        # Analyser l'expression et obtenir le résultat
        result = parse_expression(expression)
        print("\nRésultat de l'évaluation :")
        print(result)


# Exemples de tests
if __name__ == "__main__":
    file_path = "expression.txt"  # Remplacez par le chemin de votre fichier
    analyze_expression_from_file(file_path)
