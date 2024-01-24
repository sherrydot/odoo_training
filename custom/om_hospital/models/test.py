# # -*- coding: utf-8 -*-
# from odoo import api, fields, models, _
#
# access_hospital_test,access.hospital.test,model_hospital_test,,1,1,1,1
#
# class HospitalTest(models.Model):
#     _name = "hospital.test"
#     _inherit = ["mail.thread", "mail.activity.mixin"]
#     _description = "hospital test"
#     _rec_name = "test_name"
#
#     test_name = fields.Char(string="Name")
#
#     lahore = fields.Boolean(string="Lahore", invisible=True)
#     karachi = fields.Boolean(string="Karachi", invisible=True)
#     islamabad = fields.Boolean(string="Islamabad", invisible=True)
#
#     def toggle_lahore(self):
#         self.lahore = True
#
#     def toggle_karachi(self):
#         self.karachi = True
#
#     def toggle_islamabad(self):
#         self.islamabad = True
#
#     #
#     # def toggle_lahore(self):
#     #     # if self.lahore:
#     #     self.lahore = True
#     #     # else:
#     #     #     self.is_lahore_visible = False
#     #
#     # def toggle_karachi(self):
#     #     # if self.karachi:
#     #     self.karachi = True
#     #
#     # def toggle_islamabad(self):
#     #     # if self.islamabad:
#     #     self.islamabad = True
#
#     def reset_all(self):
#         self.lahore = False
#         self.karachi = False
#         self.islamabad = False

# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalTest(models.Model):
    # _name = "hospital.test"
    _inherit = 'sale.order'
    # _description = "hospital test"
    # _rec_name = "test_name"

    test_name = fields.Char(string="Name")

    lahore = fields.Boolean(string="Lahore", invisible=True)
    karachi = fields.Boolean(string="Karachi", invisible=True)
    islamabad = fields.Boolean(string="Islamabad", invisible=True)

    def toggle_lahore(self):
        self.karachi = False
        self.islamabad = False
        self.lahore = True

    def toggle_karachi(self):
        self.islamabad = False
        self.lahore = False
        self.karachi = True

    def toggle_islamabad(self):
        self.lahore = False
        self.karachi = False
        self.islamabad = True

    # def toggle_lahore(self):
    #     if self.lahore == False:
    #         self.lahore = not self.lahore
    #
    # def toggle_karachi(self):
    #     if self.karachi == False:
    #         self.karachi = not self.karachi
    #
    # def toggle_islamabad(self):
    #     if self.islamabad == False:
    #         self.islamabad = not self.islamabad

    def reset_all(self):
        self.lahore = False
        self.karachi = False
        self.islamabad = False
