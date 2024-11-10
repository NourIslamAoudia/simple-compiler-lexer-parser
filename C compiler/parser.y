%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex(void);  // Déclaration de yylex()
void yyerror(const char *s);  // Déclaration de yyerror()
%}

%token NUMBER

%%

// Règles de la grammaire
expr:
    expr '+' expr { $$ = $1 + $3; printf("Résultat: %d\n", $$); }
  | expr '-' expr { $$ = $1 - $3; printf("Résultat: %d\n", $$); }
  | NUMBER { $$ = $1; printf("Nombre: %d\n", $$); }
  ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Erreur : %s\n", s);
}
