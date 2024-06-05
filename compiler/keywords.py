# ----- Unary operators
# PLUS = 'plot'
# MINUS = 'plot twist'
# NOT = 'reverse movie'

# ----- Binary operators
# ADD = 'make new movie with'
# SUB = 'wrong director, sorry'
# MULT = 'won oscars with'
# DIV = 'lost oscars from'
# EQUAL = 'belongs to the same saga as'
# GT = 'better rated than'
# LT = 'worst rated than'
# OR = 'any streaming between'
# ALL = 'all streaming between'

# ----- Other operators
# if
# IF_NETFLIX = 'does Netflix have'
# IF_PRIME_VIDEO = 'does PrimeVideo have'
# IF_DISNEY_PLUS = 'does Disney+ have'
# END_STMT_IF = '?'

# ELSE = 'only Bluray'
# WHILE = 'loop scene'
# PRINT = 'watch movie'
# INPUT = 'select movie'
# VAR_DEC = 'movie'

PLOT:        str = 'plot'
TWIST:       str = 'twist'
REVERSE:     str = 'reverse'
MOVIE:       str = 'movie'
MAKE:        str = 'make'
NEW:         str = 'new'
WITH:        str = 'with'
WRONG:       str = 'wrong'
DIRECTOR:    str = 'director'
SORRY:       str = 'sorry'
WON:         str = 'won'
OSCARS:      str = 'oscars'
LOST:        str = 'lost'
FROM:        str = 'from'
BELONGS:     str = 'belongs'
TO:          str = 'to'
THE:         str = 'the'
SAME:        str = 'same'
SAGA:        str = 'saga'
AS:          str = 'as'
BETTER:      str = 'better'
RATED:       str = 'rated'
THAN:        str = 'than'
WORST:       str = 'worst'
ANY:         str = 'any'
STREAMING:   str = 'streaming'
BETWEEN:     str = 'between'
ALL:         str = 'all'
DOES:        str = 'does'
NETFLIX:     str = 'Netflix'
HAVE:        str = 'have'
PRIMEVIDEO:  str = 'PrimeVideo'
DISNEYPLUS:  str = 'DisneyPlus'
ONLY:        str = 'only'
BLURAY:      str = 'Bluray'
LOOP:        str = 'loop'
SCENE:       str = 'scene'
WATCH:       str = 'watch'
SELECT:      str = 'select'


KEYWORDS: set[str] = {
    PLOT,
    TWIST,
    REVERSE,
    MOVIE,
    MAKE,
    NEW,
    WITH,
    WRONG,
    DIRECTOR,
    SORRY,
    WON,
    OSCARS,
    LOST,
    FROM,
    BELONGS,
    TO,
    THE,
    SAME,
    SAGA,
    AS,
    BETTER,
    RATED,
    THAN,
    WORST,
    ANY,
    STREAMING,
    BETWEEN,
    ALL,
    DOES,
    NETFLIX,
    HAVE,
    PRIMEVIDEO,
    DISNEYPLUS,
    ONLY,
    BLURAY,
    LOOP,
    SCENE,
    WATCH,
    SELECT
}