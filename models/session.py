# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'session'

    name = fields.Char(
        string='Session'
    )
    start_date = fields.Date(
        date='Date',
        default=fields.Date.context_today,
    )
    
    duration = fields.Float(
        float='Duration'
    )

    number_seats = fields.Integer(
        Integer="Number of Seats"
    )

    instructor = fields.Many2one(
        string='Instructor',
        comodel_name='res.partner',
        ondelete='restrict',
        required=True,
        domain = ['|', ('instructor', '=', True), ('category_id.name', 'ilike', "Teacher")]
    )

    course = fields.Many2one(
        string='Course',
        comodel_name='open_academy.course',
        ondelete='restrict',
        required=True
    )

    attendees = fields.Many2many(
        string='Attendees',
        comodel_name='res.partner'
    )

    @api.depends('number_seats')
    @api.depends('attendees')
    def taken_seats(self):
        cont=0

        for record in self.attendees:
            cont=cont+1

        for record in self:
            record.percentage = (cont/record.number_seats)*100

    percentage = fields.Float(
        string='Taken seats percentage',
        compute=taken_seats
    )
    
    
    active = fields.Boolean(
        string='Active',
        default=True,
    )
    