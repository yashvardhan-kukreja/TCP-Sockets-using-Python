import socket
client = socket.socket()
ip = socket.gethostbyname(socket.gethostname())
port = 2324

address = (ip, port)

client.connect(address)

while True:
    message = input("Enter some message: ")
    client.send(str.encode(message))
    data = client.recv(1024).decode("utf-8")
    print("Message from server: " + data)
    if message == "bye" or message == "Bye" or data == "bye" or data == "Bye":
        client.close()
        break
