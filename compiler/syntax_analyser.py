from .lexical_analyser import Tokenizer, PrePro
from .semantic_analyser import *


class Parser:
    tokenizer = None

    @staticmethod
    def parse_factor() -> Node:
        tokenizer: Tokenizer = Parser.tokenizer

        # Integer: "<int>"
        if tokenizer.next.type == 'INT':
            token = tokenizer.next.value
            tokenizer.select_next()
            return IntVal(token, [])

        # Identifier: "<identifier>"
        elif tokenizer.next.type == 'IDENTIFIER':
            identifier = tokenizer.next.value
            tokenizer.select_next()
            return IdentifierNode(identifier, [])

        elif tokenizer.next.type == 'PLOT':
            value = '+'  # Un op plus: "plot <factor>"
            tokenizer.select_next()
            
            if tokenizer.next.type == 'TWIST':
                value = '-'  # Un op minus: "plot twist <factor>"
                tokenizer.select_next()
            
            return UnOp(value, [Parser.parse_factor()])    

        # Un op not: "reverse movie <factor>"
        elif tokenizer.next.type == 'REVERSE':
            tokenizer.select_next()
            
            if tokenizer.next.type == 'MOVIE':
                value = 'not'
                tokenizer.select_next()
                
                return UnOp(value, [Parser.parse_factor()])
            
            raise SyntaxError(f'Reverse must be followed by "movie" at position "{tokenizer.position}"')

        # Parenthesis expression: "(<bool_expression>)"
        elif tokenizer.next.type == 'LPAREN':
            tokenizer.select_next()
            result: Node = Parser.parse_bool_expression()

            if tokenizer.next.type == 'RPAREN':
                tokenizer.select_next()
                return result

            raise SyntaxError(f'Missing closing parenthesis at position "{tokenizer.position}"')

        # Read statement: "select movie()"
        elif tokenizer.next.type == 'SELECT':
            tokenizer.select_next()
            
            if tokenizer.next.type == 'MOVIE':
                tokenizer.select_next()

                if tokenizer.next.type == 'LPAREN':
                    tokenizer.select_next()

                    if tokenizer.next.type == 'RPAREN':
                        tokenizer.select_next()
                        return ReadNode('READ', [])

                    raise SyntaxError(f'Missing closing parenthesis when calling read() at position "{tokenizer.position}"')

                raise SyntaxError(f'"select movie()" call must have parenthesis at position "{tokenizer.position}"')
            
            raise SyntaxError(f'"select" must be followed by "movie" at position "{tokenizer.position}"')

        raise SyntaxError(f'Invalid syntax at position "{tokenizer.position}"')

    @staticmethod
    def parse_term() -> Node:
        tokenizer: Tokenizer = Parser.tokenizer
        result: Node = Parser.parse_factor()

        while tokenizer.next.type in ['WON', 'LOST']:
            
            # Bin op multiplication: "_ won oscars with <factor>"
            if tokenizer.next.type == 'WON':
                tokenizer.select_next()
                
                if tokenizer.next.type == 'OSCARS':
                    tokenizer.select_next()
                    
                    if tokenizer.next.type == 'WITH':
                        tokenizer.select_next()
                        value = '*'
                        result = BinOp(value, [result, Parser.parse_factor()])
                        continue
                    
                    raise SyntaxError(f'Expected "with" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                
                raise SyntaxError(f'Expected "oscars" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
            
            # Bin op division: "_ lost oscars from <factor>"
            if tokenizer.next.type == 'LOST':
                tokenizer.select_next()
                
                if tokenizer.next.type == 'OSCARS':
                    tokenizer.select_next()
                    
                    if tokenizer.next.type == 'FROM':
                        tokenizer.select_next()
                        value = '/'
                        result = BinOp(value, [result, Parser.parse_factor()])
                        continue
                    
                    raise SyntaxError(f'Expected "from" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                
                raise SyntaxError(f'Expected "oscars" at position "{tokenizer.position}", found "{tokenizer.next.value}"')

        return result

    @staticmethod
    def parse_expression() -> Node:
        tokenizer: Tokenizer = Parser.tokenizer
        result: Node = Parser.parse_term()

        while tokenizer.next.type in ['MAKE', 'WRONG']:
            
            # Bin op addition: "_ make new movie with <term>"
            if tokenizer.next.type == 'MAKE':
                tokenizer.select_next()
                
                if tokenizer.next.type == 'NEW':
                    tokenizer.select_next()
                    
                    if tokenizer.next.type == 'MOVIE':
                        tokenizer.select_next()
                        
                        if tokenizer.next.type == 'WITH':
                            tokenizer.select_next()
                            value = '+'
                            result = BinOp(value, [result, Parser.parse_term()])
                            continue
                        
                        raise SyntaxError(f'Expected "with" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                    
                    raise SyntaxError(f'Expected "movie" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                
                raise SyntaxError(f'Expected "new" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
            
            # Bin op subtraction: "_ wrong director, sorry <term>"
            if tokenizer.next.type == 'WRONG':
                tokenizer.select_next()
                
                if tokenizer.next.type == 'DIRECTOR':
                    tokenizer.select_next()
                    
                    if tokenizer.next.type == 'COMMA':
                        tokenizer.select_next()
                        
                        if tokenizer.next.type == 'SORRY':
                            tokenizer.select_next()
                            value = '-'
                            result = BinOp(value, [result, Parser.parse_term()])
                            continue
                        
                        raise SyntaxError(f'Expected "sorry" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                    
                    raise SyntaxError(f'Expected comma at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                
                raise SyntaxError(f'Expected "director" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
            
        return result
    
    @staticmethod
    def parse_relational_expression() -> Node:
        tokenizer: Tokenizer = Parser.tokenizer
        result: Node = Parser.parse_expression()
        
        while tokenizer.next.type in ['BELONGS', 'BETTER', 'WORST']:
            
            # Bin op equals: "_ belongs to the same saga as <expression>"
            if tokenizer.next.type == 'BELONGS':
                tokenizer.select_next()
                
                if tokenizer.next.type == 'TO':
                    tokenizer.select_next()
                    
                    if tokenizer.next.type == 'THE':
                        tokenizer.select_next()
                        
                        if tokenizer.next.type == 'SAME':
                            tokenizer.select_next()
                            
                            if tokenizer.next.type == 'SAGA':
                                tokenizer.select_next()
                                
                                if tokenizer.next.type == 'AS':
                                    tokenizer.select_next()
                                    value = '=='
                                    result = BinOp(value, [result, Parser.parse_expression()])
                                    continue
                                
                                raise SyntaxError(f'Expected "as" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                            
                            raise SyntaxError(f'Expected "saga" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                        
                        raise SyntaxError(f'Expected "same" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                    
                    raise SyntaxError(f'Expected "the" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                
                raise SyntaxError(f'Expected "to" at position "{tokenizer.position}", found "{tokenizer.next.value}"')

            # Bin op greater than: "_ better rated than <expression>"
            if tokenizer.next.type == 'BETTER':
                tokenizer.select_next()
                
                if tokenizer.next.type == 'RATED':
                    tokenizer.select_next()
                    
                    if tokenizer.next.type == 'THAN':
                        tokenizer.select_next()
                        value = '>'
                        result = BinOp(value, [result, Parser.parse_expression()])
                        continue
                    
                    raise SyntaxError(f'Expected "than" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                
                raise SyntaxError(f'Expected "rated" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
            
            # Bin op less than: "_ worst rated than <expression>"
            if tokenizer.next.type == 'WORST':
                tokenizer.select_next()
                
                if tokenizer.next.type == 'RATED':
                    tokenizer.select_next()
                    
                    if tokenizer.next.type == 'THAN':
                        tokenizer.select_next()
                        value = '<'
                        result = BinOp(value, [result, Parser.parse_expression()])
                        continue
                    
                    raise SyntaxError(f'Expected "than" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                
                raise SyntaxError(f'Expected "rated" at position "{tokenizer.position}", found "{tokenizer.next.value}"')

        return result
    
    @staticmethod
    def parse_bool_term() -> Node:
        tokenizer: Tokenizer = Parser.tokenizer

        # Bin op and: "all streaming between <bool_term>, <bool_term>"
        if tokenizer.next.type == 'ALL':
            tokenizer.select_next()
            
            if tokenizer.next.type == 'STREAMING':
                tokenizer.select_next()
                
                if tokenizer.next.type == 'BETWEEN':
                    tokenizer.select_next()
                    left = Parser.parse_relational_expression()
                    
                    if tokenizer.next.type == 'COMMA':
                        tokenizer.select_next()
                        value = 'and'
                        right = Parser.parse_relational_expression()
                        return BinOp(value, [left, right])
                    
                    raise SyntaxError(f'Expected comma at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                
                raise SyntaxError(f'Expected "between" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
            
            raise SyntaxError(f'Expected "streaming" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
        
        return Parser.parse_relational_expression()

    @staticmethod
    def parse_bool_expression() -> Node:
        tokenizer: Tokenizer = Parser.tokenizer
        
        # Bin op or: "any streaming between <bool_term>, <bool_term>"
        if tokenizer.next.type == 'ANY':
            tokenizer.select_next()
            
            if tokenizer.next.type == 'STREAMING':
                tokenizer.select_next()
                
                if tokenizer.next.type == 'BETWEEN':
                    tokenizer.select_next()
                    left = Parser.parse_bool_term()
                    
                    if tokenizer.next.type == 'COMMA':
                        tokenizer.select_next()
                        value = 'or'
                        right = Parser.parse_bool_term()
                        return BinOp(value, [left, right])
                    
                    raise SyntaxError(f'Expected comma at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                
                raise SyntaxError(f'Expected "between" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
            
            raise SyntaxError(f'Expected "streaming" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
        
        return Parser.parse_bool_term()

    @staticmethod
    def parse_statement() -> Node:
        tokenizer: Tokenizer = Parser.tokenizer
        # No operation: "(\n | ;)"
        if tokenizer.next.type in ['NEWLINE', 'SEMICOLON']:
            tokenizer.select_next()
            return NoOp(None, [])

        # Variable assignment: "<identifier> = <bool_expression>;"
        elif tokenizer.next.type == 'IDENTIFIER':
            identifier = tokenizer.next.value
            tokenizer.select_next()

            if tokenizer.next.type == 'ASSIGN':
                assignment_token = tokenizer.next.value
                tokenizer.select_next()
                expression = Parser.parse_bool_expression()
                
                if tokenizer.next.type == 'SEMICOLON':
                    return Assignment(assignment_token, [identifier, expression])

                raise SyntaxError(f'Missing semicolon at position "{tokenizer.position}"')

            raise SyntaxError(f'Missing assignment at position "{tokenizer.position}"')

        # Variable declaration: "movie <identifier> [= <bool_expression>];"
        elif tokenizer.next.type == 'MOVIE':
            tokenizer.select_next()

            if tokenizer.next.type == 'IDENTIFIER':
                identifier = tokenizer.next.value
                tokenizer.select_next()
                expression = None

                if tokenizer.next.type == 'ASSIGN':
                    tokenizer.select_next()
                    expression = Parser.parse_bool_expression()

                if tokenizer.next.type == 'SEMICOLON':
                    return VarDeclaration('MOVIE', [identifier, expression])

                raise SyntaxError(f'Invalid syntax declaring variable at position "{tokenizer.position}"')

        # Print statement: "watch movie(<bool_expression>);"
        elif tokenizer.next.type == 'WATCH':
            tokenizer.select_next()
            
            if tokenizer.next.type == 'MOVIE':
                tokenizer.select_next()

                if tokenizer.next.type == 'LPAREN':
                    tokenizer.select_next()
                    expression = Parser.parse_bool_expression()

                    if tokenizer.next.type == 'RPAREN':
                        tokenizer.select_next()

                        if tokenizer.next.type == 'SEMICOLON':
                            return PrintNode('PRINT', [expression])
        
                        raise SyntaxError(f'Missing semicolon at position "{tokenizer.position}"')
                    
                    raise SyntaxError(f'Missing closing parenthesis at position "{tokenizer.position}"')
                
                raise SyntaxError(f'Missing left parenthesis at position "{tokenizer.position}"')
            
            raise SyntaxError(f'Expected "movie" at position "{tokenizer.position}", found "{tokenizer.next.value}"')

        # If statement: "does (Netflix | PrimeVideo | Disney+) have <bool_expression>? { <statements> } [only Bluray { <statements> }]"
        elif tokenizer.next.type == 'DOES':
            tokenizer.select_next()
            
            if tokenizer.next.type in ['NETFLIX', 'PRIMEVIDEO', 'DISNEYPLUS']:
                tokenizer.select_next()
                
                if tokenizer.next.type == 'HAVE':
                    tokenizer.select_next()
                    condition = Parser.parse_bool_expression()
                    children = [
                        condition,
                        BlockNode('IF_BLOCK', []),
                        BlockNode('ELSE_BLOCK', [])
                    ]
                    if_node = IfNode('IF', children)
                    
                    if tokenizer.next.type == 'QUESTION':
                        tokenizer.select_next()
                        
                        if tokenizer.next.type == 'LBRACE':
                            left_brace_position = tokenizer.position
                            tokenizer.select_next()
                            
                            while tokenizer.next.type != 'RBRACE':
                                if tokenizer.next.type == 'EOF':
                                    raise SyntaxError(f'Missing closing brace after left brace position "{left_brace_position}"')
                                
                                statement = Parser.parse_statement()
                                if_node.children[1].children.append(statement)
                            
                            rbrace_if_found: bool = True
                                
                            tokenizer.select_next()
                            
                            if tokenizer.next.type != 'ONLY' and rbrace_if_found:
                                return if_node
                                
                            if tokenizer.next.type == 'ONLY':
                                tokenizer.select_next()
                                
                                if tokenizer.next.type == 'BLURAY':
                                    tokenizer.select_next()
                                    
                                    if tokenizer.next.type == 'LBRACE':
                                        left_brace_position = tokenizer.position
                                        tokenizer.select_next()
                                        
                                        while tokenizer.next.type != 'RBRACE':
                                            if tokenizer.next.type == 'EOF':
                                                raise SyntaxError(f'Missing closing brace after left brace position "{left_brace_position}"')
                                            
                                            statement = Parser.parse_statement()
                                            if_node.children[2].children.append(statement)
                                        
                            if tokenizer.next.type == 'RBRACE':
                                tokenizer.select_next()
                                return if_node
                            
                            raise SyntaxError(f'Missing closing brace after left brace position "{left_brace_position}"')
                        
                        raise SyntaxError(f'Expected left brace at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                    
                    raise SyntaxError(f'Expected "?" at position "{tokenizer.position}", found "{tokenizer.next.value}"')
                
                raise SyntaxError(f'Expected "have" at position "{tokenizer.position}", found "{tokenizer.next.value}"')

            raise SyntaxError(f'Expected streaming service at position "{tokenizer.position}", found "{tokenizer.next.value}"')

        # While statement: "loop scene <bool_expression> { <statements> }"
        elif tokenizer.next.type == 'LOOP':
            tokenizer.select_next()
            
            if tokenizer.next.type == 'SCENE':
                tokenizer.select_next()
                condition = Parser.parse_bool_expression()
                children = [
                    condition,
                    BlockNode('WHILE_BLOCK', [])
                ]
                while_node = WhileNode('WHILE', children)
                
                if tokenizer.next.type == 'LBRACE':
                    left_brace_position = tokenizer.position
                    tokenizer.select_next()
                    
                    while tokenizer.next.type != 'RBRACE':
                        if tokenizer.next.type == 'EOF':
                            raise SyntaxError(f'Missing closing brace after left brace position "{left_brace_position}"')
                        
                        statement = Parser.parse_statement()
                        while_node.children[1].children.append(statement)

                    if tokenizer.next.type == 'RBRACE':
                        tokenizer.select_next()
                        return while_node
                    
                    raise SyntaxError(f'Missing closing brace after left brace position "{left_brace_position}"')

                raise SyntaxError(f'Expected left brace at position "{tokenizer.position}", found "{tokenizer.next.value}"')
            
            raise SyntaxError(f'Expected "scene" at position "{tokenizer.position}", found "{tokenizer.next.value}"')

        raise SyntaxError(f'Invalid syntax at position "{tokenizer.position}", found "{tokenizer.next.value}"')

    @staticmethod
    def parse_block() -> Node:
        tokenizer: Tokenizer = Parser.tokenizer
        result = BlockNode('BLOCK', [])

        while tokenizer.next.type != 'EOF':
            result.children.append(Parser.parse_statement())

        return result

    @staticmethod
    def run(code: str) -> Node:
        if not code:
            raise ValueError('The code cannot be empty')

        code = PrePro.filter(code)

        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.select_next()
        
        result = Parser.parse_block()

        if Parser.tokenizer.next.type != 'EOF':
            raise SyntaxError(f'Invalid syntax at position "{Parser.tokenizer.position}"')

        return result
