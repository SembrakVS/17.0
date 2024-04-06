from odoo import _, api, models, fields


class Diseases(models.Model):
    _name = 'diseases'
    _description = 'Diseases'
    _parent_store = True

    name = fields.Char()
    parent_id = fields.Many2one(
        'diseases',
        string='Parent Disease',
        index=True,
        ondelete='cascade',
        domain="[('id', '!=', id),]",
    )
    child_ids = fields.One2many(
        'diseases',
        'parent_id',
        string='Child Diseases')

    parent_path = fields.Char(index=True)

    @api.depends('parent_id.parent_path')
    def _compute_parent_path(self):
        for disease in self:
            if disease.parent_id:
                disease.parent_path = "%s/%s" % (
                    disease.parent_id.parent_path,
                    disease.parent_id.id)
            else:
                disease.parent_path = "%s" % (disease.id)

    @api.constrains('parent_id')
    def check_recursion_parent_id(self):
        if not self._check_recursion():
            raise ValueError(_(
                'You cannot create recursive categories.'))

    _sql_constraints = [
        ('parent_check',
         'check(parent_id != id)',
         "You cannot create recursive hierarchy."),
    ]
