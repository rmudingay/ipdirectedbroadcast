#!/usr/bin/python
import sys
import socket
import multiprocessing
from time import sleep
import time

# directed broadcast settings
bcAddress = ["192.168.1.255","192.168.2.255"] # L3 directed broadcasts addresses
bcPort    = 5064                              # udp destination port to use
bcCount   = 10000000                          # how many datagrams shall we send
bcRate    = 14                                # Herz (Rate)
bcSize    = 80                                # bytes (payload for udp segment)

def sendUDP(myAddress):
        """Send UDP datagram"""
        b = multiprocessing.current_process()
       # assemble payload see bcSize
        payload = ""
        for x in range(0,bcSize):
                payload += "X"
        s = time.time()
        # WTF, numerator MUST be float to get a float
        rateS = 1/float(bcRate)
        print("Sending " + str(bcCount) + " UDP segments to " + str(SVI) + ":" + str(bcPort) + " PID(" + str(b.pid) + ") every " + str(rateS) + "s")
        # create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        #send at specified rate
        for x in range(bcCount):
                sock.sendto(str(payload),(myAddress,bcPort))
                sleep(rateS)

for SVI in bcAddress:
        p = multiprocessing.Process(target=sendUDP, args=(SVI,)).start()
