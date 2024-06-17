from analisador_lexico import (gerar_relatorio_lex, analisar_lexico)
from tabela_simbolos import (gerar_relatorio_tab)

# Função para ler arquivo
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
        return None

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
        tabela_simbolos, atomos_alterados = analisar_lexico(texto_fonte)
        # Gera relatórios de átomos e tabela de símbolos
        gerar_relatorio_lex(nome_arquivo, atomos_alterados, equipe_info)
        gerar_relatorio_tab(nome_arquivo, tabela_simbolos, equipe_info)
        print("Análise léxica concluída. Relatórios .LEX e .TAB gerados.")

if __name__ == "__main__":
    main()
