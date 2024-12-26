# -*- coding: utf-8 -*-
{
    'name': "Elosys test",
    'summary': """  """,
    'description': """ test """,
    'version'       : "18.0.1.0",
    'category'      : "Human Resources/Employees",


    "contributors": [
       
        
    ],
    
    'sequence': 1,
    
    'company'       : 'Elosys',
    'author'        : 'Elosys',
    'maintainer'    : 'Elosys',

    'website': "https://www.elosys.net/",
    'support' : "support@elosys.net",
    'live_test_url' : "https://www.elosys.net/shop/employes-algerie-50?category=13#attr=111",

    

    'license'       : "LGPL-3",
    'price'         : "164.99",
    'currency'      : 'Eur',
    'depends': [
        'base',
    ],

'data': [
        'security/ir.model.access.csv',


        'views/elo_history_customer.xml',
        'views/menuitems.xml',


    ],

  
    'installable': True,
    'auto_install': False,
    'application': True,
}
