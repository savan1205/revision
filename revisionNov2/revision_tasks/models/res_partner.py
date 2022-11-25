from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_limit_check = fields.Boolean(string="Credit Limit Check")
    block_limit_check = fields.Boolean(string="Block Limit Check")

    credit_limit = fields.Float(string="Credit Limit")
    block_limit = fields.Float(string="Block Limit")
    


    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = list(args or [])
        if name:

            args +=  ['|', '|', '|','|', ('name', operator, name),('function', operator, name), ('phone', operator, name), ('email', operator, name), ('state_id.name', operator, name)]
            print("------------------------------------------------args",args)
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)



    # def name_get(self):
    #   result = [] 

    #   for rec in self:
    #       result.append((rec.id,"%s-%s"%(rec.name,rec.function)))
    #   return result


