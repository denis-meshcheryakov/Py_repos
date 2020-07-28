# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf = ospf_route.split()
ospf.pop(2)  

prefix = ospf[0]
ad = ospf[1]
n_hop = ospf[2]
l_update = ospf[3]
o_intf = ospf[4]


ad = ad.strip('[]')
n_hop = n_hop.rstrip(',')
l_update = l_update.rstrip(',')
o_intf = o_intf.rstrip(',')

ospf_route = '''
Prefix	            	{0:18}
AD/Metric	        {1:18}
Next-Hop	        {2:18}
Last update	        {3:18}
Outbound Interface	{4:18}
'''

print(ospf_route.format(prefix,ad,n_hop,l_update,o_intf))
