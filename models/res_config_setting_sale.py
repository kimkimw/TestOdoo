from odoo import fields, models, api


class ResConfigSettingSale(models.TransientModel):
    _inherit = 'res.config.settings'

    loyalty_for_sale_id = fields.Many2one(comodel_name='quan.ly.chuong.trinh.khuyen.mai', config_parameter='loyalty_sale_id')



