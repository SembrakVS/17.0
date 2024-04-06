from odoo import api, fields, models


class Doctor(models.Model):
    _name = 'doctor'
    _description = 'Doctor'
    _inherit = 'person'

    name = fields.Char(compute='_compute_name', store=True)
    speciality = fields.Many2one(comodel_name='speciality')
    is_intern = fields.Boolean(string='Intern')
    mentor_id = fields.Many2one(
        comodel_name='doctor',
        string='Mentor',
        domain="[('is_intern', '=', True)]",
        attrs={'invisible': [('is_intern', '=', False)]}
    )

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = "%s %s" % (rec.first_name, rec.last_name or '')
