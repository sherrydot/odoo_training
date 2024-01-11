# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "hospital doctor"
    _rec_name = "doctor_name"

    doctor_name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Integer(string="Age", required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string="Description")
    image = fields.Binary(string="Doctor Image")

    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('doctor_name'):
            default['doctor_name'] = _("%s (Copy)", self.doctor_name)
        default['note'] = ""
        return super(HospitalDoctor, self).copy(default)
