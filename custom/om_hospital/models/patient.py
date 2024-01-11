# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "hospital patient"
    _order = 'name asc'

    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        res['gender'] = 'other'
        res['age'] = 50
        res['note'] = 'Test default description'
        return res

    name = fields.Char(string="Name", required=True)
    reference = fields.Char(string="Order Reference", required=True,
                            copy=False, readonly=True, default=lambda self: _('New'))
    age = fields.Integer(string="Age", required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string="Description")
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')],
                             default='draft', string="Status", tracking=True)
    responsible_id = fields.Many2one('res.partner', string="Responsible")
    appointment_count = fields.Integer(string="Number of Appointments", compute='_compute_appointment_count')
    image = fields.Binary(string="Patient Image")
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string="Appointments")

    def _compute_appointment_count(self):
        appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = appointment_count

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

    @api.model
    def create(self, vals):

        if not vals.get('note'):
            vals['note'] = "New Patient"

        if vals.get('reference', _("New")) == _("New"):
            vals['reference'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient') or _("New")

        res = super(HospitalPatient, self).create(vals)
        return res

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            patients = self.env['hospital.patient'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if patients:
                raise ValidationError(_("The Name %s Already Exists in Record" % rec.name))

    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError("Age cannot be set as 0")

    def name_get(self):
        result = []
        for rec in self:
            name = '['+rec.reference+'] ' + rec.name + " " + str(rec.age)
            result.append((rec.id, name))
        return result
