import socket
import time

SECRET_GREETING = "found you"

if __name__ == "__main__":
    greeting_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    greeting_socket.bind(('', 0))
    port_num = greeting_socket.getsockname()[1]
    greeting_socket.listen(1)
    while True:
        connection, addr = greeting_socket.accept()
        data = connection.recv(len(SECRET_GREETING))
        data.rstrip()
        data.lower()
        if SECRET_GREETING in str(data).lower():
            winner = "Aw man how did you know I was hiding on port {0}\n".format(port_num)
            try:
                connection.sendall(winner.encode())
            except:
                print(winner.strip())
            break;
    greeting_socket.close()
