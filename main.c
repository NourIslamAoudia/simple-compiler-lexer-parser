#include <stdio.h>
#include <stdlib.h>

extern int yyparse(void); // Déclaration de yyparse
extern FILE *yyin;        // Déclaration de l'entrée pour le lexer

int main() {
    printf("Entrez une expression :\n");
    yyin = stdin;  // Utilisation de l'entrée standard pour le lexer
    yyparse();     // Appeler la fonction de parsing
    return 0;
}
