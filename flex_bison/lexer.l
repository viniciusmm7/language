%{
#include "parser.tab.h"
%}

DIGIT       [0-9]
LETTER      [a-zA-Z]
IDENTIFIER  {LETTER}({LETTER}|{DIGIT}|_)*
NUMBER      {DIGIT}+
SPACE       [ ]
COMMENT     "//"[^\n]*
NEWLINE     [\n]

%%

{COMMENT}                       ;
"movie"                         { return MOVIE; }
"watch"                         { return WATCH; }
"loop"                          { return LOOP; }
"scene"                         { return SCENE; }
"does"                          { return DOES; }
"Netflix"                       { return NETFLIX; }
"PrimeVideo"                    { return PRIME_VIDEO; }
"DisneyPlus"                    { return DISNEY_PLUS; }
"have"                          { return HAVE; }
"only"                          { return ONLY; }
"Bluray"                        { return BLURAY; }
"any"                           { return ANY; }
"streaming"                     { return STREAMING; }
"between"                       { return BETWEEN; }
"all"                           { return ALL; }
"belongs"                       { return BELONGS; }
"to"                            { return TO; }
"the"                           { return THE; }
"same"                          { return SAME; }
"saga"                          { return SAGA; }
"as"                            { return AS; }
"better"                        { return BETTER; }
"rated"                         { return RATED; }
"than"                          { return THAN; }
"worst"                         { return WORST; }
"make"                          { return MAKE; }
"new"                           { return NEW; }
"with"                          { return WITH; }
"wrong"                         { return WRONG; }
"director"                      { return DIRECTOR; }
"sorry"                         { return SORRY; }
"would"                         { return WOULD; }
"be"                            { return BE; }
"nicer"                         { return NICER; }
"won"                           { return WON; }
"oscars"                        { return OSCARS; }
"lost"                          { return LOST; }
"from"                          { return FROM; }
"plot"                          { return PLOT; }
"twist"                         { return TWIST; }
"reverse"                       { return REVERSE; }
"select"                        { return SELECT; }
"="                             { return ASSIGN; }
","                             { return COMMA; }
";"                             { return SEMICOLON; }
"("                             { return LPAREN; }
")"                             { return RPAREN; }
"{"                             { return LBRACE; }
"}"                             { return RBRACE; }
"?"                             { return QUESTION; }
{NEWLINE}                       { yylineno++; return NEWLINE; }
{NUMBER}                        { yylval.num = atoi(yytext); return NUMBER; }
{IDENTIFIER}                    { yylval.str = strdup(yytext); return IDENTIFIER; }
{SPACE}                         ;

%%

int yywrap() {
    return 1;
}
