# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course'

    name = fields.Char(
        string='Course'
    )
    title = fields.Char(
        string='First course'
    )
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(
        string='Course of open_academy'
    )
