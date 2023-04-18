# -----------------------------------------------------------------------------
# 
# File Name: SharedCanvasClient.py
#
# Author: Donald Summers, structure authored by Doug Galarus
#
# Description:  A client that runs in tandum with the SharedCanvasServer,
#               processes all the drawing tools sent to the server and displays
#               the current shared canvas
#
# How to use:   Run it in the terminal with a system arguement, the host's
#               IP address(or localhost if your running it on the same system)
#
# Example use:  python SharedCanvasClient.py localhost
#
# -----------------------------------------------------------------------------

import socket
from datetime import datetime
import sys
import stddraw

#Gets the necessary data to make a connection to the server
host = sys.argv[1]
port = 5000
max_size = 1000

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
#   Runs the client by connecting to the server and allows for the drawing
#   capabilities for the canvas/drawing portion, sends requests to the server
#   when client needs them
#
# Exceptions:
#   None
# -----------------------------------------------------------------------------
# main() method
def main():
    #sends a very specific request to the server side to welcome the client
    response = sendCommand("Hey!")
    # Boolean flag to track clicks for line-drawing.
    # If True, the next click will define the start of a line segment.
    # If False, the next click will define the end of a line segment.
    startNewLine = True
    # Starting coordinates for line segment
    startX = 0.0
    startY = 0.0
    
    # End coordinates for line segment
    endX = 0.0
    endY = 0.0

    # Clear/initialize the stddraw window.
    stddraw.clear()
    
    # Set the pen color to black.
    stddraw.setPenColor(stddraw.BLACK)
    
    # Print simple instructions.
    print('------------------------------------------------------------------')
    print('Single User Canvas')
    print('------------------------------------------------------------------')
    print('Click the mouse to draw lines. The first click chooses the start,')
    print('the second chooses the end and draws the line segment on the canvas.')
    print('Type c to clear the canvas.')
    print('Type q to quit and exit the program.')
    print('------------------------------------------------------------------')
    
    # Infinite loop to process events.
    while True:
        # Check for mouse press/click.
        if stddraw.mousePressed():
            # Draw a point to show the user where the click was.
            stddraw.filledCircle(stddraw.mouseX(), stddraw.mouseY(), .005)
            # Handle case where mouse click indicates end of line.
            if startNewLine == False:
                # Get the end coordinates.
                endX = stddraw.mouseX()
                endY = stddraw.mouseY()
                # Draw the line segment.
                stddraw.line(startX, startY, endX, endY)
                #sends "ADD" request to server to add line endpoints to drawing
                sendingMessage = f"ADD {startX} {startY} {endX} {endY}"
                response = sendCommand(sendingMessage)
                # Set flag to start new line on next mouse click.
                startNewLine = True
            # Handle case where mouse click indicates start of line.
            else:
                # Get the start coordinates.
                startX = stddraw.mouseX()
                startY = stddraw.mouseY()
                # Set flag to end line on next mouse click.
                startNewLine = False
        # Check for key press.
        if stddraw.hasNextKeyTyped():
            # Retrieve the character.
            ch = stddraw.nextKeyTyped()
            # If it is a c, clear the canvas.
            if ch == 'c':
                #sends "CLEAR" request to server to clear the list of points
                response = sendCommand("CLEAR")
                stddraw.clear()
            # If it is a q, then quit the infinite loop via break.
            if ch == 'q':
                #sends "QUIT" request to server to send a goodbye message
                response = sendCommand("QUIT")
                break
        # Show with 100 ms delay. The value could be decreased to be more responsive.
        #Also sends "GET" request to server to constantly update the client's current canvas
        response = sendCommand("GET")
        if response != "OK":
            response = response.split()
            stddraw.clear()
            for x in range(0, int(response[0])):
                stddraw.line(float(response[4*x+1]), float(response[4*x+2]), float(response[4*x+3]), float(response[4*x+4]))
        stddraw.show(100)
    # Print exit message.
    print("Exiting Single User Canvas")

# -----------------------------------------------------------------------------
# Function: sendCommand
#
# Inputs:
#   strCommand: a string of a command that is sent to the server to be processed
#
# Return Value:
#   strResponse: a string that contains either "OK" or a list of points
#
# Example Use:
#   response = sendCommand("GET")
#
# Description:
#   Holds the command sending of the client, connects to the server when it needs
#   to, and shuts the connection down once it is through processing the request
#
# Exceptions:
#   If the client cannot connect to the server with the address/port, say so and close
#   If the client gets an error when sending a request,, say so and close connection
# -----------------------------------------------------------------------------
def sendCommand(strCommand):
    global host
    global port
    global max_size

    try:
        address = (host, port)
        
        # Create a socket.
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Try to connect to the server.
        client.connect(address)
        
    # If an exception occurred in binding or initially trying to connect, print an error message and exit.
    except:
        print("An error occurred when attempting to connect to the server at the given address and port.")
        return

    try:
        #try sending a request to the server and close once processed
        client.sendall(bytes(strCommand, "UTF-8"))
        data = client.recv(max_size)
        strResponse = data.decode("UTF-8")
        client.close()

        return strResponse

    except:
        print("An error occurred when making a request to the server.")
        # Close the connection to the server.
        client.close()
        return

#-----------------------------------------------------------------------

# Call the main function when invoked.
if __name__ == '__main__':
    main()
