# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PatientCardXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_id_card_xls'
    _inherit = 'report.report_xlsx.abstract'

    @staticmethod
    def generate_xlsx_report(workbook, data, patients):
        sheet = workbook.add_worksheet('Patient ID Card')
        preset_1 = workbook.add_format({'bold': True, 'align': 'center',
                                        'bg_color': 'gray', 'color': 'black'})
        preset_2 = workbook.add_format({'align': 'center',
                                        'bg_color': 'gray', 'color': 'black'})
        center = workbook.add_format({'align': 'center'})

        row = 5
        col = 5
        total = 0
        sheet.set_column('J:J', 15)

        sheet.write(row, col, 'Name', preset_1)
        sheet.write(row, col + 1, 'Age', preset_1)
        sheet.write(row, col + 2, 'Gender', preset_1)
        sheet.write(row, col + 3, 'Status', preset_1)
        sheet.write(row, col + 4, 'Description', preset_1)

        for obj in patients:
            sheet.write(row + 1, col, obj.name)
            sheet.write(row + 1, col + 1, obj.age)
            sheet.write(row + 1, col + 2, obj.gender)
            sheet.write(row + 1, col + 3, obj.state)
            sheet.write(row + 1, col + 4, obj.note)
            row += 1
            total += 1

        sheet.merge_range(row + 3, col + 2, row + 3, col + 3, 'Total Patients:', preset_2)
        sheet.write(row + 3, col + 4, total, center)
