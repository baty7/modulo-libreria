# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class LibreriaSaleOrder(models.Model):
    _description = 'Modelo de ventas de la libreria'
    _inherit = 'sale.order'

    is_socio = fields.Boolean(string='Socio')
    line_ids = fields.One2many('libreria.historico.sale.order', inverse_name ='order_id', string='Historial libros')
    libro_id = fields.Many2one('libros', string='Libro')
    partner_id = fields.Many2one('res.partner',string="Cliente")
    numero_socio = fields.Char(string='Número de Socio',related='partner_id.numero_socio')
    telefono = fields.Char(string='Teléfono',related='partner_id.phone')
    email = fields.Char(string='Correo electrónico',related='partner_id.email')
    