import requests
import json

url = "http://localhost:11434/api/chat"
bdd={}

payload = {
    "model": "qwen3:4b",
    "messages": [
        {"role": "system", "content": "Vous êtes un assistant Administratif."},
        {"role": "user", "content": "génère moi une base de données en .json avec en clé le type de la valeur par exemple nom et en objet la valeur par exemple Jean commences avec pour exemple Jean Dupont qui a 45 ans"}
    ]
}

response = requests.post(url, json=payload, stream=True)

for line in response.iter_lines():
    if line:
        data = json.loads(line)
        print(data.get("message", {}).get("content", ""), end="")
#         test = (data.get("content"))
#         bdd.append(test)
        
# print(bdd)

# print(type(data))
# print(bdd)
# with open("/C:/Users/edoua_itw4d03/Documents/SIO SLAM première année/Mini-Entreprise/Python", "w") as f:
#    json.dump(bdd, f)

#