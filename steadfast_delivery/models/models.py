# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class steadfast_delivery(models.Model):
#     _name = 'steadfast_delivery.steadfast_delivery'
#     _description = 'steadfast_delivery.steadfast_delivery'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

