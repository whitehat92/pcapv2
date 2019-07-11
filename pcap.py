"""
DISCLAIMER: as always, please don't judge my code. You were once a learner as well
"""
# -*- coding: utf-8 -*-
from scapy.all import *
import sys
import time
from scapy.utils import RawPcapReader

lerpcap = str(sys.argv[1])
timeprompt = str(input("Do you want to print with time? (Y/N): "))
if timeprompt == "Y" or timeprompt == "y" or timeprompt == "":
    pcap = rdpcap(lerpcap)
    s = pcap.sessions()
    print("-----------------------------------| SUMMARY OF CAPTURE |---------------------------------------------")
    print(pcap.summary)
    print("------------------------------------------| SESSIONS por inteiro |--------------------------------------")
    for b in s.items():
         print(b)
    print("SESSOES MODIFICADAS")
    for b in s.items():
        print(b[0])
    print(("SESSOES OUTRAS MODIFICADAS"))
    for b in s.items():
        print("ARP SESSIONS")
        print(pcap[ARP])
        print("UDP SESSIONS")
        print(pcap[UDP])
        print("ANALISE MAIS COMPLETA DOS PACOTES")
        print(pcap[UDP][0].show())
        print("POSICAO 2 NO PAYLOAD DO PACOTE UDP")
        print(pcap[UDP][1].show())
        print("---------------------OUTRAS POSICOES ---------------------------------------")
        load_layer('tls')
        #print(TLS(pcap[UDP][0]))
        print(pcap[UDP][0].show(packet))
        #print("PAYLOAD DO PROTOCOLO RRC")
        #print(pcap[GSM_SMS].show())

        #print("MOSTRAR PAYLOAD DOS PACOTES TCP")
        #print(pcap[TCP][0].show())


        """
                self._debug('PAYLOAD LENGTH {0}'.format(len(load)),
                            no_prefix=True)
                self._debug(load, load=True)
                self._parse_load(load)
            except AttributeError:
                self._debug('LOAD EXCEPTION', no_prefix=True)
        if len(self.messages) > 0 and not self.messages[-1].write_closed:
            self._debug('DELETE LAST OPEN FILE')
            del self.messages[-1]

        if self.args.debug_analysis:
            sys.exit(0)
        """

        """
        print(pcap[UDP].sessions())
        
        print("SSL SESSIONS")
        print(pcap[SSL])
    """
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

