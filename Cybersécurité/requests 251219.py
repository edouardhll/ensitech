import requests

url = "https://pokeapi.co/api/v2/pokemon"
response = requests.get(url)

print(f"Code de statur : {response.status_code}")
print(f"Type de contenu : {response.headers.get('Content-Type')}")

if response.status_code == 200:
    print("--- Contenu JSON reçu")
    print(response.json())