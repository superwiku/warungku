# -*- coding: utf-8 -*-
# from odoo import http


# class Warungku(http.Controller):
#     @http.route('/warungku/warungku/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/warungku/warungku/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('warungku.listing', {
#             'root': '/warungku/warungku',
#             'objects': http.request.env['warungku.warungku'].search([]),
#         })

#     @http.route('/warungku/warungku/objects/<model("warungku.warungku"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('warungku.object', {
#             'object': obj
#         })
