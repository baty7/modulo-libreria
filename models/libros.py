# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Libros(models.Model):
    _name = 'libros'
    _description = 'Modelo de libros donde se almacena informacion sobre cada libro'

    name = fields.Char(string='Nombre',help='Nombre del libro',required=True)
    isbn = fields.Char(string="ISBN",required=True)
    author = fields.Char(string="Autor")
    description= fields.Text(string=u"Descripción")
    price=fields.Float(string="Precio")
    quantity = fields.Integer(string="Cantidad")
    
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
    genre = fields.Selection(get_genre,string="Género")

    @api.model
    def get_state(self):
        state = [
            ("disponible",u"Disponible"),
            ("prestado",u"Prestado"),
            ("vendido",u"Vendido"),
            ("no_stock",u"Sin stock"),
        ]
        return state
    state = fields.Selection(get_state,string="Estado",default="disponible")


    



    
    
    
      
    
    
