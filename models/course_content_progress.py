# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course(models.Model):
    _name="cibertec.course"
    _description="courses"

    name=fields.Text(string="Título de Curso",required=True)
    tag_ids = fields.Many2many('cibertec.tag',string="Course Tags")
    content_ids = fields.One2many('cibertec.content','course_id')
    description= fields.Text()   
    color = fields.Integer()
    active_id= fields.Boolean(default=True,string="Activo")
    course_img = fields.Image(Attachment=True)
    
    partner_ids = fields.Many2many('res.partner',string="Usuarios")#relation='cibertec_res_partner_students_rel'

    category_id = fields.Many2one('cibertec.category',ondelete='set null',index=True)

    content_count = fields.Integer(default=0,compute="_content_count",store=True)
    student_pro_ids = fields.One2many('cibertec.progress','course_id')

    course_content_progress = fields.One2many('cibertec.contentpro','course_id')

    @api.depends('content_ids')
    def _content_count(self):
        for i in self:
            if len(i.content_ids) == 0:
                i.content_count = 0
            else:
                i.content_count = len(i.content_ids) 


    def action_viewstudents(self):
        domain = [('id','in',self.partner_ids.ids)]
        return {
		'name':'Students',
		'type': 'ir.actions.act_window',
		'res_model': 'res.partner',
		'view_mode': 'tree,form',
        'domain': domain,
	}

    def course_student_progress(self):
        students = self.env['res.partner'].search([('student','=',True),('course_ids.id','in',self.ids)])
        self.student_pro_ids.unlink()
        for rec in students:
            objProgress = False
            for i in rec.student_content_progress:
                if i.course_id.id == self.id and i.content_is_done == True: 
                    print("--------",i.course_id.name)
                    print("--------",rec.id)
                    print("--------",rec.name)
                    print("--------",self.id)
                    print("--------",self.name)
                    
                    dictionary = {
                                'course_id': self.id,
                                 'student_id': rec.id,
                                } 
                    objProgress = self.env['cibertec.progress'].create(dictionary)
                    break
            if not objProgress:
                dictionary = {
                                'course_id': self.id,
                                 'student_id': rec.id,
                                } 
                self.env['cibertec.progress'].create(dictionary)

                        
                    
     

class Content(models.Model):
    _name="cibertec.content"
    _description="contents"

    name=fields.Text(required=True)
    content_type = fields.Selection([('infographic','Infografía'),
                                      ('presentation','Presentación'),
                                      ('document','Documento'),
                                      ('webpage','Sitio Web'),
                                      ('video','Video'),
                                      ('quiz','Preguntas')],required=True)
    duration = fields.Float(digits=(6,2),help="Duración en horas")
    active_id = fields.Boolean(default=True, string="Activo")
    course_id = fields.Many2one('cibertec.course',required=True,string="Cursos")
    risponsible_ids = fields.Many2one('res.partner',ondelete="set null", index=True,string="Responsable")
    date_published = fields.Date(default=fields.Date.today)
    datas = fields.Binary(string="Adjunto")
    url = fields.Binary()
    description = fields.Text()
    color = fields.Integer()
    mime_type = fields.Char()
    partner_ids = fields.Many2many('res.partner',string="Usuarios")

    content_content_progress = fields.One2many('cibertec.contentpro','content_id')
 
    #@api.constrains('risponsible_ids','partner_ids')
    #def _check_risponsible_not_a_student(self):

    #   for j in self:
    #      print(j.risponsible_ids,j.partner_ids)
    #     if j.risponsible_ids and (j.risponsible_ids in j.partner_ids):
                
    #        raise exceptions.ValidationError("The Content's responsible cannot be an student")



class student_progress(models.Model):
    _name='cibertec.progress'
    _description = 'progress'

    course_id = fields.Many2one('cibertec.course',string="Cursos")
    student_id = fields.Many2one('res.partner',string='Estudiantes',domain = [('student','=',True)])
    content_done_count = fields.Integer(compute="_get_content_count",store=True)
    progress = fields.Float(compute="_get_content_count",store=True) 
    
    @api.depends('student_id','course_id')
    def _get_content_count(self):
        for rec in self:
            can=0
            for s in rec.student_id.student_content_progress:
                if rec.course_id == s.course_id:
                    can+=int(s.content_is_done)

            rec.content_done_count = can
            rec.progress = 100.0 * can / len(rec.course_id.content_ids)


class content_progress(models.Model):
    _name = 'cibertec.contentpro'
    _description = 'contentpro'

    course_id = fields.Many2one('cibertec.course',string='Cursos')
    content_id = fields.Many2one('cibertec.content',string='Contenidos')
    student_id = fields.Many2one('res.partner',string='Estudiantes',domain=[('student','=',True)])
    content_is_done = fields.Boolean(default=False)


