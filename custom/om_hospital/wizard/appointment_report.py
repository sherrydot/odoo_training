# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


# Transient model does not store data in a database
class AppointmentReportWizard(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Print Appointment Wizard"

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('other', 'Other'),
    # ], tracking=True, store=True, related='patient_id.gender')
    # doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    # date_appointment = fields.Date(string="Date")

    def action_print_report(self):
        appointments = self.env['hospital.appointment'].search_read([])
        data = {
            'form': self.read()[0],
            'appointments': appointments
        }

        return self.env.ref('om_hospital.action_report_appointment').report_action(self, data=data)
