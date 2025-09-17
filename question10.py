# =============================================================================
# Question 10: Client-Server Socket Programming
# =============================================================================

import socket

class SimpleServer:
    """Simple TCP server implementation."""
    
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.socket = None
    
    def start_server(self):
        """Start the server and listen for connections."""
        try:
            # Create socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Bind to address
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            
            print(f"Server listening on {self.host}:{self.port}")
            
            # Accept connection
            client_socket, client_address = self.socket.accept()
            print(f"Connection from {client_address}")
            
            # Send message
            message = "Hello from server!"
            client_socket.send(message.encode('utf-8'))
            print(f"Sent: {message}")
            
            client_socket.close()
            
        except socket.error as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            if self.socket:
                self.socket.close()


class SimpleClient:
    """Simple TCP client implementation."""
    
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
    
    def connect_to_server(self):
        """Connect to server and receive message."""
        try:
            # Create socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to server
            client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
            
            # Receive message
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {message}")
            
            client_socket.close()
            return message
            
        except socket.error as e:
            print(f"Connection error: {e}")
            return None
        except Exception as e:
            print(f"Client error: {e}")
            return None


def socket_demo():
    """
    Demonstrate client-server communication.
    Note: In a real scenario, you'd run server and client in separate processes.
    """
    print("Socket Programming Demo:")
    print("-" * 25)
    print("Note: This demo shows the code structure.")
    print("In practice, run server and client in separate terminals/processes.")
    
    # Show how to create and use server
    server = SimpleServer()
    print(f"Server created for {server.host}:{server.port}")
    
    # Show how to create and use client
    client = SimpleClient()
    print(f"Client created to connect to {client.host}:{client.port}")
