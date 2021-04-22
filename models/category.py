from odoo import models, fields, api


class Category(models.Model):
    _name = 'cibertec.category'
    _description = 'category'

    name = fields.Text()
    description = fields.Text()
    active_id = fields.Boolean(default=True, string="Activo")
    