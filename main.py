import argparse
import os
from analyzer.project_reader import get_project_structure
from analyzer.prompt_builder import generate_prompt
from analyzer.llm_client import analyze_with_openai

def main():
    parser = argparse.ArgumentParser(description="Analisador de Projeto com LLM")
    parser.add_argument("project_path", help="Caminho para o projeto")
    parser.add_argument("-o", "--output", default="relatorio_tecnico.md", help="Arquivo de saída")
    args = parser.parse_args()

    print("[🔍] Lendo estrutura do projeto...")
    structure = get_project_structure(args.project_path)
    prompt = generate_prompt(structure)

    print("[🤖] Enviando para LLM...")
    report = analyze_with_openai(prompt)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"[✅] Relatório salvo em: {args.output}")

if __name__ == "__main__":
    main()
