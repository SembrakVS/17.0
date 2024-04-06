import logging

from odoo import api, models, fields, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class PacientVisits(models.Model):
    _name = 'pacient_visits'
    _description = 'Pacient Visits'

    status_visits = fields.Selection(
        selection=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')],
        default='scheduled'
    )
    planned_visits_date = fields.Datetime()
    visits_date = fields.Datetime()
    doctor_id = fields.Many2one(comodel_name="doctor")
    pacient_id = fields.Many2one(comodel_name="pacient")
    diagnos_ids = fields.One2many(
        comodel_name='diagnos',
        inverse_name='visit_id',
        string='Diagnoses'
    )

    @api.constrains('status_visits', 'visits_date', 'doctor_id')
    def _check_past_visit(self):
        for record in self:
            if (record.status_visits == 'completed'
                    and (not record.doctor_id or not record.visits_date)):
                raise ValidationError(_(
                    "You cannot change doctor or visits date "
                    "after status is set to Completed."))

    @api.constrains('diagnos_ids')
    def _check_diagnos_ids(self):
        for record in self:
            if record.diagnos_ids:
                raise ValidationError(_(
                    "You cannot delete or archive visits with diagnoses."))

    @api.constrains('pacient_id', 'visits_date')
    def _check_unique_patient_per_day(self):
        for record in self:
            count = self.env['pacient_visits'].search_count([
                ('pacient_id', '=', record.pacient_id.id),
                ('visits_date', '=', record.visits_date.date()),
                ('id', '!=', record.id)
            ])
            if count > 0:
                raise ValidationError(_(
                    "You cannot schedule more than one visit "
                    "for a patient to the same doctor on the same day."))

    def write(self, vals):
        if 'status_visits' in vals and vals['status_visits'] == 'completed':
            if 'doctor_id' in vals or 'visits_date' in vals:
                raise ValidationError(_(
                    "You cannot change doctor_id or visits date"
                    " after status is set to Completed."))
        return super(PacientVisits, self).write(vals)
