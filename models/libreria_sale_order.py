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
    #partner_id = fields.Many2one('res.partner',string="Cliente",required=False)
    numero_socio = fields.Char(string='Número de Socio',required=True)
    telefono = fields.Char(string='Teléfono',related='partner_id.phone')
    email = fields.Char(string='Correo electrónico',related='partner_id.email')
    total_precio = fields.Monetary(string='Total Precio', compute='_compute_total_precio', store=True)

    @api.depends('line_ids.price')
    def _compute_total_precio(self):
        for record in self:
            record.total_precio = sum(linea.price for linea in record.line_ids)

    
    @api.model_create_multi
    def create(self, vals):

        self.procesar_vals(vals)

        res = super(LibreriaSaleOrder, self).create(vals)
        return res

    def write(self, vals):

        self.procesar_vals(vals)

        res = super(LibreriaSaleOrder, self).write(vals)
        return res  
    
    @api.model
    def procesar_vals(self,vals):
        #amount_total_vals = vals.get("amount_total",None)
        #if amount_total_vals is not None:
        vals["amount_total"] = self._compute_total_precio()
         