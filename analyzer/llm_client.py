import openai

def analyze_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Certifique-se de usar o modelo correto
        messages=[
            {"role": "system", "content": "Você é um assistente técnico."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
