from odoo import api, fields, models


class ReasonWizard(models.TransientModel):
    _name = 'reason.wizard'
    _description = 'Reason'


    name=fields.Char(string="reason")
 