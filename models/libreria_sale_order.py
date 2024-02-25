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
    