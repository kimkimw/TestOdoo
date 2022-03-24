from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    # _name = 'res.config.setting'
    _inherit = 'res.config.settings'

    loyalty_email_notify = fields.Boolean(default=False)
