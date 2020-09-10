#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "add_gtnt.py"
#  
network = input('Введите адрес сети с префиксом(Например 10.1.1.0/30):')
number_of_mag = input('Введите номер магазина: ')
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

src_file_930 = '/var/share/config/rt-{}.hp-msr930.txt'.format(number_of_mag)
dest_file_930 = '/var/share/config/rt-{}.hp-msr930-gtnt.txt'.format(number_of_mag)
src_file_880 = '/var/share/config/rt-{}.cisco-880.txt'.format(number_of_mag)
dest_file_880 = '/var/share/config/rt-{}.cisco-880.txt'.format(number_of_mag)
src_file_2800 = '/var/share/config/rt-{}.cisco-2800-gtnt.txt'.format(number_of_mag)
dest_file_2800 = '/var/share/config/rt-{}.cisco-2800-gtnt.txt'.format(number_of_mag)

src_930 = open(src_file_930)
src_list_930 = src_930.readlines()
src_930.close()
src_880 = open(src_file_880)
src_list_880 = src_880.readlines()
src_880.close()
src_2800 = open(src_file_2800)
src_list_2800 = src_2800.readlines()
src_2800.close()

item_int_vl_700 = 'ip address {} 255.255.255.252\n'.format(pe_ip)

# MSR-930
item_930_1 = 'peer {} as-number 65301\n'.format(ce_ip)
item_930_2 = 'peer {} as-path-acl 50 export\n'.format(ce_ip)
item_930_3 = 'peer {} route-policy rm-sp2-out export\n'.format(ce_ip)
item_930_4 = 'peer {} route-policy rm-sp2-in import\n'.format(ce_ip)
item_930_5 = 'peer {} advertise-community\n'.format(ce_ip)
item_930_6 = 'peer {} advertise-ext-community\n'.format(ce_ip)
item_930_7 = 'peer {} fake-as 65524\n'.format(ce_ip)

# Cisco 880
item_880_1 = 'neighbor {} remote-as 65301\n'.format(ce_ip)
item_880_2 = 'neighbor {} local-as 65524\n'.format(ce_ip)
item_880_3 = 'neighbor {} route-map rm-sp2-in in\n'.format(ce_ip)
item_880_4 = 'neighbor {} route-map rm-sp2-out out\n'.format(ce_ip)
item_880_5 = 'neighbor {} filter-list 50 out\n'.format(ce_ip)
item_880_6 = 'neighbor {} send-community both\n'.format(ce_ip)
item_880_7 = 'neighbor {} soft-reconfiguration inbound\n'.format(ce_ip)

# MSR-930
src_list_930.pop(218)
src_list_930.insert(218, item_int_vl_700)
src_list_930.pop(255)
src_list_930.insert(255, item_930_1)
src_list_930.pop(256)
src_list_930.insert(256, item_930_2)
src_list_930.pop(257)
src_list_930.insert(257, item_930_3)
src_list_930.pop(258)
src_list_930.insert(258, item_930_4)
src_list_930.pop(259)
src_list_930.insert(259, item_930_5)
src_list_930.pop(260)
src_list_930.insert(260, item_930_6)
src_list_930.pop(261)
src_list_930.insert(261, item_930_7)

# Cisco 880
src_list_880.pop(360)
src_list_880.insert(360, item_int_vl_700)
src_list_880.pop(243)
src_list_880.insert(243, item_880_1)
src_list_880.pop(244)
src_list_880.insert(244, item_880_2)
src_list_880.pop(245)
src_list_880.insert(245, item_880_3)
src_list_880.pop(246)
src_list_880.insert(246, item_880_4)
src_list_880.pop(247)
src_list_880.insert(247, item_880_5)
src_list_880.pop(248)
src_list_880.insert(248, item_880_6)
src_list_880.pop(249)
src_list_880.insert(249, item_880_7)

# Cisco 2800
# item_880 потому-что строки конфига одинаковые
src_list_2800.pop(350)
src_list_2800.insert(350, item_int_vl_700)
src_list_2800.pop(238)
src_list_2800.insert(238, item_880_1)
src_list_2800.pop(239)
src_list_2800.insert(239, item_880_2)
src_list_2800.pop(240)
src_list_2800.insert(240, item_880_3)
src_list_2800.pop(241)
src_list_2800.insert(241, item_880_4)
src_list_2800.pop(242)
src_list_2800.insert(242, item_880_5)
src_list_2800.pop(243)
src_list_2800.insert(243, item_880_6)
src_list_2800.pop(244)
src_list_2800.insert(244, item_880_7)

dest_930 = open(dest_file_930, 'w')
dest_930.writelines(src_list_930)
dest_930.close()
dest_880 = open(dest_file_880, 'w')
dest_880.writelines(src_list_880)
dest_880.close()
dest_2800 = open(dest_file_2800, 'w')
dest_2800.writelines(src_list_2800)
dest_2800.close()

