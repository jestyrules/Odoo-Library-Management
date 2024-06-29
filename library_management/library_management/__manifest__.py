{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage library books',
    'author': 'Jerin G Johnson',
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/sale_order_views.xml',
        'report/sale_report_templates.xml',
    ],
    'installable': True,
    'application': True,
}
