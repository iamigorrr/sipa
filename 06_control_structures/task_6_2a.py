# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = input('Введите IP-адрес в формате X.X.X.X: ')
ip_correct = False

'''
if ''.join(ip.split('.')).isdigit() and len(ip.split('.')) == 4:
	for octet in ip.split('.'):
		if int(octet) < 256 and int(octet) >= 0:
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
'''
if ''.join(ip.split('.')).isdigit() and len(ip.split('.')) == 4:
	for octet in ip.split('.'):
		if int(octet) > 255 or int(octet) < 0:
				print('Неправильный IP-адрес')
				break
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
