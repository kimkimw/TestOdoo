from odoo import fields, models, api, _


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    points_acumulated = fields.Float('Points acumulated')
    points_acumulating = fields.Float('Points acumulating')
    points_won = fields.Float('Points won')
    points_used = fields.Float('Points used')
    percent = fields.Float(related='loyalty_name.points')

    def _default_loyalty_program(self):
        loyalty_id = int(self.env['ir.config_parameter'].sudo().get_param('loyalty_sale_id', False))
        loyalty = self.env['quan.ly.chuong.trinh.khuyen.mai'].browse(loyalty_id)
        return loyalty if loyalty_id and loyalty.exists() else None

    loyalty_name = fields.Many2one(
        comodel_name='quan.ly.chuong.trinh.khuyen.mai',
        string='Chương trình khuyến mãi',
        default=_default_loyalty_program
    )

    @api.model
    def create(self, vals):
        result = super(SaleOrderInherit, self).create(vals)
        val = {
            'name': vals.get('name'),
            'partner_id': vals.get('partner_id'),
            'date_order': vals.get('date_order'),
            'loyalty_point': vals.get('loyalty_point')
        }
        print('ádasdasdsaddaasda')
        print(val)
        self.env['loyalty.history'].sudo().create(val)
        return result

    @api.onchange('order_line')
    def _onchange_points(self):
        for rec in self:
            print('-------------------------------', rec.tax_totals_json)
            rec.points_won = rec.amount_total + rec.points_acumulated
            rec.points_acumulating = rec.amount_total * rec.percent / 100
