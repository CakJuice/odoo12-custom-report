# -*- coding: utf-8 -*-
{
    'name': "Custom Report Odoo 12",

    'summary': """
        Custom Report Example for Odoo 12""",

    'description': """
        Custom report for practice purpose
    """,

    'author': "Cak Juice",
    'website': "https://cakjuice.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_attendance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'wizards/recap.xml',
        'reports/recap.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}