# -*- coding: utf-8 -*-

{
    'name': 'CMMS / IP Map Integration',
    'version': '0.1',
    'category': 'Generic Modules',
    'sequence': 98,
    'summary': 'Allow Equipment to be linked to IP records.',
    'description': 'Allow Equipment to be linked to IP records.',
    'author': 'Van Sebille Systems',
    'depends': [
        'base',
        'cmms',
	'ip_map',
        'web',
        ],
    'data': [
        'cmms_view.xaml',
        ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
