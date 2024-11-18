from lexer import get_tokens
from parser import parse_expression

def analyze_program_from_file(file_path):
    # Lire le contenu du fichier
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    # Supprimer les espaces inutiles et les lignes vides
    lines = [line.strip() for line in lines if line.strip()]
    
    # Vérifier la structure globale
    if not (lines[0] == "VAR_GLOBAL {" and "}" in lines and "DECLARATION {" in lines and "INSTRUCTION {" in lines):
        raise SyntaxError("Erreur : La structure globale du programme est invalide.")
    
    # Extraire les sections
    var_global_index = lines.index("VAR_GLOBAL {")
    declaration_index = lines.index("DECLARATION {")
    instruction_index = lines.index("INSTRUCTION {")
    
    # Vérification des bornes
    if var_global_index >= declaration_index or declaration_index >= instruction_index:
        raise SyntaxError("Erreur : L'ordre des sections est incorrect.")
    
    # Extraire le contenu de la section INSTRUCTION
    instruction_lines = []
    open_braces = 0
    for line in lines[instruction_index + 1:]:  # On commence à partir de la ligne suivante à "INSTRUCTION {"
        if line == "}":
            open_braces -= 1
            if open_braces == 0:
                break
        elif line == "{":
            open_braces += 1
        else:
            instruction_lines.append(line)
    
    # Joindre les lignes d'instructions et analyser
    instruction_content = "\n".join(instruction_lines).strip()
    print("Contenu de la section INSTRUCTION :")
    print(instruction_content)

    # Analyser l'expression si nécessaire
    result = parse_expression(instruction_content)
    print("\nRésultat de l'évaluation :")
    print(result)


# Exemple de test
if __name__ == "__main__":
    file_path = "expression.txt"  # Remplacez par le chemin de votre fichier
    analyze_program_from_file(file_path)
