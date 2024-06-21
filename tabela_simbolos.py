# Função para inicializar a tabela de símbolos
def inicializar_tabela_simbolos():
    return []

# Função para adicionar elementos na tabela
def adicionar_simbolo(tabela_simbolos, codigo, lexeme, qtd_char_antes, qtd_char_depois, tipo ,linha):
    if lexeme not in [entry['lexeme'] for entry in tabela_simbolos]:
        tabela_simbolos.append({
            'codigo': codigo,
            'lexeme': lexeme,
            'qtd_char_antes': qtd_char_antes,
            'qtd_char_depois': qtd_char_depois,
            'tipo': tipo,
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