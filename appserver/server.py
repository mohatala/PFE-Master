import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Bind the socket to a public host and a well-known port
server_socket.bind((host, 8000))

# Listen for incoming connections
server_socket.listen(1)

while True:
    # Wait for a client to connect
    client_socket, addr = server_socket.accept()

    # Receive the data sent by the client
    question = client_socket.recv(1024)
    print(question)
    # Process the question and send back an answer
    answer = "This is the answer to your question: " + question.decode()
    client_socket.send(answer.encode())

    # Close the connection with the client
    client_socket.close()
