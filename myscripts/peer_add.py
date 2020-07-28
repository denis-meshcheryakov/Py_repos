#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "peer.py"
#  
network = input('Введите адрес сети с префиксом(Например 10.1.1.0/30):')
ip = network[:network.find('/')]
ip = ip.split('.')
oct1 = int(ip[0])
oct2 = int(ip[1])
oct3 = int(ip[2])
oct4 = int(ip[3])

vlan700 = int(oct4)
vlan700 = vlan700 + 1
peer = vlan700 + 1




bgp_tamplate = '''
bgp 65500
neihbor {}
neihbor1 {}
neihbor2 {}
neihbor3 {}
'''

int_vl700_temp = '''
int vl700
ip addres {0:<}'.'{1:<}'.'{2:<}'.'{vlan700} mask 255.255.255.252
'''

print(int_vl700_temp.format(oct1, oct2, oct3, vlan700))
#print(bgp_tamplate.format(peer))
