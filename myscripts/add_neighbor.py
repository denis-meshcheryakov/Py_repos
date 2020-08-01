#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "add_neighbor.py"
#  
network = input('Введите адрес сети с префиксом(Например 10.1.1.0/30):')
ip = network[:network.find('/')]
ip = ip.split('.')
oct1 = int(ip[0])
oct2 = int(ip[1])
oct3 = int(ip[2])
oct4 = 1 + (int(ip[3]))
oct5 = 1 + (int(oct4))

int_vl700_temp = '''
interface vlan 700
ip address {0:<}.{1:<}.{2:<}.{3:<}  255.255.255.252
'''

print(int_vl700_temp.format(oct1, oct2, oct3, oct5))


bgp_tamplate = '''
router bgp 64567
no neighbor 10.0.0.1
neighbor {0:<}.{1:<}.{2:<}.{oct4} remote-as 65301
neighbor {0:<}.{1:<}.{2:<}.{oct4} local-as 65524
neighbor {0:<}.{1:<}.{2:<}.{oct4} route-map rm-sp2-in in
neighbor {0:<}.{1:<}.{2:<}.{oct4} route-map rm-sp2-out out
neighbor {0:<}.{1:<}.{2:<}.{oct4} filter-list 50 out
neighbor {0:<}.{1:<}.{2:<}.{oct4} send-community both
neighbor {0:<}.{1:<}.{2:<}.{oct4} soft-reconfiguration inbound

end
wr
'''

print(bgp_tamplate.format(oct1, oct2, oct3, oct4 = oct4))
