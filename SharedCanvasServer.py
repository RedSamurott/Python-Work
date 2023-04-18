# -----------------------------------------------------------------------------
# 
# File Name: SharedCanvasServer.py
#
# Author: Donald Summers, structure authored by Doug Galarus
#
# Description:  A server to run a shared canvas between multiple devices/clients
#               that compiles all the points currently drawn
#
# How to use:   Run it in the terminal with a system arguement, the host's
#               IP address(or localhost if your running it on the same system)
#
# Example use:  python SharedCanvasServer.py localhost
#
# -----------------------------------------------------------------------------
from datetime import datetime
import socket
import threading
import random
import sys

# Maximum size (in bytes) to retrieve from clients
max_size = 1000

# Empty list to hold line endpoints
listLines = []

# Lock for updating list of points
lock = threading.Lock()

# -----------------------------------------------------------------------------
# Function: client_thread
#
# Inputs:
#   client: a socket object that runs whenever a client connects
#
# Return Value:
#   a string that holds either "OK" or a list of points, depending on what
#   request was sent to the server
#
# Example Use:
#   server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   server.bind(address)
#   server.listen(5)
#   client, addr = server.accept()
#   p = threading.Thread(target=client_thread, args=(client,))
#   p.start()
#
# Description:
#   Processes an individual client request and returns a string that will
#   help draw the correct lines on a client's canvas
#
# Exceptions:
#   None
# -----------------------------------------------------------------------------
def client_thread(client):
    # Update the list of endpoints, and allow locking to be used in the function
    global listLines
    global lock
    # Receive the request data (in bytes).
    data = client.recv(max_size)
    #checks for which command is sent in and respond appropriately
    if data.decode("UTF-8") == "Hey!":
        print(f"HELLO: {client}")
        strResponse = "OK"
    if data.decode("UTF-8")[:3] == "ADD":
        lock.acquire()
        currentLine = data.decode("UTF-8")[3:]
        currentLine = currentLine.split()
        for x in currentLine:
            listLines.append(x)
        strResponse = "OK"
        lock.release()
    if data.decode("UTF-8") == "QUIT":
        lock.acquire()
        strResponse = "OK"
        print(f"GOODBYE: {client}")
        lock.release()
    if data.decode("UTF-8") == "GET":
        lock.acquire()
        strResponse = str(int(len(listLines)/4))
        for x in listLines:
            strResponse += f" {x}"
        lock.release()
    if data.decode("UTF-8") == "CLEAR":
        lock.acquire()
        strResponse = "OK"
        listLines = []
        lock.release()
    # Print the time, client information, and the data, decoded as a UTF-8 string.
    print('At', datetime.now(), client, 'said', data.decode("UTF-8"))
    client.sendall(bytes(strResponse, 'utf-8'))
    # Close the connection to the client.
    client.close()

# -----------------------------------------------------------------------------
# Function: main
#
# Inputs:
#   None
#
# Return Value:
#   main does not return anything
#
# Example Use:
#   if __name__ == "__main__":
#   main()
#
# Description:
#   Runs the server by connecting the server to a port on the computer that is free
#   and allows it to run, creates client threads when needed
#
# Exceptions:
#   If the server cannot bind itself to the address/port, say so and shut down
# -----------------------------------------------------------------------------
# main() method
def main():
    
    # Make sure the host argument is passed.
    # The host argument specifies the (local) host.
    # This can be localhost or 127.0.0.1 for the loopback address.
    # Or, it can be the IP address of the local computer. This allows access from other computers.
    if len(sys.argv) != 2:
        print("Usage: python MAGIC8BALL_tcp_server.py host")
        print("host may be localhost or an IP address bound to the local computer you are using.")
        return
    
    # Bind to the host and port and start listening.
    try:
        # Get the host command line argument.
        host = sys.argv[1]
        # Hard-coded port for this application.
        port = 5000
        
        address = (host, port)
        
        print('Starting the Shared Canvas server at:', datetime.now())
        
        # Create a socket.
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind to the address (host, port) combination.
        server.bind(address)
        # Listen for requests. Allow a "backlog" of 5, meaning roughly 5 simultaneous connections allowed.
        server.listen(5)
    # If an exception occurred in binding or initially trying to listen, print an error message and exit.
    except:
        print("An error occurred when attempting to bind to the address and port.")
        return
    
    # Now wait for client requests.
    print('Waiting for clients to make requests.')
    while True:
        # Block and wait for a client request.
        client, addr = server.accept()
        # Create and start a new client_thread to handle the request.
        p = threading.Thread(target=client_thread, args=(client,))
        p.start()
    
    # Close the server.
    # This line will not be reached, because there is no mechanism to exit the infinite loop above.
    server.close()


# Call the main function when invoked.
if __name__ == "__main__":
    main()
