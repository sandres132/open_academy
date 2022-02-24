# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


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
        Integer="Number of Seats",
        default = 1
    )

    instructor = fields.Many2one(
        string='Instructor',
        comodel_name='res.partner',
        ondelete='restrict',
        required=True,
        domain=['|', ('instructor', '=', True),
                ('category_id.name', 'ilike', "Teacher")]
    )

    course = fields.Many2one(
        string='Course',
        comodel_name='open_academy.course',
        ondelete='restrict',
        required=True
    )

    @api.depends('attendees')
    def total_attend(self):
        for record in self:
            record.attend_count = len(record.attendees)

    attend_count = fields.Integer(
        string='Attend_count',
        compute = total_attend
    )
    

    @api.constrains('attendees', 'instructor')
    def _check_something(self):
        for record in self.attendees:
            if record==self.instructor:
                raise ValidationError("Your record is categorized as the instructor of this session")

    attendees = fields.Many2many(
        string='Attendees',
        comodel_name='res.partner'
    )

    @api.depends('number_seats')
    @api.depends('attendees')
    def taken_seats(self):
        cont = 0

        for record in self.attendees:
            cont = cont+1

        for record in self:
            record.percentage = (cont/record.number_seats)*100

    @api.onchange('attendees', 'number_seats')
    def _onchange_porcentage(self):
        cont = 0

        for record in self.attendees:
            cont = cont+1

        if cont<=self.number_seats and self.number_seats>0:
            self.percentage = (cont/self.number_seats)
        elif self.number_seats<=0:
            return {
                'warning': {
                    'title': "Something bad happened",
                    'message': "Negative number of seats",
                }
            }
        elif cont>self.number_seats:
            return {
                'warning': {
                    'title': "Something bad happened",
                    'message': "There are more participants than seats",
                }
            }

    percentage = fields.Float(
        string='Taken seats percentage',
        compute=taken_seats,
    )

    active = fields.Boolean(
        string='Active',
        default=True,
    )
