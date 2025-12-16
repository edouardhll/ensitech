import ollama
import json

response = ollama.chat(
    model="qwen3:4b",
    messages=[
        {"role": "system", "content": "Vous êtes un assistant Administratif. Fais juste ton travail, pas de plus"},
        {"role": "user", "content": "Réponds UNIQUEMENT avec un JSON valide. Génère un objet représentant Jean Dupont, 45 ans."}
    ]
)

content = response['message']['content']

data = json.loads(content)



with open("bdd.json", "w") as f:
    json.dump(data, f, indent=4)
print(f"Json enregistré : {data}")