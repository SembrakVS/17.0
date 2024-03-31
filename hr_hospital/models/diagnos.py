from odoo import fields, models


class Diagnos(models.Model):
    _name = 'diagnos'
    _description = 'Diagnos'

    # name = fields.Char()
    visit_id = fields.Many2one(comodel_name='pacient_visits')
    diseases_id = fields.Many2one(comodel_name='diseases')
    treatment = fields.Text(string='Appointment for treatment')
    approved = fields.Boolean()
