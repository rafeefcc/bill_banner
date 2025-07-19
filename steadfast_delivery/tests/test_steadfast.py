from odoo.tests.common import TransactionCase
import json

class TestSteadfastDelivery(TransactionCase):

    def setUp(self):
        super().setUp()
        self.company = self.env.company
        self.partner = self.env['res.partner'].create({
            'name': 'John Doe',
            'phone': '01234567890',
            'street': '123 Main St',
            'city': 'Dhaka',
        })
        self.sale_order = self.env['sale.order'].create({
            'partner_id': self.partner.id,
            'company_id': self.company.id,
            'order_line': [(0, 0, {
                'name': 'Test Product',
                'product_uom_qty': 1,
                'price_unit': 100,
                'product_id': self.env.ref('product.product_product_4').id,
            })],
        })
        self.config = self.env['steadfast.config'].create({
            'company_id': self.company.id,
            'api_key': 'dummy_key',
            'secret_key': 'dummy_secret',
            'base_url': 'https://portal.packzy.com/api/v1',
        })

    def test_send_to_steadfast(self):
        import requests
        from unittest.mock import patch, MagicMock

        fake_response = MagicMock()
        fake_response.status_code = 200
        fake_response.json.return_value = [{
            'invoice': self.sale_order.name,
            'tracking_code': 'FAKETRACK',
            'consignment_id': '12345',
            'status': 'success'
        }]

        with patch.object(requests, 'post', return_value=fake_response):
            self.sale_order.action_send_to_steadfast()

        self.assertEqual(self.sale_order.steadfast_tracking_code, 'FAKETRACK')
        self.assertEqual(self.sale_order.steadfast_status, 'success')
