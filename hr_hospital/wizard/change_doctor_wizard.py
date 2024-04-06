from odoo import models, fields


class ChangeDoctorWizard(models.TransientModel):
    _name = 'change.doctor.wizard'
    _description = 'Change Doctor Wizard'

    new_doctor_id = fields.Many2one('doctor', string='New Doctor')

    def change_patient_doctor(self):
        active_ids = self.env.context.get('active_ids', [])
        patients = self.env['pacient'].browse(active_ids)
        patients.write({'personal_doctor': self.new_doctor_id.id})
