from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class Pacient(models.Model):
    _name = 'pacient'
    _description = 'Pacient'
    _inherit = 'person'

    name = fields.Char(compute='_compute_name', store=True)
    personal_doctor = fields.Many2one(
        string='Personal doctor',
        comodel_name='doctor')
    birthday = fields.Date(string='Date of Birth')
    age = fields.Integer(compute='_compute_age')
    passport = fields.Binary(attachment=True)
    contact_person = fields.Char()

    @api.depends('birthday')
    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                rec.age = relativedelta(
                    date.today(),
                    date(
                        rec.birthday.year,
                        rec.birthday.month,
                        rec.birthday.day),
                ).years
            else:
                rec.age = False

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = "%s %s" % (rec.first_name, rec.last_name or '')
