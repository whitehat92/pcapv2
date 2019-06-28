"""
DISCLAIMER: as always, please don't judge my code. You were once a learner as well
"""
# -*- coding: utf-8 -*-
from scapy.all import *
import sys
import time
from scapy.utils import RawPcapReader
import argparse

lerpcap = str(sys.argv[1])
timeprompt = str(input("Do you want to print with time? (Y/N): "))
if timeprompt == "Y" or timeprompt == "y" or timeprompt == "":
    pcap = rdpcap(lerpcap)
    s = pcap.sessions()
    print("------- SUMMARY OF CAPTURE ------")
    print(pcap.summary)
    print("------- SESSIONS --------")
    for a in s.items():
        print(a)
    print("-------- TIME ----------")
    for a, variables in s.items():
        for tm in variables:
            opentime = time.strftime('%A, %d/%m/%y, %I:%M:%S %p', time.localtime(tm.time))
            print(opentime, a)
    hexprompt = str(input("Also wanna print hexdump? "))
    if hexprompt == "y":
        print(pcap.hexdump())
else:
    pcap = rdpcap(lerpcap)
    s = pcap.sessions()
    print("------- SUMMARY OF CAPTURE ------")
    print(pcap.summary)
    print("------- SESSIONS --------")
    print(s)
    for a in s.items():
        print(a)
    hexprompt = str(input("Also wanna print hexdump? "))
    if hexprompt == "y":
        print(pcap.hexdump())
