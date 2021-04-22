from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'
    
    student = fields.Boolean(string="Estudiante",default=False) 
    course_ids = fields.Many2many('cibertec.course', string='Cursos')
    student_progress_ids = fields.One2many('cibertec.progress','student_id', string="Progreso de Estudiante")
    
    student_content_progress = fields.One2many('cibertec.contentpro','student_id',string="Progreso de contenido")
