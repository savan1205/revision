from odoo import api, fields, models, _


class CompanyCompany(models.Model):
    _name = "company.company"
    _description = "Company"

    name = fields.Char(string="Name")
    product_ids = fields.Many2many("product.product", string="Product")
    partner_id = fields.Many2one("res.partner", string="partner")
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales order'),
        ('cancel', 'Cancelled'),
    ], default="draft", readonly=False, string="State")
    sequence_number = fields.Char(
        string="Order number", copy=False, readonly=True, default=lambda self: _('New'))

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['reference_no'] = self.env['ir.sequence'].next_by_code(
    #            'company.company') or _('New')
    #     res = super(CompanyCompany, self).create(vals)
    #     return res

    @api.model
    def create(self, vals):
        if vals.get('sequence_number', _('New')) == _('New'):
            vals['sequence_number'] = self.env['ir.sequence'].next_by_code(
                'company.company') or _('New')
        res = super(CompanyCompany, self).create(vals)
        return res

    def action_create(self):
        for records in self:
            new_so = self.env['salesale.order'].new({
                'partner_id': records.partner_id,
                'state': records.state
            })

            new_so.onchange_partner_id()
            vals = new_so._convert_to_write(new_so._cache)
            created_so = self.env['sale.order'].create(vals)

            values = []
            for product in records.product_ids:
                print("+=======================================", product)
                line = values.append((0, 0, {
                    'product_id': product.id
                }))

            created_so.write({
                'order_line': values
            })


class Myclass(models.Model):
    _name = "my.model"


    name=fields.Char(string=" My Name")
