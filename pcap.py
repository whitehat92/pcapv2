"""
DISCLAIMER: as always, please don't judge my code. You were once a learner as well
"""


from scapy.all import *
from scapy.utils import *
# -*- coding: utf-16 -*-

import dpkt

#f = open(sys.argv[1], "r")
#text = f.read()
timeprompt = str(input("Do you want to print with time? (Y/N): "))
if timeprompt == "Y" or timeprompt == "y" or timeprompt == "":

    pcap = rdpcap('<filetoimport.pcap')
    s = pcap.sessions()
    print("------- SUMMARY OF CAPTURE ------")
    print(pcap.summary)
    print("------- SESSIONS --------")
    for a in s.items():
        print(a)
    print("-------- TIME ----------")
    for b, c in s.items():
        for x in c:
            print(x.time, b)
    #GSM
    #for x in s.items():
     #   print(x.filter("gsm_sms"))
#possibly UDP packet?
    hexprompt = str(input("Also wanna print hexdump? "))
    if hexprompt == "y":
        print(pcap.hexdump())
    #if "UDP" in str(pcap.sessions()):
        #tcpprompt = str(input("Found some TCP packets on file, print them? "))
        #if tcpprompt == "y":
         #   print(pcap.sessions(UDP_SERVICES(Raw)))


else:
    pcap = rdpcap('26_to_40_2019-06-04_09-08-27UTC.pcap')
    s = pcap.sessions()
    print("------- SUMMARY OF CAPTURE ------")
    print(pcap.summary)
    print("------- SESSIONS --------")
    print(s)
    for a in s.items():
        print(a)
    #udpacket = pcap.ls(UDP)
    #print(udpacket)
    hexprompt = str(input("Also wanna print hexdump? "))
    if hexprompt == "y":
        print(pcap.hexdump())
    for sessions in pcap.sessions():
        print(sessions(raw))
