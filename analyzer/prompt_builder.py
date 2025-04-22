def generate_prompt(project_structure):
    return f"""
Você é um engenheiro de software sênior. Abaixo está a estrutura do projeto:

{project_structure}

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
