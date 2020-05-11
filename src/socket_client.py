import socket
import threading
import time
import sys

from argparse import ArgumentParser

from Definitions import *

# For each client a new thread is started / instance created to handle the requests.
class RFAMPClient(threading.Thread):
    # Class variables
    host = ""
    loop_cnt = 0
    client_sock = ()

    # constructor
    def __init__(self, host):
        self.host = host

        # Create a TCP/IP socket
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        #print("connecting to " + host + ":" + str(connect_port)
        self.client_sock.connect((host, int(connect_port)))

        # query this once
        message = 'ver'
        data = self.do_query(message)
        print(message + " -> " + data)

        # init thread
        threading.Thread.__init__(self)

    def __str__(self):
        return str(self.host)

    # The implementation of the thread's run function call
    def run(self):
        while 1:
            message = '?'
            data = self.do_query(message)
            print(message + " -> " + data)

            #print("iteration: " + str(self.loop_cnt))
            self.loop_cnt = self.loop_cnt + 1
            time.sleep(0.1)

    def do_query(self, cmd):
        self.client_sock.sendall(bytearray(cmd, 'utf8'))
        data = self.client_sock.recv(1024)
        return str(data)


if __name__ == "__main__":

    # parse command line argument
    parser = ArgumentParser()
    parser.add_argument("--connect", dest="connect_host",
                        help="UI can connect to localhost (default) or a remote host. The localhost default is typically the UI which is physically connected via GPIO to the amplifier controller.",
                        default="localhost",
                        required=False)
    args = parser.parse_args()

    print("Start RFAMPClient and connecting to " + args.connect_host)
    myclient = RFAMPClient(args.connect_host)
    myclient.start()

    while 1:
        time.sleep(3)
        #print("client still alive... check in another 3 seconds")


    print("finished")
