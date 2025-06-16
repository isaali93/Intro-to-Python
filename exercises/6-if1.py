'''
Working with a if statements

Let's assume that we have a program that checks to see if a remote computer is online
and if it is online, print it the port and hostname

I've given you 3 varibles and the framework for the if statement.

  1. Read the code and finish the if statement.
  2. Add an if statement that prints the name port name based on the target_port number:
    a. 80 - HTTP
    b. 443 - HTTPS
    c. 502 - MODBUS
    d. 3389 - RDP
    e. 6667 - IRC
'''

target_online = False
target_port = 3389
target_name = "example.org"

if target_online:
  # code to execute
