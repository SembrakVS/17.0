import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class PacientVisits(models.Model):
    _name = 'pacient_visits'
    _description = 'Pacient Visits'

    # name = fields.Char()
    status_visits = fields.Selection(
        selection=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')],
        default='scheduled'
    )
    plannet_visits_date = fields.Datetime()
    visits_date = fields.Datetime()
    doctor_id = fields.Many2one(comodel_name="doctor")
    pacient_id = fields.Many2one(comodel_name="pacient")
    diagnos_ids = fields.One2many(
        comodel_name='diagnos',
        inverse_name='visit_id',
        string='Diagnoses'
    )
