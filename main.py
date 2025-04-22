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


Com base nessa estrutura, gere um relatório técnico com os seguintes tópicos:

1. Estrutura do Projeto
2. Stack Tecnológica
3. Arquitetura do Sistema
4. Fluxo de Dados e Estado
5. Persistência de Dados
6. Segurança
7. Testes Automatizados
8. DevOps e Deploy
9. Monitoramento e Performance
10. Documentação
11. APIs e Integrações
12. Resumo Geral

O resultado deve ser em Markdown e bem estruturado.
"""

# Envia para a API da OpenAI
def analyze_project_with_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um especialista em engenharia de software."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )
    return response['choices'][0]['message']['content']

# Execução
if __name__ == "__main__":
    print("[🔍] Lendo estrutura do projeto...")
    structure = get_project_structure(project_path)
    prompt = generate_prompt(structure)

    print("[🤖] Enviando para análise com LLM...")
    report = analyze_project_with_llm(prompt)

    # Salva o relatório
    output_file = "relatorio_tecnico.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"[✅] Relatório gerado com sucesso: {output_file}")
