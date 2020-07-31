#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  "add_vl_700.py"
#  
network = input('Введите адрес сети с префиксом(Например 10.1.1.0/30):')
ip = network[:network.find('/')]
ip = ip.split('.')
oct1 = int(ip[0])
oct2 = int(ip[1])
oct3 = int(ip[2])
oct4 = 1 + (int(ip[3]))
oct5 = 1 + (int(oct4))

int_vl700_temp = "{0:<}.{1:<}.{2:<}.{3:<}"

ipadd = int_vl700_temp.format(oct1, oct2, oct3, oct4)

mask = network[network.find('/')::]
mask1 = mask.lstrip('/')
maskint = int(mask1)
maskbit = '1' * maskint
maskbit = "{:<032}".format(maskbit)
moktet1 = int(maskbit[0:8], 2)
moktet2 = int(maskbit[8:16], 2)
moktet3 = int(maskbit[16:24], 2)
moktet4 = int(maskbit[24:32], 2)

mask_template = "{0:<}.{1:<}.{2:<}.{3:<}"


maskf = mask_template.format(moktet1, moktet2, moktet3, moktet4)

resalt_template = """
conf t
int vl 700
ip address {ipadd} {maskf} secondary
end
wr
"""

print(resalt_template.format(ipadd=ipadd, maskf=maskf))
