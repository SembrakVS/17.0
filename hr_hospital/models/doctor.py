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
    intern_ids = fields.One2many(
        comodel_name='doctor',
        compute='_compute_intern_ids',
        string='Interns')
    pacient_visit_id = fields.One2many('pacient_visits', 'doctor_id')

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = "%s %s" % (rec.first_name, rec.last_name or '')

    @api.depends('is_intern')
    def _compute_intern_ids(self):
        for doctor in self:
            if doctor.is_intern:
                doctor.intern_ids = False
            else:
                doctor.intern_ids = self.search([(
                    'mentor_id', '=', 'doctor.id')])
