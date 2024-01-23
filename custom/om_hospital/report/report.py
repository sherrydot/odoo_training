# -*- coding: utf-8 -*-

from odoo import models, api


class AppointmentReport(models.AbstractModel):
    _name = 'appointment.report'

    @api.model
    def action_print_report(self, patient_id, data=None):
        docs = self.env['om_hospital.action_report_appointment'].browse(patient_id)
        data = {
            'patient': patient_id,
            'doc_model': 'hospital.appointment',
            'docs': docs,
            'data': data,
        }
