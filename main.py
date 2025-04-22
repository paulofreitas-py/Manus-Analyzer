import os
import openai

# Configuração da API
openai.api_key = os.getenv("OPENAI_API_KEY")  # ou defina diretamente aqui

# Caminho para o projeto
project_path = "/caminho/para/seu/projeto"  # troque para seu caminho local

# Função para ler estrutura de arquivos
def get_project_structure(path):
    structure = ""
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = '  ' * level
        structure += f"{indent}- {os.path.basename(root)}/\n"
        subindent = '  ' * (level + 1)
        for f in files:
            structure += f"{subindent}- {f}\n"
    return structure

# Prompt técnico baseado na estrutura e análise do código
def generate_prompt(project_structure):
    return f"""
Você é um engenheiro de software sênior. Abaixo está a estrutura do projeto:

