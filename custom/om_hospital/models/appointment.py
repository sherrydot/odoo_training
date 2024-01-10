# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "hospital appointment"

    name = fields.Char(string="Order Reference", required=True,
                            copy=False, readonly=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    age = fields.Integer(string="Age", required=True, related='patient_id.age', tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')],
                             default='draft', string="Status", tracking=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    note = fields.Text(string="Description", related='patient_id.note')
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Date and Time")

    def action_confirm(self):
        if self.state == 'draft':
            self.state = 'confirm'
        else:
            pass

    def action_done(self):
        if self.state == 'confirm':
            self.state = 'done'
        else:
            pass

    def action_draft(self):
        if self.state == 'cancel':
            self.state = 'draft'
        else:
            pass

    def action_cancel(self):
        self.state = 'cancel'

    def button_done(self):
        self.state = 'done'


    @api.model
    def create(self, vals):

        if not vals.get('note'):
            vals['note'] = "New Patient"

        if vals.get('name', _("New")) == _("New"):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'hospital.appointment') or _("New")

        res = super(HospitalAppointment, self).create(vals)
        return res

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender = self.patient_id.gender
            if self.patient_id.note:
                self.note = self.patient_id.note
        else:
            self.gender = ''
            self.note = ''