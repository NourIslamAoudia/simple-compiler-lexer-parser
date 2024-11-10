import ply.lex as lex

# Liste des tokens
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN','AND',   
    'OR', 
    'NOT',  
    'LT',  
    'LE',   
    'GT',   
    'GE',  
    'EQ',    
    'NE',   
    'TRUE',  
    'FALSE', 
)

# Règles de lexing
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'    
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

t_AND = r'&&'
t_OR  = r'\|\|'
t_NOT = r'!'
t_LT  = r'<'
t_LE  = r'<='
t_GT  = r'>'
t_GE  = r'>='
t_EQ  = r'=='
t_NE  = r'!='

# Règle pour les nombres
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorer les espaces et les tabulations
t_ignore = ' \t'

# Règle pour gérer les retours à la ligne
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Gérer les erreurs de lexing
def t_error(t):
    print(f"Caractère illégal '{t.value[0]}'")
    t.lexer.skip(1)

# Créer le lexer
lexer = lex.lex()

# Fonction pour récupérer tous les tokens d'une expression
def get_tokens(input_data):
    lexer.input(input_data)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append((tok.type, tok.value))
    return tokens_list
