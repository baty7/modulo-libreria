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
        for record in self:
            vals["amount_total"] = record.total_precio

        """   def button_confirmar(self):
        for record in self:
            vals = {
                'partner_id': record.partner_id.id,
                'is_socio':record.is_socio,
                'numero_socio':record.numero_socio,
                'phone':record.phone,
                'email':record.email,
                'line_ids':[],        
            }
            
            for line in record.line_ids:
                venta_line_vals =  {
                    "libro_id": line.libro_id.id,
                    "genre": line.genre,
                    "isbn": line.isbn,
                    "author": line.author,
                    "price": line.price      
                    }            
                                
                vals['line_ids'].append((0,0,venta_line_vals))
                
            venta = self.env['sale.order'].create(vals) """
         