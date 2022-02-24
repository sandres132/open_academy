# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course'
    
    def copy(self, default={}):
        if not default.get('name'):
            default['name'] = "Copy of ["+self.name+"]"
        return super(Course, self).copy(default)

    name = fields.Char(
        string='Course'
    )

    _sql_constraints = [
        ("name_cnst", "UNIQUE(name)", "Course name has to be unique"),
        ("chk_cnst", "CHECK(title!=description)", "Course description has to be diferent than title"),
    ]

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
        inverse_name='course'
    )