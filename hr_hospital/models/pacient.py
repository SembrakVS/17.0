from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class Pacient(models.Model):
    _name = 'pacient'
    _description = 'Pacient'
    _inherit = 'person'

    name = fields.Char(compute='_compute_name', store=True)
    personal_doctor = fields.Many2one(
        string='Personal doctor',
        comodel_name='doctor')
    birthday = fields.Date(string='Date of Birth')
    age = fields.Integer(compute='_compute_age')
    passport = fields.Binary(attachment=True)
    contact_person = fields.Char()
    doctor_diagnosis_history_ids = fields.One2many(
        comodel_name='diagnos',
        inverse_name='pacient_id',
        string='Diagnoses')
    visit_history_ids = fields.One2many(
        'pacient_visits',
        'pacient_id',
        string='Visit History'
    )

    def view_visit_history(self):
        return {
            'name': 'Visit History',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'pacient_visits',
            'domain': [('pacient_id', '=', self.id)],
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

    def action_create_visits(self):
        self.ensure_one()
        return {
            'name': 'New Visits',
            'type': 'ir.actions.act_window',
            'res_model': 'pacient_visits',
            'view_mode': 'form',
            'context': {'default_pacient_id': self.id},
            'target': 'new'
        }

    @api.depends('birthday')
    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                rec.age = relativedelta(
                    date.today(),
                    date(
                        rec.birthday.year,
                        rec.birthday.month,
                        rec.birthday.day),
                ).years
            else:
                rec.age = False

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = "%s %s" % (rec.first_name, rec.last_name or '')
