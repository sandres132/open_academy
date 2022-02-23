# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'session'

    name = fields.Char(
        string='Session'
    )
    start_date = fields.Date(
        date='Date'
    )
    
    duration = fields.Float(
        float='Duration'
    )

    number_seats = fields.Integer(
        Integer="Number of Seats"
    )

    instructor  = fields.Many2one(
        string='Instructor',
        comodel_name='res.partner',
        ondelete='restrict',
    )

    course = fields.Many2one(
        string='Course',
        comodel_name='open_academy.course',
        ondelete='restrict',
        required=True
    )