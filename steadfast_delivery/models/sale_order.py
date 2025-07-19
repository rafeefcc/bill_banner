from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
import json

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    steadfast_tracking_code = fields.Char(string="SteadFast Tracking Code")
    steadfast_consignment_id = fields.Char(string="SteadFast Consignment ID")
    steadfast_status = fields.Char(string="SteadFast Status")
    steadfast_response_json = fields.Text(string="SteadFast Raw Response")

    def action_send_to_steadfast(self):
        config = self.env['steadfast.config'].sudo().search([
            ('company_id', '=', self.env.company.id)
        ], limit=1)

        if not config:
            raise UserError("Please configure SteadFast API credentials for your company.")

        headers = {
            'api_key': config.api_key,
            'secret_key': config.secret_key,
        }
        url = f"{config.base_url}/orders/bulk"

        orders_data = []
        order_map = {}

        for order in self:
            if not order.partner_id.phone or not order.partner_id.contact_address:
                raise UserError(f"Missing phone or address for order {order.name}")

            payload = {
                'invoice': order.name,
                'recipient_name': order.partner_id.name,
                'recipient_phone': order.partner_id.phone,
                'recipient_address': order.partner_id.contact_address,
                'cod_amount': order.amount_total,
                'note': order.note or ''
            }
            orders_data.append(payload)
            order_map[order.name] = order

        response = requests.post(url, json=orders_data, headers=headers)
        if response.status_code == 200:
            results = response.json()
            for result in results:
                order = order_map.get(result.get("invoice"))
                if order:
                    order.write({
                        'steadfast_tracking_code': result.get("tracking_code"),
                        'steadfast_consignment_id': result.get("consignment_id"),
                        'steadfast_status': result.get("status"),
                        'steadfast_response_json': json.dumps(result)
                    })
        else:
            raise UserError(f"SteadFast API Error: {response.text}")