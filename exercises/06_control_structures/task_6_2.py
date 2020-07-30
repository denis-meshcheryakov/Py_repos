# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP-адрес в формате 10.0.1.1:  ')
ip = ip.strip().split('.')
okt1 = int(ip[0])
okt2 = int(ip[1])
okt3 = int(ip[2])
okt4 = int(ip[3])

unicast = list(range(1, 224))
multicast = list(range(224, 240))
broadcast = [255, 255, 255, 255]
unassigned = [0, 0, 0, 0]

if okt1 in unicast:
    print('unicast')
elif okt1 in multicast:
    print('multicast')
elif okt1 in broadcast and okt2 in broadcast and okt3 in broadcast and okt4 in broadcast:
    print('local broadcast')
elif okt1 in unassigned and okt2 in unassigned and okt3 in unassigned and okt4 in unassigned:
    print('unassigned')
else:
    print('unused')