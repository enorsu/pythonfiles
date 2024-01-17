import http.server
import socketserver
import os
# imports

# Made by SotaNorsu

# port if port.txt is not found
standard = 8000

# add the command that shows your ip address
# linux command
ipadd = "hostname -I"

# port file name
port_file_name = "port.txt"

print("made by (github) SotaNorsu\n")


# here we will check if "port.txt" exists
try:
    
    portfile = open(port_file_name, "") # opens the "port.txt" file if it does not exist gives an error
    
    port = int(portfile.read())  # sets the port to port.txt
except:
    print("port.txt file not found or empty")

    
    print("creating port.txt with 8000")
    
    portfile = open("port.txt", "w") # open the port.txt
    
    portfile.write(str(standard)) # write the standard port
    
    port = int(portfile.read()) # set the port to the port.txt



handler = http.server.SimpleHTTPRequestHandler # the handler

with socketserver.TCPServer(("", port), handler) as httpd: #start the server
    os.system(ipadd) # ip address

    print("serving files at " + str(port))

    httpd.serve_forever() # serve files until closed