# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course'

    name = fields.Char(
        string='Course'
    )
    title = fields.Char(
        string='Title'
    )

    responsible  = fields.Many2one(
        string='Responsible',
        comodel_name='res.users',
        ondelete='restrict',
    )

    description = fields.Text(
        string='Description'
    )

    session = fields.One2many(
        string='Session',
        comodel_name='open_academy.session',
        inverse_name='course',
    )
    