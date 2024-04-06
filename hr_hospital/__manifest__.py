{
    'name': 'Hospital',
    'summary': 'Hospital management',

    'author': 'Vasyl Sembrak',
    'website': '',

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.0.0.1',

    'depends': [
        'base',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/diseases_views.xml',
        'views/doctor_views.xml',
        'views/pacient_views.xml',
        'views/pacient_visits_views.xml',
        'wizard/change_doctor_wizard_views.xml',
        'wizard/disease_report_wizard_views.xml',
    ],

    'demo': [
        'demo/doctor_demo.xml',
        'demo/pacient_demo.xml',
        'demo/disease_demo.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    'images': [
        'static/description/icon.png',
    ],

    'price': 100,
    'currency': 'EUR',
}
