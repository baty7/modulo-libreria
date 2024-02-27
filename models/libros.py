# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
import logging

_logger = logging.getLogger(__name__)

class Libros(models.Model):
    _name = 'libros'
    _description = 'Modelo de libros donde se almacena informacion sobre cada libro'
    _inherit = ['mail.thread']
    _rec_name = 'name'

    _sql_constraints = [
        ('unique_isbn', 'UNIQUE(isbn)', 'El ISBN debe ser único. Ya existe un libro con este ISBN.')
    ]

    name = fields.Char(string='Nombre',help='Nombre del libro',required=True,tracking=True)
    isbn = fields.Char(string="ISBN",required=True,tracking=True)
    author = fields.Char(string="Autor",tracking=True)
    
    description= fields.Text(string=u"Descripción",tracking=True)
    price=fields.Float(string="Precio",tracking=True)
    quantity = fields.Integer(string="Stock",tracking=True,required=True)
    message_ids = fields.One2many('mail.message', 'res_id', domain=[('model', '=', 'libros')], string='Mensajes', copy=False)
    sale_order_id = fields.Many2one('sale.order',string="Venta",tracking=True)
    sale_order_line_ids = fields.One2many('sale.order',inverse_name="libro_id",string="Lineas de ventas",tracking=True,compute="_compute_generar_venta_asociada_by_libro")

    @api.model
    def get_puntuacion(self):
        puntuacion = [
            ("mui_malo",u" Muy Malo"),
            ("malo",u"Malo"),
            ("normal",u"Normal"),
            ("mui_bueno",u"Muy bueno"),
            ("excelente",u"Para comprarte 30"),
        ]
        return puntuacion


    puntuacion_libro = fields.Selection(get_puntuacion,string="Puntuación del libro")
    
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
    genre = fields.Selection(get_genre,string="Género",tracking=True)

    @api.model
    def get_state(self):
        state = [
            ("disponible",u"Disponible"),
            ("no_stock",u"Sin stock"),
        ]
        return state
    state = fields.Selection(get_state,string="Estado",default="disponible",tracking=True)

    
    def _compute_generar_venta_asociada_by_libro(self):
        _logger.debug("_compute_generar_venta_asociada_by_libro")
        for libro in self:
            venta_asociada_by_libro = self.env['sale.order'].search([
                ("line_ids.libro_id","=",libro.id)
            ])
            libro.sale_order_line_ids = [(6, 0, venta_asociada_by_libro.ids)]


    @api.onchange('quantity')
    def _onchange_establecer_cantidad(self):
        for record in self:
            if record.quantity == 0:
                record.state = 'no_stock'
            elif record.quantity > 0:
                record.state = 'disponible'
            else:
                raise ValidationError(u"No puede haber un stock de libros negativo")
            

    def button_generar_venta_popup(self):
        ventas_ids = []
        for record in self:
            if record.quantity == 0:
                raise ValidationError(u"No se puede generar una venta de un libro sin STOCK")
            
            libros_vals_line = {
                "libro_id":record.id,
                "genre":record.genre,
                "isbn":record.isbn,
                "author":record.author,
                "price":record.price
            }

            ventas_ids.append((0,0,libros_vals_line))

        if len (ventas_ids) > 0:
            res = {
                'name': u'Generar venta',
                'view_type': 'form',
                'view_mode': 'form',
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                "views": [
                        [self.env.ref("modulo-libreria.libreria_sale_order_modal_form").id, "form"]
                ],
                'target': 'new',
                'context': {
                    'default_line_ids': ventas_ids
                } 
            }
            return res




    



    
    
    
      
    
    
