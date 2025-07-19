{
    'name': 'SteadFast bangladesh Courier Integration',
    'version': '17.0.1.3',
    'summary': 'Send Sale Quotations to SteadFast Courier',
    'description': 'Integrate Odoo Sales with SteadFast Courier API for delivery order creation. Returns the raw response from steadfast api and keeps it with the sales order. Checks for the delivery update twice from Steadfast, and changes the delivery status accordingly',
    'author': 'Taxample.com',
    'website': 'https://odoo.taxample.com',
    'category': 'Sales',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/steadfast_config_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'price': 85,
    'currency': 'USD'
}
