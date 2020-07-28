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
oct4 = 1 + (int(ip[3]))

int_vl700_temp = '''
interface Vlan-interface700
ip address {0:<}.{1:<}.{2:<}.{3:<}  255.255.255.252
'''

print(int_vl700_temp.format(oct1, oct2, oct3, oct4))

oct5 = 1 + (int(oct4))

bgp_tamplate = '''
bgp 64567
undo peer 10.0.0.1
peer {0:<}.{1:<}.{2:<}.{oct5} as-number 65301
peer {0:<}.{1:<}.{2:<}.{oct5} as-path-acl 50 export
peer {0:<}.{1:<}.{2:<}.{oct5} route-policy rm-sp2-out export
peer {0:<}.{1:<}.{2:<}.{oct5} route-policy rm-sp2-in import
peer {0:<}.{1:<}.{2:<}.{oct5} advertise-community
peer {0:<}.{1:<}.{2:<}.{oct5} advertise-ext-community
peer {0:<}.{1:<}.{2:<}.{oct5} fake-as 65524
quit
sa fo
'''

print(bgp_tamplate.format(oct1, oct2, oct3, oct5 = oct5))
