# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderEntregaStarx(http.Controller):
#     @http.route('/sale_order_entrega_starx/sale_order_entrega_starx/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_entrega_starx/sale_order_entrega_starx/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_entrega_starx.listing', {
#             'root': '/sale_order_entrega_starx/sale_order_entrega_starx',
#             'objects': http.request.env['sale_order_entrega_starx.sale_order_entrega_starx'].search([]),
#         })

#     @http.route('/sale_order_entrega_starx/sale_order_entrega_starx/objects/<model("sale_order_entrega_starx.sale_order_entrega_starx"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_entrega_starx.object', {
#             'object': obj
#         })
