from odoo import http
from odoo.http import request
import json

class NoticeBannerController(http.Controller):
    
    @http.route('/get_notice_banner', type='json', auth='user')
    def get_notice_banner(self):
        """Get active notice banner data"""
        try:
            # Get the active notice banner
            user = request.env.user
            employee = request.env['hr.employee'].search([('user_id', '=', user.id)], limit=1)
            
            all_notices = request.env['bill_banner.notice_banner']

            # Search for system-wide notices
            system_notices = all_notices.search([
                ('is_active', '=', True),
                ('display_type', '=', 'all')
            ])
            
            employee_notices = all_notices
            # Search for employee-specific notices if employee exists
            if employee:
                employee_notices = all_notices.search([
                    ('is_active', '=', True),
                    ('display_type', '=', 'employee'),
                    ('employee_ids', 'in', [employee.id])
                ])

            # Combine all relevant notices
            notices = system_notices + employee_notices

            if notices:
                # Concatenate all messages into a single string
                concatenated_message = " | ".join([f"{notice.name}: {notice.message}" for notice in notices])
                return {
                    'is_active': True,
                    'messages': [concatenated_message], # Return as a single-element array
                    'ids': notices.ids
                }
            else:
                return {
                    'is_active': False,
                    'messages': [], # Return empty array
                    'ids': []
                }
        except Exception as e:
            return {
                'is_active': False,
                'message': '',
                'id': False
            }