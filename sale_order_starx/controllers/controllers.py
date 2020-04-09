# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderStarx(http.Controller):
#     @http.route('/sale_order_starx/sale_order_starx/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_starx/sale_order_starx/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_starx.listing', {
#             'root': '/sale_order_starx/sale_order_starx',
#             'objects': http.request.env['sale_order_starx.sale_order_starx'].search([]),
#         })

#     @http.route('/sale_order_starx/sale_order_starx/objects/<model("sale_order_starx.sale_order_starx"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_starx.object', {
#             'object': obj
#         })
