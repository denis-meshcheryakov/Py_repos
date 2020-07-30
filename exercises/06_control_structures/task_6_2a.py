# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input('Введите IP-адрес в формате 10.0.1.1:  ')
ip = ip.strip().split('.')
okt1 = int(ip[0])
okt2 = int(ip[1])
okt3 = int(ip[2])
okt4 = int(ip[3])

dot = ip.split('.')

if dot != 3:
    print('Неправильный IP-адрес, октеты разделяются точками')
    else:
        "проверка на числа в октетах"
        ip = ip.strip().split('.')



# Проверка на тип адреса
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
