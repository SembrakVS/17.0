from odoo import fields, models


class Person(models.AbstractModel):
    _name = 'person'
    _description = 'Persons'

    first_name = fields.Char()
    last_name = fields.Char()
    phone = fields.Char()
    photo = fields.Image()
    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other/Undefined')],
        default='other'
    )
