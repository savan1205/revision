from odoo import api, fields, models


class ProductWizard(models.TransientModel):
    _name = 'product.wizard'
    _description = 'Fill product into wizard'

    def get_lines(self):
        record=self.env['sale.order.line'].browse([103])
        return record


    order_line_ids=fields.One2many(comodel_name="sale.order.line",inverse_name="order_id",default=get_lines)

    def btn_split(self):\
    print("/////////////////////////////////////////////////////////Split Activated")
 

# class SaleOrederLine(models.Models):
#     _name = "sale.history"
#     _description="sale history"("///////////)


