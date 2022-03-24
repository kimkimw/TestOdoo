from odoo import fields, models, api

class PartnerLevels(models.Model):
    _name = 'partner.levels'
    _description = 'Description'

    name = fields.Char('Tên của cấp độ', required=True)
    loyalty_points = fields.Float('Số điểm cần đạt được cấp độ tương ứng', required=1)
    description = fields.Text('Mô tả cấp độ')


