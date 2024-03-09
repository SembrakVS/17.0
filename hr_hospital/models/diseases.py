import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Diseases(models.Model):
    _name = 'diseases'
    _description = 'Diseases'

    name = fields.Selection(
        selection=[
            ("covid", "Covid"),
            ("influenza", "Influenza"),
            ("asthma", "Asthma Bronchiale"),
        ]
    )

    active = fields.Boolean(default=True, )
