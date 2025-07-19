# -*- coding: utf-8 -*-
# from odoo import http


# class SteadfastDelivery(http.Controller):
#     @http.route('/steadfast_delivery/steadfast_delivery', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/steadfast_delivery/steadfast_delivery/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('steadfast_delivery.listing', {
#             'root': '/steadfast_delivery/steadfast_delivery',
#             'objects': http.request.env['steadfast_delivery.steadfast_delivery'].search([]),
#         })

#     @http.route('/steadfast_delivery/steadfast_delivery/objects/<model("steadfast_delivery.steadfast_delivery"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('steadfast_delivery.object', {
#             'object': obj
#         })

