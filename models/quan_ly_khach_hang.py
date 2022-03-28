from odoo import api, fields, models, tools, _


class QLKH(models.Model):
    _inherit = 'res.partner'
    _description = 'Decription'

    loyalty_point = fields.Float('Số điểm của tích lũy của khách hàng')
    loyalty_level = fields.Many2one('partner.levels')
