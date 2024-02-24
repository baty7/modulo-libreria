# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Libros(models.Model):
    _name = 'libros'
    _description = 'Modelo de libros donde se almacena informacion sobre cada libro'
    _inherit = ['mail_thread']

    _sql_constraints = [
        ('unique_isbn', 'UNIQUE(isbn)', 'El ISBN debe ser único. Ya existe un libro con este ISBN.')
    ]

    name = fields.Char(string='Nombre',help='Nombre del libro',required=True,track_visibility='onchangue')
    isbn = fields.Char(string="ISBN",required=True,track_visibility='onchangue')
    author = fields.Char(string="Autor",track_visibility='onchangue')
    description= fields.Text(string=u"Descripción",track_visibility='onchangue')
    price=fields.Float(string="Precio",track_visibility='onchangue')
    quantity = fields.Integer(string="Cantidad",track_visibility='onchangue')
    message_ids = fields.One2many('mail.message', 'res_id', domain=[('model', '=', 'libros')], string='Mensajes', copy=False)
    historial_prestamo_libro_ids = fields.One2many('prestamo.libros', inverse_name='libro_id', string='Historial de Préstamos')

    
    @api.model
    def get_genre(self):
        genre = [
            ("fantasia",u"Fantasía"),
            ("romance",u"Romance"),
            ("ciencia_ficcion",u"Ciencia ficción"),
            ("misterio",u"Misterio"),
            ("terror",u"Terror"),
        ]
        return genre
    genre = fields.Selection(get_genre,string="Género",track_visibility='onchangue')

    @api.model
    def get_state(self):
        state = [
            ("disponible",u"Disponible"),
            ("prestado",u"Prestado"),
            ("vendido",u"Vendido"),
            ("no_stock",u"Sin stock"),
        ]
        return state
    state = fields.Selection(get_state,string="Estado",default="disponible",track_visibility='onchangue')


    



    
    
    
      
    
    
