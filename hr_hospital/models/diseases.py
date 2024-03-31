from odoo import models, fields


class Diseases(models.Model):
    _name = 'diseases'
    _description = 'Diseases'

    name = fields.Char()
