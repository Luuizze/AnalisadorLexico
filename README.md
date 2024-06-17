# Analisador Léxico da Linguagem NikoBoko2024-1

## Descrição do Projeto

Este projeto é um analisador léxico que processa arquivos de código fonte escritos na linguagem NikoBoko2024-1, identificando átomos e gerando relatórios detalhados de análise léxica e da tabela de símbolos.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `nikoboko.py`: Script principal que coordena a leitura do arquivo fonte, a chamada da análise léxica e a geração dos relatórios.
- `analisador_lexico.py`: Contém as funções para análise léxica do texto fonte e geração do relatório `.LEX`.
- `analisador_sintatico.py`: Define as regras e padrões para identificar átomos no texto fonte.
- `tabela_simbolos.py`: Gerencia a tabela de símbolos, incluindo inicialização, adição e atualização de símbolos, e geração do relatório `.TAB`.

## Uso

### Requisitos

- Python 3.x

### Executando o Projeto

1. Clone o repositório para sua máquina local.

```bash
git clone <URL do repositório>
cd <diretório do projeto>
```

2. Execute o script principal nikoboko.py.

```
python nikoboko.py
```

3. Quando solicitado, insira o nome do arquivo fonte (sem extensão). O arquivo deve estar no mesmo diretório do script principal e ter a extensão .241.

4. O script processará o arquivo e gerará dois relatórios:

   - <nome_do_arquivo>.LEX: Relatório da análise léxica.
   - <nome_do_arquivo>.TAB: Relatório da tabela de símbolos.

## Detalhes do Código

`nikoboko.py`

- Lê o arquivo fonte especificado pelo usuário.
- Realiza a análise léxica utilizando a função analisar_lexico do módulo analisador_lexico.
- Gera relatórios .LEX e .TAB contendo detalhes da análise léxica e da tabela de símbolos, respectivamente.

`analisador_lexico.py`

- Define a função analisar_lexico que percorre o texto fonte, identificando átomos e gerenciando a tabela de símbolos.
- Contém a função gerar_relatorio_lex que cria o relatório .LEX com informações detalhadas dos átomos identificados.

`analisador_sintatico.py`

- Define a função identificar_atom que utiliza expressões regulares para identificar diferentes tipos de átomos no texto fonte.
- Prioriza a identificação de comentários de bloco e linha, seguido por palavras reservadas e variáveis.

`tabela_simbolos.py`

- Define a estrutura da tabela de símbolos e inicializa a tabela de palavras reservadas.
- Contém funções para adicionar e atualizar símbolos na tabela.
- Inclui a função gerar_relatorio_tab que cria o relatório .TAB com informações detalhadas da tabela de símbolos.

## Contribuidores

    - Carlos Henrique Racobaldo Luz Montes
    - Luiz Guilherme Guerreiro Carvalho
    - Maria Eduarda Lopes de Morais Brito
    - Mateus Torres Barreto
