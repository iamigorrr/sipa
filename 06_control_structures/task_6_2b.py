# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input('Введите IP-адрес в формате X.X.X.X: ')
ip_correct = False

if ''.join(ip.split('.')).isdigit() and len(ip.split('.')) == 4:
	for octet in ip.split('.'):
		if int(octet) > 255 or int(octet) < 0:
				print('Неправильный IP-адрес')
	else:
		if int(ip.split('.')[0]) > 0 and int(ip.split('.')[0]) < 224:
			print('Адрес unicast')
		elif int(ip.split('.')[0]) > 223 and int(ip.split('.')[0]) < 240:
			print('Адрес multicast')
		elif '255.255.255.255' in ip:
			print('Адрес local broadcast')
		elif '0.0.0.0' in ip:
			print('Адрес unassigned')
		else:
			print('Адрес unused')	
else:
	print('Неправильный IP-адрес')
