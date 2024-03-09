import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Pacient(models.Model):
    _name = 'pacient'
    _description = 'Pacient'

    name = fields.Char()

    active = fields.Boolean(default=True, )
