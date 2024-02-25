# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class PrestamoLibros(models.Model):
    _name = 'prestamo.libros'
    _description = 'Modelo de prestamos de la libreria'

    socio_id = fields.Many2one('libreria.socios', string='Socio')
    libro_id = fields.Many2one('libros', string='Libro')
    fecha_prestamo = fields.Date(string='Fecha de Préstamo')
    fecha_devolucion = fields.Date(string='Fecha de Devolución')
    estado = fields.Selection([('prestado', 'Prestado'), ('devuelto', 'Devuelto')], default='prestado', string='Estado')


   