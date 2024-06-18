from tabela_simbolos import adicionar_simbolo, atualizar_simbolo, inicializar_tabela_simbolos
from analisador_lexico import analisar_lexico
# Função para gerar relatório .LEX
def gerar_relatorio_lex(nome_arquivo, armazena_atomos, equipe_info):
    with open(f"{nome_arquivo}.LEX", 'w', encoding='utf-8') as arquivo:
        arquivo.write(equipe_info.strip() + "\n" + "\n")
        arquivo.write(f"RELATÓRIO DOS ÁTOMOS. Texto fonte analisado: {nome_arquivo}.241\n")
        arquivo.write("-" * 80 + "\n")
        for atomo, codigo, linha in armazena_atomos:
            arquivo.write(f"Lexeme: {atomo}, Código: {codigo}, ÍndiceTabSimb: {codigo[-2:]}, Linha: {linha}.\n")
            arquivo.write("-" * 80 + "\n")


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

# Função para ler arquivo
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
        return None
    
def trata_atomos(armazena_atomos):
    atomos_revisados = []
    tabela_simbolos = inicializar_tabela_simbolos()
    flagFunc = False
    flagProg = False
    for atomo, codigo, linha_atual in armazena_atomos:
        atomo_trunc = atomo[:30] # Trunca o átomo para um máximo de 30 caracteres
        qtd_char_antes = len(atomo)
        qtd_char_depois = len(atomo_trunc) 
        if atomo.upper() == 'PROGRAMA':
            flagProg = True
        elif atomo.upper() == 'FUNCOES':
            flagFunc = True   
        if codigo.startswith('C'):
        # Checa o contexto onde o programa se encontra e define seu código correto
            if flagProg and atomo[0].upper().isalpha():
                codigo = 'C06'
                flagProg = False                                             
            elif flagFunc and atomo[0].upper().isalpha():
                codigo = 'C05'
                flagFunc = False          
            # Adiciona e atualiza o símbolo na tabela
            if not adicionar_simbolo(tabela_simbolos, codigo, atomo_trunc, qtd_char_antes, qtd_char_depois, linha_atual):
                atualizar_simbolo(tabela_simbolos, atomo_trunc, linha_atual)
        atomos_revisados.append((atomo_trunc, codigo, linha_atual))  
    return tabela_simbolos, atomos_revisados


# Função principal
def main():
    equipe_info = """
    Código da Equipe: 5
    Componentes:
        Carlos Henrique Racobaldo Luz Montes; carlos.montes@aln.senaicimatec.edu.br; (75)981133861
        Luiz Guilherme Guerreiro Carvalho; luiz.carvalho@aln.senaicimatec.edu.br; (71)999141910
        Maria Eduarda Lopes de Morais Brito; maria.brito@aln.senaicimatec.edu.br; (71)992262193
        Mateus Torres Barreto; mateus.torres@aln.senaicimatec.edu.br; (75)98103-6459
    """

    # Solicita o nome do arquivo fonte sem a extensão
    nome_arquivo = input("Digite o nome do arquivo fonte (sem extensão): ")
    caminho_arquivo = nome_arquivo + ".241"
    texto_fonte = ler_arquivo(caminho_arquivo)
    if texto_fonte:
        # Realiza a análise léxica do texto fonte
        tabela_simbolos, atomos_retornados = trata_atomos(analisar_lexico(texto_fonte))
        # Gera relatórios de átomos e tabela de símbolos
        gerar_relatorio_lex(nome_arquivo, atomos_retornados, equipe_info)
        gerar_relatorio_tab(nome_arquivo, tabela_simbolos, equipe_info)
        print("Análise léxica concluída. Relatórios .LEX e .TAB gerados.")

if __name__ == "__main__":
    main()
