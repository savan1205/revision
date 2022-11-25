from odoo import api,fields,models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    state = fields.Char(related="company_id.state",readonly=False,string='state')


class CompanyInherit(models.Model):
    _inherit = "res.company"
    _description = "Company"

    state = fields.Char(string='state')    


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order"


    def action_post(self):
        
        self.env.user.company_id.state