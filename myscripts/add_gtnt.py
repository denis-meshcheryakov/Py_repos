#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "add_gtnt.py"
#  
network = input('Введите адрес сети с префиксом(Например 10.1.1.0/30):')
number_of_mag = input('Введите номер магазина')
ip = network[:network.find('/')]
net_ip = ip
ip = ip.split('.')
oct1 = int(ip[0])
oct2 = int(ip[1])
oct3 = int(ip[2])
oct4 = 1 + (int(ip[3]))
oct5 = 1 + (int(oct4))
ce_ip = [str(oct1), str(oct2), str(oct3), str(oct4)]
ce_ip = '.'.join(ce_ip)
pe_ip = [str(oct1), str(oct2), str(oct3), str(oct5)]
pe_ip = '.'.join(pe_ip)

src_file = 'rt-{}.hp-msr930.txt'.format(number_of_mag)
dest_file = 'rt-{}.hp-msr930-gtnt.txt'.format(number_of_mag)

src = open(src_file)
src_list = src.readlines()
src.close()

item1 = 'ip address {} 255.255.255.252\n'.format(pe_ip)
item2 = 'peer {} as-number 65301\n'.format(ce_ip)
item3 = 'peer {} as-path-acl 50 export\n'.format(ce_ip)
item4 = 'peer {} route-policy rm-sp2-out export\n'.format(ce_ip)
item5 = 'peer {} route-policy rm-sp2-in import\n'.format(ce_ip)
item6 = 'peer {} advertise-community\n'.format(ce_ip)
item7 = 'peer {} advertise-ext-community\n'.format(ce_ip)
item8 = 'peer {} fake-as 65524\n'.format(ce_ip)

src_list.pop(218)
src_list.insert(218, item1)
src_list.pop(255)
src_list.insert(255, item2)
src_list.pop(256)
src_list.insert(256, item3)
src_list.pop(257)
src_list.insert(257, item4)
src_list.pop(258)
src_list.insert(258, item5)
src_list.pop(259)
src_list.insert(259, item6)
src_list.pop(260)
src_list.insert(260, item7)
src_list.pop(261)
src_list.insert(261, item8)
    
dest = open(dest_file, 'w')
dest.writelines(src_list)
dest.close()
