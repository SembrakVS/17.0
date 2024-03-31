from odoo import fields, models


class Speciality(models.Model):
    _name = 'speciality'
    _description = 'Speciality'

    name = fields.Char()
