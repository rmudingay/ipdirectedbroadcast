#!/usr/bin/python
# 
# This file is part of the ipdirectedbroadcast script (https://github.com/rmudingay/ipdirectedbroadcast).
# Copyright (c) European Spallation Source ERIC.
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import socket
import multiprocessing
from time import sleep
import time

broadcast_addr = sys.argv
# directed broadcast settings
bcAddress = broadcast_addr                    # L3 directed broadcasts addresses
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
