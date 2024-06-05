#!/bin/bash

cd flex_bison/

flex lexer.l
bison -d parser.y

sed -i 's/extern int yylex (void);/extern "C" int yylex(void);/' lex.yy.c
sed -i 's/#define YY_DECL int yylex (void)/#define YY_DECL extern "C" int yylex()/' lex.yy.c

g++ parser.tab.c lex.yy.c -lfl -o mnlang

echo "Movie Night Language executable created"

cd ../examples/

for script in *.mnl; do
    if [ -f "$script" ] && [ -r "$script" ]; then
        echo "Running $script"
        ../flex_bison/mnlang "$script"
    else
        echo "Error: $script is not a readable file or does not exist"
    fi
done