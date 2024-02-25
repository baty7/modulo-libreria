# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class LibreriaHistoricoSaleOrder(models.Model):
    _description = 'Historico de libros vendidos'
    _name = 'libreria.historico.sale.order'
    _rec_name = 'libro_id'

    libro_id = fields.Many2one('libros', string='Libro',required=True)
    order_id = fields.Many2one('sale.order',string="Orden de Venta")
    isbn = fields.Char(string='ISBN', related='libro_id.isbn', store=True)
    author = fields.Char(string='Autor', related='libro_id.author', store=True)
    price=fields.Float(string="Precio",related='libro_id.price', store=True)
    genre = fields.Selection(string="Género",related='libro_id.genre', store=True)
    total_importe = fields.Monetary(string='Total Importe', compute='_compute_total_importe', store=True)

    
    @api.depends('libro_id')
    def _compute_total_importe(self):
        total = 0
        for record in self:
            total += record.price
        return total  
            
        