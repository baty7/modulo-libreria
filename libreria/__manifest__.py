# -*- coding: utf-8 -*-
{
    'name': 'Gestión de una tienda de de libros    ',
    'summary':"Gestión de una tienda de de libros ",
    'description':"""
    Módulo para la gestión de una tienda de libros
    """,
    'author': "Juan José Bautista Gallego",

    'category': 'tools',
    'version': '0.2',
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/groups.xml',
        #'security/ir.model.access.csv',
        'views/libros.xml',
        #'views/templates.xml',
        #'demo/demo.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    # Pendiente de añadir un report Qweb.
    
}
