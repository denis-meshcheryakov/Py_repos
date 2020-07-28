# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

network = input('Введите адрес сети с префиксом(Например 10.1.1.0/24):')
ip = network[:network.find('/')]
ip = ip.split('.')
oct1 = int(ip[0])
oct2 = int(ip[1])
oct3 = int(ip[2])
oct4 = int(ip[3])

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
