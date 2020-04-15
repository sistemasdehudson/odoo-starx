# -*- coding: utf-8 -*-
# from odoo import http


# class StockEntregasStarx(http.Controller):
#     @http.route('/stock_entregas_starx/stock_entregas_starx/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_entregas_starx/stock_entregas_starx/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_entregas_starx.listing', {
#             'root': '/stock_entregas_starx/stock_entregas_starx',
#             'objects': http.request.env['stock_entregas_starx.stock_entregas_starx'].search([]),
#         })

#     @http.route('/stock_entregas_starx/stock_entregas_starx/objects/<model("stock_entregas_starx.stock_entregas_starx"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_entregas_starx.object', {
#             'object': obj
#         })
