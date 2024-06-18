import re
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
}

# Regex de padrões para elementos léxicos
padroes = {
    'consReal': r'^\d+\.\d*([eE][+-]?\d+)?',
    'consInteiro': r'^\d+',
    'consCadeia': r'^"[^"]*"',
    'consCaracter': r"^'[^']'",
    'variavel': r'^[a-zA-Z_]\w*',
    'nomFuncao': r'^[a-zA-Z_]\w*',
    'nomPrograma': r'^[a-zA-Z_]\w*', 
    'comentario_linha': r'^//.*',
    'comentario_bloco': r'^/\*[\s\S]*?\*/'
}

# Inicialização da tabela de palavras e símbolos reservados
tabela_reservados = {k: v for k, v in ATOMOS.items() if not v.startswith('C')}

# Função para identificar átomos
def identificar_atom(texto, posicao):
    # Verificar comentários de bloco primeiro
    for tipo, regex in padroes.items():
        if tipo == 'comentario_bloco':
            match = re.match(regex, texto[posicao:], re.DOTALL)
            if match:
                if '\n' in match.group():
                    linhas_adicionais = match.group().count('\n') # Conta as linhas dentro do comentário
                return match.group(), None, posicao + len(match.group()), linhas_adicionais

    # Verificar comentários de linha em segundo lugar
    for tipo, regex in padroes.items():
        if tipo == 'comentario_linha':
            match = re.match(regex, texto[posicao:], re.IGNORECASE)
            if match:
                linhas_adicionais = 1 if '\n' in match.group() else 0
                return match.group(), None, posicao + len(match.group()), linhas_adicionais

    # Verificar átomos reservados e variáveis, priorizando o maior
    for padrao in sorted(tabela_reservados.keys(), key=len, reverse=True):
        if texto[posicao:posicao + len(padrao)].upper() == padrao.upper():
            return padrao, tabela_reservados[padrao], posicao + len(padrao), 0

    # Verificar constantes e identificadores
    for tipo, regex in padroes.items():
        if tipo not in ['comentario_linha', 'comentario_bloco']:
            match = re.match(regex, texto[posicao:], re.IGNORECASE)
            if match:
                return match.group(), ATOMOS.get(tipo, 'C07'), posicao + len(match.group()), 0

    return None, None, posicao, 0

# Função para analisar léxico
def analisar_lexico(texto):
    posicao = 0
    linha_atual = 1
    armazena_atomos = []
    while posicao < len(texto):
        atomo, codigo, nova_posicao, linhas_adicionais = identificar_atom(texto, posicao)
        linha_atual += linhas_adicionais
        if atomo:
            if codigo is not None:  
                armazena_atomos.append((atomo, codigo, linha_atual))        
            posicao = nova_posicao
        else:
            # Tratamento de exceções
            if texto[posicao] == '\n':
                linha_atual += 1
            elif texto[posicao].isspace():
                pass  # Ignorar espaços em branco
            else:
                print(f"Caractere inválido ignorado: {texto[posicao]} na linha {linha_atual}") 
            posicao += 1          
    return armazena_atomos