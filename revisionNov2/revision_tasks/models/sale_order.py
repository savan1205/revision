from odoo import api, models, fields
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Order"

    total_lines = fields.Integer(compute="count_lines", string="Total Lines")

    credit_limit = fields.Float(
        related="partner_id.credit_limit", string="Credit Limit")
    block_limit = fields.Float(
        related="partner_id.block_limit", string="Block Limit")

    def action_fill_products(self):
        ctx = {'sale_id':self.id} 
        return {
            "type": "ir.actions.act_window",
            "res_model": "product.wizard",
            "view_mode": "form",
            "name": "Wizard name",
            "target":"new",
        }

    @api.model
    def create(self, vals):
        # for rec in self:
        # print("=======================================",res)
        # if res.amount_total > res.block_limit:
        #     raise ValidationError("Your Sale Order Credit Limit has been Exceeded.")
        quote_sale = super(SaleOrder, self).create(vals)
        quote_record = self.env['sale.order'].search(
            [('state', '=', 'draft'), ('partner_id', '=', self.partner_id.id)])
        total_sum_quote = 0
        for recc in quote_record:
            total_sum_quote += recc.amount_total
        if total_sum_quote > recc.credit_limit:
            raise ValidationError(
                "Your Sale Order Credit Limit has been Exceeded.")
        return quote_sale

    def action_confirm(self):
        print("---------------------------------------------------++++++++++++++++++++++++++++=",self.order_line.id)
        confirm_sale = super(SaleOrder, self).action_confirm()
        sale_records = self.env['sale.order'].search(
            ['&', ('state', '=', 'sale'), ('partner_id', '=', self.partner_id.id)])
        print("---------------------------------------", sale_records)
        total_sum = 0
        for rec in sale_records:
            total_sum += rec.amount_total
            print("---------------------------------------", total_sum)
        if total_sum > rec.block_limit:
            print("---------------------------------------", total_sum)
            raise ValidationError(
                "You cannot create SO as the Block Limit has been Exceeded")
        return confirm_sale

    def preview_sale_order_line(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Products',
            'view_mode': 'tree',
            'res_model': 'product.product',
            'domain': [('id', '=', self.order_line.product_id.ids)],
            'target': 'new',
            # 'context': "{'create': False}"
        }

    @api.depends('order_line')
    def count_lines(self):
        count = 0
        for rec in self.order_line:
            count += 1
        self.total_lines = count
