# -*- coding: utf-8 -*-
{
    'name':'libreria',
    'summary':"Gestión de una tienda de de libros",
    'description':"""
    Módulo para la gestión de una tienda de libros
    """,
    'author': "Juan José Bautista Gallego",

    'category': 'tools',
    'version': '1.2',
    'depends': ['base','mail','sale'],
    'data': [
        #'security/groups.xml',
        'security/ir.model.access.csv',
        'views/libros.xml',
        'views/libreria_sale_order.xml',
        'views/libreria_socios.xml',
        'demo/demo.xml',
    ],
    'images':[
        'static/description/logo-tienda.jpeg',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
}
