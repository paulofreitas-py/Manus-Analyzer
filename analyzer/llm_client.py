import openai

def analyze_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um especialista em engenharia de software."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )
    return response['choices'][0]['message']['content']
