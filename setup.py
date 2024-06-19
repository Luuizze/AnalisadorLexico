from cx_Freeze import setup, Executable

executables = [
    Executable('analisador_sintatico.py', base="Console")
]

setup(
    name="Nikoboko2024-1",
    version="1.0",
    description="Analisador Léxico da Linguagem NikoBoko2024-1",
    executables=executables,
    options={
        "build_exe": {
            "packages": ["re", "sys", "time"],  # Lista de pacotes a incluir
            "include_files": ["teste.241", "tabela_simbolos.py", "analisador_lexico.py"],  # Arquivos adicionais a incluir
        },
    },
)
