from odoo import models,fields


class ToDOTask(models.Model):
    _name = 'todo.task'
    _description = 'ToDOTask'
    _inherit = ['mail.thread','mail.activity.mixin']


    task_name = fields.Char(string='Task Name', required=True)
    assign_to = fields.Many2one('users')
    description = fields.Char()
    due_date = fields.Date()
    status = fields.Selection([
        ('new','New'),
        ('in_progress','In Progress'),
        ('completed','Completed'),
    ])