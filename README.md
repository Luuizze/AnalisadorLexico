# Analisador Léxico da Linguagem NikoBoko2024-1

## Descrição do Projeto

Este projeto implementa um analisador léxico e sintático que processa arquivos de código fonte escritos na linguagem NikoBoko2024-1. O analisador léxico identifica e classifica os tokens no código-fonte, enquanto o analisador sintático organiza esses tokens em uma estrutura lógica.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `analisador_lexico.py`: Responsável por analisar o código-fonte e identificar os tokens.
- `analisador_sintatico.py`: Define as regras, ler arquivo e gera relatórios `.LEX` e `.TAB` com base nos tokens identificados, basicamente o Script principal.
- `tabela_simbolos.py`: Gerencia a tabela de símbolos, incluindo inicialização, adição e atualização de símbolos.
- `setup`: Arquivo de criação do executável do analisador encontrado dentro da pasta build.

## Uso

### Requisitos

- Python 3.x

### Executando o Projeto pelo Terminal

1. Clone o repositório para sua máquina local.

```bash
git clone <URL do repositório>
cd <diretório do projeto>
```

2. Execute o script principal analisador_sintatico.py.

```
python analisador_sintatico.py
```

3. Quando solicitado, insira o nome do arquivo fonte (sem extensão). O arquivo deve estar no mesmo diretório do script principal e ter a extensão .241.

4. O script processará o arquivo e gerará dois relatórios:

   - <nome_do_arquivo>.LEX: Relatório da análise léxica.
   - <nome_do_arquivo>.TAB: Relatório da tabela de símbolos.

### Executando o Projeto pelo Executável

1. Clone o repositório para sua máquina local.

```bash
git clone <URL do repositório>
```

2. Para criar o executável basta instalar a dependência cx_freeze e rodar o comando.

```bash
cd <diretório do projeto>
pip install cx_freeze
py setup.py build
```

3. Execute o script principal analisador_sintatico.exe encontrado dentro do diretório <diretório do projeto>\build\exe.win-amd64-3.12.

4. Quando solicitado, insira o nome do arquivo fonte (sem extensão). O arquivo deve estar no mesmo diretório do script principal e será gerado dentro da pasta do executável e ter a extensão .241, caso não esteja garanta que o arquivo que você quer testar esteja lá.

5. O script processará o arquivo e gerará dois relatórios:

   - <nome_do_arquivo>.LEX: Relatório da análise léxica.
   - <nome_do_arquivo>.TAB: Relatório da tabela de símbolos.

## Detalhes do Código

`analisador_lexico.py`

- Prioriza a identificação de comentários de bloco e linha, seguido por palavras reservadas e variáveis e inicializa a tabela de palavras reservadas.
- Define a função identificar_atom que utiliza expressões regulares para identificar diferentes tipos de átomos no texto fonte.
- Define a função analisar_lexico que percorre o texto fonte, analisando átomos presentes e os trata.

`analisador_sintatico.py`

- Lê o arquivo fonte especificado pelo usuário.
- Realiza a análise léxica utilizando a função `analisar_lexico` do módulo `analisador_lexico`.
- Gera relatórios `.LEX` e `.TAB` contendo detalhes da análise léxica e da tabela de símbolos, respectivamente.

`tabela_simbolos.py`

- Define a estrutura da tabela de símbolos.
- Contém funções para inicializar, adicionar e atualizar símbolos na tabela.

`setup.py`

- Define os padrões de criação do executável do analisador lexico.

## Contribuidores

    - Carlos Henrique Racobaldo Luz Montes
    - Luiz Guilherme Guerreiro Carvalho
    - Maria Eduarda Lopes de Morais Brito
    - Mateus Torres Barreto
