# -*- coding: utf-8 -*-
{
    'name': "Customized Invoicing",

    'summary': """
        Send Invoices and Track Payments'""",

    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
   
    """,

    'author': "Pravitha V",
    'website': "https://www.odoo.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'product', 'analytic', 'report', 'web_planner', 'base'],

    # always loaded
    'data': [
        'views/account_report.xml',
        'wizard/account_report_partner_statement_view.xml',
        'views/report_partnerstatement.xml',
        ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
