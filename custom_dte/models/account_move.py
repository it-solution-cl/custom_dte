from odoo import models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def _prepare_dte_amounts(self):
        amounts = super()._prepare_dte_amounts()
        amounts['amount_untaxed'] = self.amount_untaxed
        return amounts
