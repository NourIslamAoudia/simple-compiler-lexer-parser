%{
#include "parser.tab.h"  // Inclure le fichier header généré par bison
extern void yyerror(const char *s);  // Déclaration de la fonction yyerror
%}

%%
[0-9]+           { yylval = atoi(yytext); return NUMBER; }
[ \t\n]          { /* ignorer les espaces et les nouvelles lignes */ }
"+"              { return '+'; }
"-"              { return '-'; }
.                { yyerror("caractère invalide"); exit(1); }  // Appeler yyerror sans return et arrêter le programme
%%

int yywrap() {
    return 1;
}
