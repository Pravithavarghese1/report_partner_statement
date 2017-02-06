# -*- coding: utf-8 -*-
from odoo import http

# class QprAccount(http.Controller):
#     @http.route('/qpr_account/qpr_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qpr_account/qpr_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qpr_account.listing', {
#             'root': '/qpr_account/qpr_account',
#             'objects': http.request.env['qpr_account.qpr_account'].search([]),
#         })

#     @http.route('/qpr_account/qpr_account/objects/<model("qpr_account.qpr_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qpr_account.object', {
#             'object': obj
#         })