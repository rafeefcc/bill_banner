from odoo import models, fields

class SteadfastConfig(models.Model):
    _name = 'steadfast.config'
    _description = 'SteadFast Courier Configuration'
    _rec_name = 'company_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company, ondelete='cascade')
    api_key = fields.Char('API Key', required=True, tracking=True)
    secret_key = fields.Char('Secret Key', required=True, tracking=True)
    base_url = fields.Char('API Base URL', default='https://portal.steadfast.com.bd/api/v1', required=True)

    _sql_constraints = [
        ('company_unique', 'unique(company_id)', 'Each company can only have one SteadFast configuration.')
    ]