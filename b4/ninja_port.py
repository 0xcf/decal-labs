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
            print("Aw man how did you know I was hiding on port {0}".format(port_num))
            break;
    greeting_socket.close()
