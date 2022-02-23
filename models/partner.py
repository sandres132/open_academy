# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import partner

class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    instructor = fields.Boolean(
        string='Instructor',
        default = False
    )
    
    session_partner = fields.Many2many(
        string='Session_Partner',
        comodel_name='open_academy.session',
        readonly=True
    )
    