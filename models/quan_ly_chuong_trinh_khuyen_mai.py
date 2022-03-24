from odoo import api, fields, models, tools, _

class QLCTKM(models.Model):
    _name = 'quan.ly.chuong.trinh.khuyen.mai'
    _description = 'Decription'

    name = fields.Char('Tên của chương trình khuyến mãi', required=True)
    points = fields.Float('Số % point nhận được trên 1 đơn hàng.', required=True)
    active = fields.Boolean(string="Active", required=True)
