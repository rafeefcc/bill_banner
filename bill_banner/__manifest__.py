{
    'name': "bill_banner",
    'summary': "Showcase a Banner System-wide by admin Notice",

    'description': """
    This module is designed to show a simple system-wide banner which serves as a notice to all users.
    The system admin can enable or disable the notice at will. The banner does not interfere with the
    daily operations of Odoo, but it effectively displays notices on each screen, such as penalty notices.
    """,

    'author': "Taxample.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '17.0.2.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/notice_banner_views.xml',
        'views/notice_banner_actions.xml',
        'views/notice_banner_menus.xml',
        'views/notice_banner_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'bill_banner/static/src/js/notice_banner.js',
            'bill_banner/static/src/css/notice_banner.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'images': ['bill_banner/static/description/icon.png'],
    'icon': 'bill_banner/static/description/icon.png',
    'price': 11.00,
    'currency': 'USD'
}
