from odoo import models, fields, api

class NoticeBanner(models.Model):
    _name = 'bill_banner.notice_banner'
    _description = 'System Notice Banner'

    name = fields.Char(string="Title", required=True)
    message = fields.Text(string="Notice Message", required=True)
    is_active = fields.Boolean(string="Is Active", default=False)
    display_type = fields.Selection([
        ('all', 'System-wide'),
        ('employee', 'Specific Employee')
    ], string='Display Type', default='all')
    employee_ids = fields.Many2many('hr.employee', string='Employees')

    def toggle_active(self):
        """Toggle the active status of the notice banner."""
        for record in self:
            record.is_active = not record.is_active