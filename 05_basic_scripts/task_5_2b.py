# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

#ipinput = input('Введите IP-сеть в формате X.X.X.X/X: ')
ip = argv[1].split('.')
mask = argv[2]
binmask = (int(mask) * '1' + (32 - int(mask)) * '0')



oct1 = (int(bin(int(ip[0]) & int(binmask[0:8],2))[2:],2))
oct2 = (int(bin(int(ip[1]) & int(binmask[8:16],2))[2:],2))
oct3 = (int(bin(int(ip[2]) & int(binmask[16:24],2))[2:],2))
oct4 = (int(bin(int(ip[3]) & int(binmask[24:32],2))[2:],2))

iptemplate = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

masktemplate = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print(iptemplate.format(oct1, oct2, oct3, oct4))
print('Mask:\n' + '/' + mask)
print(masktemplate.format(int(binmask[0:8],2), int(binmask[8:16],2), int(binmask[16:24],2), int(binmask[24:32],2)))
