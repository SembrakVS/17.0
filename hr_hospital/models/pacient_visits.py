import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class PacientVisits(models.Model):
    _name = 'pacient_visits'
    _description = 'Pacient Visits'

    doctor_id = fields.Many2one(comodel_name="doctor")
    pacient_id = fields.Many2one(comodel_name="pacient")
    date = fields.Datetime()

    active = fields.Boolean(default=True, )
