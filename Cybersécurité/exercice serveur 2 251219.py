"""
Exercice 2 : client interactif
Créer un client capable de gérer sa propre configuration (hôte et 
port) et son état de connexion, permettant l'envoi de messages 
via la console utilisateur.


• Définissez les variables par défaut HOST ('127.0.0.1') et PORT 
(4242), ainsi qu'une variable d'état connected (False).


• Créez une boucle while True qui lit les entrées de l'utilisateur 
(input()).


• Implémentez la reconnaissance des commandes spéciales (si 
l'entrée commence par \): 


• \host <ip> : Met à jour la variable HOST.


• \port <num> : Met à jour la variable PORT.


• \connect : Tente de créer et d'établir une connexion TCP avec le 
serveur configuré. Mettez à jour connected en cas de succès.


• \close : Ferme la connexion et remet connected à False.


• Envoi de Messages : Si l'utilisateur est connected et que 
l'entrée n'est pas une commande, encodez le message en utf
8 et envoyez-le au serveur. Affichez la réponse décodée du 
serveur.


"""
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.0.1"
PORT = "4242"

connected = False

while True:
    cmd = input(">")
    if cmd == "\\close":
        client.close()
        connected = False
        break

    elif cmd == "\\host":
        ip = input("Donnez une adresse IP")
        HOST = ip

    elif cmd == "\\port":
        tcp = input(int("Donnez un PORT"))
        PORT = tcp
    elif cmd == "\\connect":
        client.connect((HOST, PORT))
        connected = True
        client.send(b"Hello")
        data = client.recv(1024)
        print("Serveur : ", data.decode("utf-8"))



    else:
        message = input()
        client.send(message.encode('utf-8'))