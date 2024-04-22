# Movie Night Language

## Description

## Syntax Diagram
![Syntax Diagram](syntax_diagram.png)

## EBNF
```
BLOCK = {STATEMENT} ;
STATEMENT = (
    "\n" |
    (IDENTIFIER, "=", BOOL_EXPRESSION |
    "movie", IDENTIFIER, ( | "=", BOOL_EXP) |
    "watch movie", BOOL_EXPRESSION), ";" |
    ("loop scene", BOOL_EXPRESSION, "{", {STATEMENT} |
    "does", ("Netflix" | "PrimeVideo" | "Disney+"), "have", BOOL_EXPRESSION, "?", "{", {STATEMENT}, {"only Bluray", "{", {STATEMENT}, "}"}), "}"
) ;
BOOL_EXPRESSION = "any streaming between", BOOL_TERM, ",", BOOL_TERM, {",", BOOL_TERM} ;
BOOL_TERM = "all streaming between", RELATIONAL_EXPRESSION, ",", RELATIONAL_EXPRESSION, {",", RELATIONAL_EXPRESSION} ;
RELATIONAL_EXPRESSION = EXPRESSION, {("belongs to the same saga as" | "better rated than" | "worst rated than"), EXPRESSION} ;
EXPRESSION = TERM, {("make new movie with" | "wrong director, sorry"), TERM} ;
TERM = FACTOR, {("won oscars with" | "lost oscars from" | "would be nicer with"), FACTOR} ;
FACTOR = NUMBER | IDENTIFIER | ("plot" | "plot twist" | "reverse movie"), FACTOR | "(", BOOL_EXPRESSION, ")" | "select movie" ;
IDENTIFIER = LETTER, {LETTER | DIGIT | "_"} ;
NUMBER = DIGIT, {DIGIT} ;
LETTER = LOWERCASE | UPPERCASE ;
LOWERCASE = "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" ;
UPPERCASE = "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" ;
DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
```