import socket
import re
import time
ip = '127.0.0.1'
port = 20321
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))
while True:
    #time.sleep(0.02)
    data, address = sock.recvfrom(1024)
    m = re.search('ResultCode (.)', data)
    if m:
        a = m.group(0)
        print a