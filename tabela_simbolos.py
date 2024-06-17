# Estruturas para armazenar os átomos e padrões
ATOMOS = {
    'cadeia': 'A01', 'caracter': 'A02', 'declaracoes': 'A03', 'enquanto': 'A04', 'false': 'A05',
    'fimDeclaracoes': 'A06', 'fimEnquanto': 'A07', 'fimFunc': 'A08', 'fimFuncoes': 'A09', 'fimPrograma': 'A10',
    'fimSe': 'A11', 'funcoes': 'A12', 'imprime': 'A13', 'inteiro': 'A14', 'logico': 'A15',
    'pausa': 'A16', 'programa': 'A17', 'real': 'A18', 'retorna': 'A19', 'se': 'A20',
    'senao': 'A21', 'tipoFuncao': 'A22', 'tipoParam': 'A23', 'tipoVar': 'A24', 'true': 'A25',
    'vazio': 'A26', '%': 'B01', '(': 'B02', ')': 'B03', ',': 'B04', ':': 'B05', ':=': 'B06',
    ';': 'B07', '?': 'B08', '[': 'B09', ']': 'B10', '{': 'B11', '}': 'B12', '-': 'B13',
    '*': 'B14', '/': 'B15', '+': 'B16', '!=': 'B17', '#': 'B18', '<': 'B19', '<=': 'B20',
    '==': 'B21', '>': 'B22', '>=': 'B23',
    'consCadeia': 'C01', 'consCaracter': 'C02', 'consInteiro': 'C03', 'consReal': 'C04',
    'nomFuncao': 'C05', 'nomPrograma': 'C06', 'variavel': 'C07',
    'subMáquina1': 'D01', 'subMáquina2': 'D02', 'subMáquina3': 'D03'
}

# Inicialização da tabela de palavras e símbolos reservados
tabela_reservados = {k: v for k, v in ATOMOS.items() if not v.startswith('C')}

# Função para inicializar a tabela de símbolos
def inicializar_tabela_simbolos():
    return []

# Função para adicionar elementos na tabela
def adicionar_simbolo(tabela_simbolos, codigo, lexeme, qtd_char_antes, qtd_char_depois, linha):
    if lexeme not in [entry['lexeme'] for entry in tabela_simbolos]:
        tabela_simbolos.append({
            'codigo': codigo,
            'lexeme': lexeme,
            'qtd_char_antes': qtd_char_antes,
            'qtd_char_depois': qtd_char_depois,
            'tipo': 'Identificador',
            'linhas': [linha]
        })
        return True
    return False

# Função para atualizar elementos na tabela
def atualizar_simbolo(tabela_simbolos, lexeme, linha):
    for entry in tabela_simbolos:
        if entry['lexeme'] == lexeme:
            if len(entry['linhas']) < 5:
                entry['linhas'].append(linha)
            break

# Função para gerar relatório .TAB
def gerar_relatorio_tab(nome_arquivo, tabela_simbolos, equipe_info):
    with open(f"{nome_arquivo}.TAB", 'w', encoding='utf-8') as arquivo:
        arquivo.write(equipe_info.strip() + "\n" + "\n")
        arquivo.write(f"RELATÓRIO DA TABELA DE SÍMBOLOS. Texto fonte analisado: {nome_arquivo}.241\n")
        arquivo.write("-" * 80 + "\n")
        for i, entry in enumerate(tabela_simbolos, start=1):
            linhas = ', '.join(map(str, entry['linhas']))
            arquivo.write(f"Entrada: {i}, Código: {entry['codigo']}, Lexeme: {entry['lexeme']},\n")
            arquivo.write(f"QtdCharAntesTrunc: {entry['qtd_char_antes']}, QtdCharDepoisTrunc: {entry['qtd_char_depois']},\n")
            arquivo.write(f"TipoSimb: {entry['tipo']}, Linhas: ({linhas})\n")
            arquivo.write("-" * 80 + "\n")