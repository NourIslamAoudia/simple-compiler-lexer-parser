# lexer.py
import ply.lex as lex

# Liste des tokens
tokens = (
    'NUMBER', 'PLUS', 'TIMES', 'LPAREN', 'RPAREN', 'MINUS',
)

# Expression régulière pour chaque token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+'

# Ignorer les espaces et tabulations
t_ignore = ' \t'

# Gérer les erreurs
def t_error(t):
    print(f"Caractère illégal '{t.value[0]}'")
    t.lexer.skip(1)

# Construire le lexer
lexer = lex.lex()

# Fonction pour analyser le texte et renvoyer les tokens
def tokenize(data):
    lexer.input(data)
    tokens_list = []
    while True:
        token = lexer.token()
        if not token:
            break
        tokens_list.append(token)
    return tokens_list
