# -*- coding: utf-8 -*-
from odoo import http

# class CustomReportV12(http.Controller):
#     @http.route('/custom_report_v12/custom_report_v12/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_report_v12/custom_report_v12/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_report_v12.listing', {
#             'root': '/custom_report_v12/custom_report_v12',
#             'objects': http.request.env['custom_report_v12.custom_report_v12'].search([]),
#         })

#     @http.route('/custom_report_v12/custom_report_v12/objects/<model("custom_report_v12.custom_report_v12"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_report_v12.object', {
#             'object': obj
#         })