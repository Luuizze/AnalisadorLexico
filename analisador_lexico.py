from analisador_sintatico import identificar_atom
from tabela_simbolos import (ATOMOS, 
                             inicializar_tabela_simbolos, 
                             adicionar_simbolo, 
                             atualizar_simbolo)

# Função para analisar léxico
def analisar_lexico(texto):
    posicao = 0
    tabela_simbolos = inicializar_tabela_simbolos()
    linha_atual = 1
    armazena_atomos = []
    flagFunc = False
    flagProg = False

    while posicao < len(texto):
        atomo, codigo, nova_posicao, linhas_adicionais = identificar_atom(texto, posicao)
        linha_atual += linhas_adicionais
        if atomo:
            if codigo is not None:
                atomo_trunc = atomo[:30] # Trunca o átomo para um máximo de 30 caracteres
                qtd_char_antes = len(atomo)
                qtd_char_depois = len(atomo_trunc)    
                if atomo.upper() == 'PROGRAMA':
                    flagProg = True
                elif atomo.upper() == 'FUNCOES':
                    flagFunc = True   
                if codigo.startswith('C'):
                    # Checa o contexto onde o programa se encontra e define seu código correto
                    if flagProg:
                        codigo = 'C06'
                        flagProg = False
                    elif flagFunc:
                        codigo = 'C05'
                        flagFunc = False
                    
                     # Adiciona e atualiza o símbolo na tabela
                    if not adicionar_simbolo(tabela_simbolos, codigo, atomo_trunc, qtd_char_antes, qtd_char_depois, linha_atual):
                        atualizar_simbolo(tabela_simbolos, atomo_trunc, linha_atual)

                armazena_atomos.append((atomo_trunc, codigo, linha_atual))
                         
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
    return tabela_simbolos, armazena_atomos

# Função para gerar relatório .LEX
def gerar_relatorio_lex(nome_arquivo, armazena_atomos, equipe_info):
    with open(f"{nome_arquivo}.LEX", 'w', encoding='utf-8') as arquivo:
        arquivo.write(equipe_info.strip() + "\n" + "\n")
        arquivo.write(f"RELATÓRIO DOS ÁTOMOS. Texto fonte analisado: {nome_arquivo}.241\n")
        arquivo.write("-" * 80 + "\n")
        for atomo, codigo, linha in armazena_atomos:
            arquivo.write(f"Lexeme: {atomo}, Código: {codigo}, ÍndiceTabSimb: {codigo[-2:]}, Linha: {linha}.\n")
            arquivo.write("-" * 80 + "\n")
