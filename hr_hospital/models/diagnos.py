from odoo import api, fields, models


class Diagnos(models.Model):
    _name = 'diagnos'
    _description = 'Diagnos'

    visit_id = fields.Many2one(comodel_name='pacient_visits')
    diseases_id = fields.Many2one(comodel_name='diseases')
    doctor_id = fields.Many2one(comodel_name='doctor')
    treatment = fields.Text(string='Appointment for treatment')
    approved = fields.Boolean(default=False)

    @api.model
    def create(self, vals):
        diagnos = super(Diagnos, self).create(vals)
        if diagnos.doctor_id and diagnos.doctor_id.is_intern:
            diagnos.approved = False
        return diagnos
