{
    'name': 'Hospital Management',
    'website': 'gg.hospital.com',
    'description': """Hospital Management Software""",
    'sequence': -100,
    'summary': """Hospital Management Software""",
    'version': '1.0',
    'category': 'Human Resources/Fleet',
    'depends': [
        'sale',
        'mail',
        'website_slides',
        'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'views/patient_view.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/appointment_view.xml',
        'views/sale.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
