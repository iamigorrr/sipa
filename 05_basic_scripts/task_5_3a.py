# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''



port_template = {
    'access' : {
			'access' : 'switchport mode access\n' 'switchport access vlan {}\n'
			'switchport nonegotiate\n' 'spanning-tree portfast\n'
			'spanning-tree bpduguard enable\n',
			
			'text' : 'Введите номер VLAN: '
    
    
    
   },


    'trunk' : {
			'trunk' : 'switchport trunk encapsulation dot1q\n' 'switchport mode trunk\n'
			'switchport trunk allowed vlan {}\n',
			
			'text' : 'Введите разрешенные VLANы: '
   }
}

mode = input('Введите режим работы интерфейса (access/trunk): ')
num = input('Введите тип и номер интерфейса: ')
vlans = input(port_template[mode]['text'])

print('interface ' + num)

print(port_template[mode][mode].format(vlans))
#mode_template = (mode + '_template')
#print(mode_template.format(vlans))
