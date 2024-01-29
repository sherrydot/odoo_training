from odoo import api, fields, models, _


class HospitalTest(models.Model):
    # _name = "hospital.test"
    _inherit = 'sale.order'
    # _description = "hospital test"
    # _rec_name = "test_name"

    test_name = fields.Char(string="Name")

    lahore = fields.Boolean(string="Lahore")
    karachi = fields.Boolean(string="Karachi")
    islamabad = fields.Boolean(string="Islamabad")

    def toggle_lahore(self):
        if self.lahore == False:
            self.lahore = not self.lahore

    def toggle_karachi(self):
        if self.karachi == False:
            self.karachi = not self.karachi

    def toggle_islamabad(self):
        if self.islamabad == False:
            self.islamabad = not self.islamabad

    def reset_all(self):
        self.lahore = False
        self.karachi = False
        self.islamabad = False
