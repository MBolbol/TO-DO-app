from odoo import models,fields


class Users(models.Model):
    _name = 'users'


    name = fields.Char(required=True)
    phone = fields.Char(size = 11)
    address = fields.Char()

   