import re
from tabela_simbolos import tabela_reservados, ATOMOS

# Regex de padrões para elementos léxicos
padroes = {
    'consReal': r'^\d+\.\d*([eE][+-]?\d+)?',
    'consInteiro': r'^\d+',
    'consCadeia': r'^"[^"]*"',
    'consCaracter': r"^'[^']'",
    'variavel': r'^[_a-zA-Z]\w*',
    'nomFuncao': r'^[a-zA-Z]\w*',
    'nomPrograma': r'^[a-zA-Z]\w*', 
    'comentario_linha': r'^//.*',
    'comentario_bloco': r'^/\*[\s\S]*?\*/'
}

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
