from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_reference = fields.Char(string='Customer Reference')

    @api.model
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        template = self.env.ref('library_management.email_template_sale_order_confirmed')
        for order in self:
            template.send_mail(order.id, force_send=True)
        return res