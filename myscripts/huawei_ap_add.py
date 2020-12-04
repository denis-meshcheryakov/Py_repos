#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "huawei_ap_add.py"
#
import re
import ipaddress

#sap = input('Введите номер САП: ')
ap_id = int(input('Введите последний зарегестрированный на контроллере AP ID: '))
division = input('Введите девизион: ')
print('''Введите вывод ARP
затем нажминте Enter для подтверждения : ''')
# Ввод строк приглашения роутера и вывода ARP 
arp = []
while True:
    arp_input = input()
    if arp_input:
        arp.append(arp_input)
    else:
        break
# Получаем список строк на каждый ARP


def get_sap(arp):
    # Получаем значение SAP из строки <930-RTR-31H2>di arp vl 30 или <930-RTR-31H2>
    for line in arp:
        if line.startswith('<'):
            sap = re.search('\w\w\w\w', line).group()
    return sap

sap = get_sap(arp)

def get_ip_netmask(arp):
# Получаем объект ipaddress.ip_network, по которому в
# дальнейшем будут определяться строки arp-вывода принадлежащие только к ТД
    arp_line = arp[4]
    if arp_line.startswith('1'):
        split_line = arp_line.split()
        ip = split_line[0]
        ip = ip.split('.')
        oct1, oct2, oct3, oct4 = ip
        host_octet = int(oct4)
        if host_octet in range(0, 32):
            net_mask = "{}.{}.{}.16/28".format(oct1, oct2, oct3)
        if host_octet in range(32, 64):
            net_mask = "{}.{}.{}.48/28".format(oct1, oct2, oct3)
        if host_octet in range(64, 96):
            net_mask = "{}.{}.{}.80/28".format(oct1, oct2, oct3)
        if host_octet in range(96, 128):
            net_mask = "{}.{}.{}.112/28".format(oct1, oct2, oct3)
        if host_octet in range(128, 160):
            net_mask = "{}.{}.{}.144/28".format(oct1, oct2, oct3)
        if host_octet in range(160, 192):
            net_mask = "{}.{}.{}.176/28".format(oct1, oct2, oct3)
        if host_octet in range(192, 224):
            net_mask = "{}.{}.{}.208/28".format(oct1, oct2, oct3)
        if host_octet in range(224, 254):
            net_mask = "{}.{}.{}.240/28".format(oct1, oct2, oct3)

    ip_netmask = ipaddress.ip_network(net_mask)
    return ip_netmask
    
ip_netmask = get_ip_netmask(arp)


def get_arp_dict(arp):
#Получаем словарь в котором key это объект ip_address, а значение mac-address
    arp_list = []
    for line in arp:
        if line.startswith('1'):
            match = re.search('([\w.]+)\s+(\S+)\s+.*', line)
            key = match.group(1)
            ip = ipaddress.ip_address(key)
            value = match.group(2)
            arp_list.append([ip, value])
    return arp_list


arp_list = get_arp_dict(arp)



def get_ap_ip(ip_netmask, arp_list):
    ap_mac_address_list = []
    for line in arp_list:
        if line[0] in ip_netmask:
            ap_mac_address_list.append(line[1])
    return ap_mac_address_list

ap_mac_address_list = get_ap_ip(ip_netmask, arp_list)



def compile_data(ap_id, ap_mac_address_list, sap, division, apn):
    # Генератор конфига для каждой точки доступа
    result = []
    ap_name_list = []
    ap_group_list = []
    for mac in ap_mac_address_list:
        ap_id = ap_id + 1
        result.append('ap-id {} ty 75 ap-mac {}'.format(ap_id, mac))
        apn = apn + 1
        result.append('ap-name {}-5-{}-AP0{}'.format(sap, division, apn))
        result.append('y')
        result.append('ap-group {}-5'.format(division))
        result.append('y')
        result.append('\n')
    return result


result_list = compile_data(ap_id, ap_mac_address_list, sap, division, apn = 00)

print('''sys
wlan
''')
for line in result_list:
    print(line)
print('''
quit
quit
quit
sa all
y

''')

print('display ap all | i {}'.format(sap))
print()
print()

print('*'*10, 'config for router', '*'*10)
print('''
sy
dhcp server ip-pool VLAN30-MANAGE
option 43 hex 031A3137 322E3139 2E31382E 31352C31 37322E31 392E3138 2E313434
undo opt 189
opt 42 ip 192.168.129.17
sa fo
''')
