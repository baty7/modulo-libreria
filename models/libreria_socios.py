# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class LibreriaSocios(models.Model):
    _name = 'libreria.socios'
    _description = 'Modelo de socios de la libreria'
    _inherit = 'res.partner'

    numero_socio = fields.Char(string='Número de Socio')
    #historial_prestamos = fields.One2many('prestamos', inverse_name ='socio_id', string='Historial de Préstamos')


