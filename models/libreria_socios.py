# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class LibreriaSocios(models.Model):
    _description = 'Modelo de socios de la libreria'
    _inherit = 'res.partner'

    numero_socio = fields.Char(string='Número de Socio')



