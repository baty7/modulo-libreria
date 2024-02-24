# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Libros(models.Model):
    _name = 'libros'
    _description = 'Modelo de libros donde se almacena informacion sobre cada libro'

    name = fields.Char(string='Nombre',help='NOmbre del libro',required=True)
    isbn = fields.Char(string="ISBN",required=True)
    author = fields.Char(string="Autor")
    desctiption= fields.Text(string="Descripción")
    price=fields.Float(string="Precio")
    quantity = fields.Integer(string="Cantidad")
    
    @api.model
    def get_genre(self):
        genre = [
            ("fantasia","Fantasía"),
            ("romance","Romance"),
            ("ciencia_ficcion","Ciencia ficción")
            ("misterio","Misterio"),
            ("terror","Terror")
        ]
        return genre
    genre = fields.Selection(get_genre,string="Género")

    @api.model
    def get_state(self):
        state = [
            ("prestado","Prestado"),
            ("vendido","Vendido"),
            ("no_stock","Sin stock")
        ]
        return state
    state = fields.Selection(get_state,string="Estado")


    



    
    
    
      
    
    
