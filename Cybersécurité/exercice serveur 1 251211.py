"""
Exercice 1 : serveur
Créer un serveur TCP simple capable de recevoir une
connexion, de traiter un message, puis de se déconnecter.

• Importez le module socket.
OK

• Définissez l'adresse HOST sur '127.0.0.1' et le PORT sur 
4242.
OK

• Créez un socket en utilisant socket.AF_INET et
socket.SOCK_STREAM.
OK

• Liez (bind) le socket à l'adresse et au port, puis mettez-le
en mode écoute (listen).
(ok)


• Utilisez server.accept() pour accepter la connexion du
client et obtenir le socket client.
(ok)

• Recevez un maximum de 1024 octets de données.
N'oubliez pas de décoder (decode) les octets reçus en
utilisant utf-8 pour obtenir un message lisible.
(ok je crois)


• Fermez les sockets (client.close() et server.close()) pour
terminer le programme proprement.


"""

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 4242))
server.listen()
print("serveur en attente")

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



try:
    client, addr = server.accept()
    print(f"client : {client}")
    print(f"addresse : {addr}")
    #client.connect(("127.0.0.1", 4242))
    data = client.recv(1024)
    data = data.decode("utf-8")
    print(f"data : {data}")
    message = ("bonjour \n")
    client.send(message.encode('utf-8'))
    print("connection")
except socket.timeout:
    print("erreur")
except socket.error as e:
    print("erreur")

reponse_bytes = client.recv(1024)
message_texte = reponse_bytes.decode("utf-8")
print(message_texte)

client.close()
server.close()
