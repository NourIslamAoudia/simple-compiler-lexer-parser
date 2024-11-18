# Import des modules nécessaires
from lexer import get_tokens  # Module pour l'analyse lexicale
from parser import parse_expression  # Module pour l'analyse syntaxique
from typing import List, Tuple, Optional  # Types pour le typage statique

class AnalyzeError(Exception):
    """
    Exception personnalisée pour gérer les erreurs spécifiques à notre analyseur.
    Cette classe permet de différencier nos erreurs des exceptions Python standard.
    """
    pass

def extract_section_content(lines: List[str], start_index: int) -> Tuple[List[str], int]:
    """
    Extrait le contenu d'une section délimitée par des accolades.
    
    Cette fonction parcourt les lignes à partir de l'index de début donné et:
    - Compte les accolades ouvrantes et fermantes pour maintenir l'équilibre
    - Collecte le contenu entre les accolades
    - Vérifie la structure correcte des accolades
    
    Args:
        lines: Liste de toutes les lignes du fichier
        start_index: Index où commence la section (ligne avec l'accolade ouvrante)
        
    Returns:
        Tuple contenant:
        - La liste des lignes de contenu de la section
        - L'index de la ligne où se termine la section
    
    Raises:
        AnalyzeError: Si la structure des accolades est incorrecte
    """
    content = []  # Liste pour stocker le contenu de la section
    open_braces = 1  # Commence à 1 car on démarre après une accolade ouvrante
    current_index = start_index + 1
    
    while current_index < len(lines):
        line = lines[current_index].strip()
        # Compte les accolades ouvrantes et fermantes dans la ligne
        open_braces += line.count("{")
        open_braces -= line.count("}")
        
        if open_braces == 0:
            # On a trouvé la fin de la section
            return content, current_index
        
        if open_braces < 0:
            # Il y a plus d'accolades fermantes qu'ouvrantes
            raise AnalyzeError("Accolades mal équilibrées dans la section")
        
        # Ajoute la ligne au contenu si ce n'est pas une ligne d'accolade
        if not (line.startswith("{") or line.startswith("}")):
            content.append(line)
            
        current_index += 1
    
    # Si on arrive ici, c'est que la section n'est pas fermée
    raise AnalyzeError("Section non fermée correctement")

def find_section_index(lines: List[str], section_name: str) -> int:
    """
    Recherche l'index de début d'une section dans le fichier.
    
    Args:
        lines: Liste des lignes du fichier
        section_name: Nom de la section à trouver (ex: "VAR_GLOBAL")
        
    Returns:
        Index de la ligne où commence la section
        
    Raises:
        AnalyzeError: Si la section n'est pas trouvée dans le fichier
    """
    try:
        return lines.index(f"{section_name} {{")
    except ValueError:
        raise AnalyzeError(f"Section {section_name} non trouvée dans le fichier")

def analyze_program_from_file(file_path: str) -> Optional[dict]:
    """
    Fonction principale d'analyse du programme.
    Cette fonction:
    1. Lit le fichier
    2. Vérifie la présence et l'ordre des sections
    3. Extrait le contenu de chaque section
    4. Analyse le contenu de la section INSTRUCTION
    
    Args:
        file_path: Chemin vers le fichier à analyser
        
    Returns:
        Dictionnaire contenant les résultats de l'analyse avec les clés:
        - var_global: contenu de la section VAR_GLOBAL
        - declaration: contenu de la section DECLARATION
        - instruction: contenu de la section INSTRUCTION
        - tokens: jetons lexicaux de la section INSTRUCTION
        - parsed_result: résultat de l'analyse syntaxique
        Retourne None en cas d'erreur
    """
    try:
        # Lecture et nettoyage du fichier
        with open(file_path, "r", encoding="utf-8") as file:
            # Supprime les espaces et lignes vides
            lines = [line.strip() for line in file.readlines() if line.strip()]
        
        # Recherche des sections dans le fichier
        sections = {}
        for section in ["VAR_GLOBAL", "DECLARATION", "INSTRUCTION"]:
            sections[section] = find_section_index(lines, section)
        
        # Vérification de l'ordre des sections
        if not (sections["VAR_GLOBAL"] < sections["DECLARATION"] < sections["INSTRUCTION"]):
            raise AnalyzeError("L'ordre des sections est incorrect. L'ordre doit être: VAR_GLOBAL, DECLARATION, INSTRUCTION")
        
        # Extraction du contenu de chaque section
        section_contents = {}
        for section, index in sections.items():
            content, end_index = extract_section_content(lines, index)
            section_contents[section] = content
        
        # Analyse de la section INSTRUCTION
        instruction_content = "\n".join(section_contents["INSTRUCTION"]).strip()
        tokens = get_tokens(instruction_content)  # Analyse lexicale
        result = parse_expression(instruction_content)  # Analyse syntaxique
        
        # Retourne tous les résultats dans un dictionnaire
        return {
            "var_global": section_contents["VAR_GLOBAL"],
            "declaration": section_contents["DECLARATION"],
            "instruction": section_contents["INSTRUCTION"],
            "tokens": tokens,
            "parsed_result": result
        }
        
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' n'existe pas.")
    except AnalyzeError as e:
        print(f"Erreur d'analyse : {str(e)}")
    except Exception as e:
        print(f"Erreur inattendue : {str(e)}")
    
    return None

def main():
    """
    Point d'entrée principal du programme.
    Gère les arguments en ligne de commande et affiche les résultats.
    """
    import sys
    
    # Utilisation du fichier spécifié en argument ou du fichier par défaut
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "code.txt"
    
    # Analyse du fichier et affichage des résultats
    result = analyze_program_from_file(file_path)
    if result:
        print("\nAnalyse réussie !")
        print("\nContenu de la section VAR_GLOBAL :")
        print("\n".join(result["var_global"]))
        print("\nContenu de la section DECLARATION :")
        print("\n".join(result["declaration"]))
        print("\nContenu de la section INSTRUCTION :")
        print("\n".join(result["instruction"]))
        if not result["parsed_result"]:
            print("\nErreur d'analyse syntaxique")
        else:   
            print(result["parsed_result"])

# Point d'entrée du script
if __name__ == "__main__":
    main()