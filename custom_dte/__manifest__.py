{
    'name': 'Custom DTE',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Customizations for DTE XML generation',
    'depends': ['account', 'l10n_cl'],  # Asegúrate de que dependas de los módulos necesarios
    'data': [
        'views/invoice_templates.xml',
    ],
    'installable': True,
}
