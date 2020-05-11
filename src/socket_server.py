import socket
import threading
import random

from Definitions import *

# Wait for new connections and if connected, then start for each client a new ClientThread
def newConnectionsHandler(self,socket):
    while True:
        conn, address = socket.accept()
        self.connections.append(ClientThread(conn, address, self.total_connections, "Name", True))
        self.connections[len(self.connections) - 1].start()
        print("New connection at ID " + str(self.connections[len(self.connections) - 1]))
        self.total_connections += 1

# The class object for the overall socket server which starts the newConnectionsHandler thread
class RFAMPServer():

    # Variables for holding information about connections
    connections = []
    total_connections = 0
    newConnectionsThread = []

    def __init__(self):
        # Get host and port
        host = 'localhost'
        port = connect_port

        # Create new server socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(5)

        # Create new thread to wait for connections
        newConnectionsThread = threading.Thread(target=newConnectionsHandler, args=(self,sock,))
        newConnectionsThread.start()


# For each client a new thread is started / instance created to handle the requests.
class ClientThread(threading.Thread):
    def __init__(self, conn, address, id, name, activeFlag):
        threading.Thread.__init__(self)
        self.conn = conn
        self.address = address
        self.id = id
        self.name = name
        self.activeFlag = activeFlag

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    # The implementation of the thread's run function call
    def run(self):
        while self.activeFlag:
            try:
                data = self.conn.recv(32)
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.activeFlag = False
                connections.remove(self)
                self.conn.close()
                break

            # disconnected client detected
            if not data:
                print("Client " + str(self.address) + " has disconnected")
                self.activeFlag = False
                connections.remove(self)
                self.conn.close()
                break

            # client data is there, then process it...
            if data != "":
                try:
                    data_str = data.decode('utf8')
                except:
                    print("got UTF-8 decode exception")
                    data_str = "undef cmd"
                    data = None

                # server implementation for the various commands
                if data_str.startswith('ver'):
                    answer_str = 'Version: ' + VERSION_TAG + '\n'
                elif data_str.startswith('?'):
                    Pfwd=random.uniform(0.0,3.0)
                    answer_str = 'Pfwd=%3.1f\n' % Pfwd
                else:
                    answer_str = 'undef cmd' + '\n'

                # send answer back to client
                answer = bytearray(answer_str, 'utf8')
                self.conn.sendall(answer)



if __name__ == "__main__":
    print("trying to start RFAMPServer")
    myserver = RFAMPServer()
    print("started")
