from odoo import models, fields, api

class Tags(models.Model):
    _name="cibertec.tag"
    _description="tags"

    name=fields.Text(string="Etiqueta")
    active_id = fields.Boolean(default=True, string="Activo")