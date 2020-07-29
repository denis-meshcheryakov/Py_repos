#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

network = argv[1:]
network = ' '.join(network)
ip = network[:network.find('/')]
ip = ip.split('.')
oct1 = int(ip[0])
oct2 = int(ip[1])
oct3 = int(ip[2])
oct4 = 0 * (int(ip[3]))

ip_tamplate = '''
Network
{0:<8} {1:<8} {2:<8} {3:<8}
{0:<08b} {1:<08b} {2:<08b} {3:<08b}
'''

print(ip_tamplate.format(oct1, oct2, oct3, oct4))

mask = network[network.find('/')::]
mask = mask.lstrip('/')
maskint = int(mask)
maskbit = '1' * maskint
maskbit = "{:<032}".format(maskbit)
moct1 = int(maskbit[0:8], 2)
moct2 = int(maskbit[8:16], 2)
moct3 = int(maskbit[16:24], 2)
moct4 = int(maskbit[24:32], 2)

mask_template = '''
Mask:
{4:<}
{0:<8} {1:<8} {2:<8} {3:<8}
{0:<8b} {1:<8b} {2:<8b} {3:<8b}
'''
print(mask_template.format(moct1, moct2, moct3, moct4, mask))
