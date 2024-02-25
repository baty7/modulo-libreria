# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class LibreriaSaleOrder(models.Model):
    _description = 'Modelo de ventas de la libreria'
    _inherit = 'sale.order'


    partner_id = fields.Many2one('res.partner',string="Cliente")
    is_socio = fields.Boolean(string='Socio')
    line_ids = fields.One2many('libros', inverse_name ='sale_order_id', string='Historial libros')