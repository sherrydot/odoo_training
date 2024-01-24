# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalTest(models.Model):
    _name = "hospital.test"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "hospital test"
    _rec_name = "test_name"

    test_name = fields.Char(string="Name")

    lahore = fields.Boolean(string="Lahore")
    karachi = fields.Boolean(string="Karachi")
    islamabad = fields.Boolean(string="Islamabad")

    # is_lahore_visible = fields.Boolean(string="is lahore visible", default=False)
    # is_karachi_visible = fields.Boolean(string="is karachi visible", default=False)
    # is_islamabad_visible = fields.Boolean(string="is islamabad visible", default=False)

    # def toggle_lahore(self):
    #     self.write({'is_lahore_visible': True, 'is_karachi_visible': False, 'is_islamabad_visible': False})
    #     return True
    #
    # def toggle_karachi(self):
    #     self.write({'is_karachi_visible': True, 'is_lahore_visible': False, 'is_islamabad_visible': False})
    #     return True
    #
    # def toggle_islamabad(self):
    #     self.write({'is_islamabad_visible': True, 'is_karachi_visible': False, 'is_lahore_visible': False})
    #     return True

    def toggle_lahore(self):
        # if self.lahore:
        self.lahore = True
        self.karachi = False
        self.islamabad = False
        # else:
        #     self.is_lahore_visible = False

    def toggle_karachi(self):
        # if self.karachi:
        self.karachi = True
        self.lahore = False
        self.islamabad = False

    def toggle_islamabad(self):
        # if self.islamabad:
        self.islamabad = True
        self.karachi = False
        self.lahore = False

    def reset_all(self):
        self.lahore = False
        self.karachi = False
        self.islamabad = False
