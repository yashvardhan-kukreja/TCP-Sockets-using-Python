import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname(socket.gethostname())
port = 2324

address = (ip, port)

server.bind(address)
server.listen(1)
print("Server listening at connection " + ip + ":" + str(port))

client, addr = server.accept()
print("Connection from " + addr[0] + ":" + str(addr[1]))

while True:
    data = client.recv(1024).decode("utf-8")
    print("Message from client: " + data)
    message = input("Enter a message: ")
    client.send(str.encode(message))
    if message == "bye" or message == "Bye" or data == "bye" or data == "Bye":
        client.close()
        break