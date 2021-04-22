# -*- coding: utf-8 -*-
from odoo import http

             
class cibertec(http.Controller):
    @http.route('/cibertec/', auth='public',website=True)
    def index(self, **kw):
        courses = http.request.env['cibertec.course']
        return http.request.render('cibertec.index',{
            'courses':courses.search([])
        })                 

#     @http.route('/cibertec/cibertec/objects/', auth='public')
#     def list(self, **kw): 
#         return http.request.render('cibertec.listing', {
#             'root': '/cibertec/cibertec',
#             'objects': http.request.env['cibertec.cibertec'].search([]),
#         })

#     @http.route('/cibertec/cibertec/objects/<model("cibertec.cibertec"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cibertec.object', {
#             'object': obj
#         })
