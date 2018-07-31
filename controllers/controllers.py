# -*- coding: utf-8 -*-
from odoo import http

# class NewConnections(http.Controller):
#     @http.route('/new_connections/new_connections/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_connections/new_connections/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_connections.listing', {
#             'root': '/new_connections/new_connections',
#             'objects': http.request.env['new_connections.new_connections'].search([]),
#         })

#     @http.route('/new_connections/new_connections/objects/<model("new_connections.new_connections"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_connections.object', {
#             'object': obj
#         })