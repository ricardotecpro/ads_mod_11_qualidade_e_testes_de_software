import os
import shutil

base_dir = r"d:\SourceCode\REPOS\github.io\ads_mod_02_logica_e_algoritmos\docs\aulas"

mapping = {
    "01_conteudo_do_curso.md": "aula-01.md",
    "02_introducao_a_programacao.md": "aula-02.md",
    "03_estrutura_sequencial.md": "aula-03.md",
    "04_estrutura_condicional.md": "aula-04.md",
    "05_estruturas_repetitivas.md": "aula-05.md",
    "06_vetores.md": "aula-06.md",
    "07_matrizes.md": "aula-07.md",
    "08_funcoes.md": "aula-08.md",
    "09_linguagem_c.md": "aula-09.md",
    "10_linguagem_cpp.md": "aula-10.md",
    "11_linguagem_java.md": "aula-11.md",
    "12_linguagem_csharp.md": "aula-12.md",
    "13_linguagem_python.md": "aula-13.md",
    "14_linguagem_javascript.md": "aula-14.md",
    "15_linguagem_rust.md": "aula-15.md",
    "16_linguagem_dart.md": "aula-16.md"
}

for old_name, new_name in mapping.items():
    old_path = os.path.join(base_dir, old_name)
    new_path = os.path.join(base_dir, new_name)
    
    if os.path.exists(old_path):
        try:
            os.rename(old_path, new_path)
            print(f"Renamed {old_name} to {new_name}")
        except Exception as e:
            print(f"Error renaming {old_name}: {e}")
    else:
        print(f"File not found: {old_name}")

# Move installation tools file to setups
tools_file = os.path.join(base_dir, "08_instalacao_ferramentas.md")
setup_dir = r"d:\SourceCode\REPOS\github.io\ads_mod_02_logica_e_algoritmos\docs\setups"
setup_target = os.path.join(setup_dir, "setup-global.md")

if os.path.exists(tools_file):
    try:
        shutil.move(tools_file, setup_target)
        print(f"Moved 08_instalacao_ferramentas.md to {setup_target}")
    except Exception as e:
        print(f"Error moving tools file: {e}")
else:
    print("file 08_instalacao_ferramentas.md not found")
