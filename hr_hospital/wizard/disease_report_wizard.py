from odoo import _, models, fields


class DiseaseReportWizard(models.TransientModel):
    _name = 'disease.report.wizard'
    _description = 'Disease Report Wizard'

    doctor_ids = fields.Many2many(
        'doctor',
        string='Doctors',
        options={'no_create': True})
    disease_ids = fields.Many2many(
        'diseases',
        string='Diseases',
        options={'no_create': True})
    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To')

    def generate_report(self):
        domain = []
        if self.doctor_ids:
            domain.append(('doctor_ids', 'in', self.doctor_ids.ids))
        if self.disease_ids:
            domain.append(('disease_ids', 'in', self.disease_ids.ids))
        if self.date_from:
            domain.append(('visit_id.visits_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('visit_id.visits_date', '<=', self.date_to))

        diagnoses = self.env['diagnos'].search(domain)
        report_data = {}
        for diagnosis in diagnoses:
            for disease in diagnosis.diseases_ids:
                disease_name = disease.name
                if disease_name not in report_data:
                    report_data[disease_name] = []
                report_data[disease_name].append(diagnosis.id)

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'name': _('Disease Report'),
            'res_model': 'diagnos',
            'domain': [('id', 'in', diagnoses.ids)],
            'context': {'group_by': 'diseases_id'},
        }

    # def action_open_wizard(self):
    #     return {
    #         'name': _('Disease Report Wizard'),
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'disease.report.wizard',
    #         'target': 'new',
    #         'context': self.env.context,
    #     }
