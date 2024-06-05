from sys import argv
from compiler.syntax_analyser import Parser
from compiler.semantic_analyser import SemanticAnalyser, Node, SymbolTable


def main() -> None:
    mnl_file: str = argv[1]
    
    if not mnl_file.endswith('.mnl'):
        raise Exception('Invalid file extension. Please provide a .mnl file')
    
    with open(mnl_file, 'r') as file:
        file_name = file.name.split('.')[0].split('/')[-1]
        code = file.read()

    symbol_table: SymbolTable = SymbolTable()
    parser: Parser = Parser()
    ast: Node = parser.run(code)
    result: any = SemanticAnalyser.run(ast, symbol_table)
    
    with open(f'asm_out/{file_name}.asm', 'w') as file:
        with open('asm/header.asm', 'r') as header:
            file.write(header.read())
            
        file.write(result)
        
        with open('asm/footer.asm', 'r') as footer:
            file.write(footer.read())


if __name__ == '__main__':
    main()
