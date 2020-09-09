#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "add_to_vl_700.py"
#  
'''Преременная "n" добавляет слово "no" в строку вывода "ip address 10.69.240.1 255.255.255.128 secondary" 
получается так: "no ip address 10.69.240.1 255.255.255.128 secondary" '''

n = input('''Если хотите добавить подсеть, нажмите Enter
Введите подсети и нажмите Enter:
________________________________________________________

Если хотите удалить подсеть, введите "no" и нажмите Enter
Введите подсети и нажмите Enter:

<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
''')
net = ""
while True:
    network = input('*')
    if network:
        net += network + " "
    else:
        break      
net = net.split()
netip = []
netmask = []
netip2 = []
netmask2 = []
for ipx in net:
    str(ipx)
    ip, mask = ipx.split('/')
    netip.append(ip)
    netmask.append(mask)


for ip in netip:
    ip = ip.split('.')
    oktet1 = int(ip[0])
    oktet2 = int(ip[1])
    oktet3 = int(ip[2])
    oktet4 = 1 + int(ip[3])
    ipadd = [str(oktet1), str(oktet2), str(oktet3), str(oktet4)]
    ipad = '.'.join(ipadd)
    netip2.append(ipad)
    
for maskint in netmask:
    maskint = int(maskint)
    maskbit = '1' * maskint
    maskbit = "{:<032}".format(maskbit)
    moktet1 = int(maskbit[0:8], 2)
    moktet2 = int(maskbit[8:16], 2)
    moktet3 = int(maskbit[16:24], 2)
    moktet4 = int(maskbit[24:32], 2)
    mask = [str(moktet1), str(moktet2), str(moktet3), str(moktet4)]
    mask = '.'.join(mask)
    netmask2.append(mask)
    
result = list(zip(netip2, netmask2))

print('''
conf t
int vl 700''')
for ip, mask in result:
    print('{} ip address {} {} secondary'.format(n, ip, mask))
    
print('''end
wr

''')    
