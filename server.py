import socket
import threading
import time

HOST = '0.0.0.0'  # Allow connections from all interfaces on the Pi
PORT = 5000       # Port number

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                print("[Server] Client connection has ended.")
                break
            print(f"[Client] {message.decode()}")
        except:
            print("[Server] Lost connection with client.")
            break

def send_messages(client_socket):
    while True:
        message = input("")
        if message.lower() == 'exit':
            print("[Server] Terminating connection.")
            client_socket.close()
            break
        client_socket.sendall(message.encode())

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print("[Server] Socket creation complete!")
    print(f"[Server] Binding to {HOST}:{PORT}...")
    time.sleep(1)
    
    server_socket.bind((HOST, PORT))
    print(f"[Server] Successfully bound to port {PORT}!")
    
    server_socket.listen(1)
    print("[Server] Waiting for client connection...")

    client_socket, addr = server_socket.accept()
    print(f"[Server] Client connected successfully! Address: {addr}")

    # Separate threads for receiving and sending messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    print("[Server] Shutting down server.")
    server_socket.close()

if __name__ == "__main__":
    main()
