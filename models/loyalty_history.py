from odoo import fields, models, api


class LoyaltyHistory(models.Model):
    _name = 'loyalty.history'
    _description = 'Description'

    partner_id = fields.Many2one(comodel_name='res.partner', string= "Tên khách hàng")
    loyalty_points = fields.Float('Tổng số điểm tích lũy nhận được trong 1 đơn hàng')
    money_spent = fields.Float('Tổng tiền của 1 đơn hàng')
    loyalty_point = fields.Float('Số điểm của tích lũy của khách hàng')
    date_order = fields.Datetime('Thời gian xác nhận đơn hàng')
    name = fields.Char('Mã đơn hàng')


