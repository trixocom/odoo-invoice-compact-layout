{
    'name': 'Invoice Compact Layout',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Reduce spacing in invoice reports for better paper usage',
    'description': """
        Invoice Compact Layout
        ======================
        
        Este módulo optimiza el diseño de los reportes de factura para:
        - Reducir el espacio entre el encabezado y la información del cliente
        - Optimizar el uso del papel
        - Mantener la legibilidad del documento
        
        Características:
        - Espaciado compacto entre secciones
        - Tablas optimizadas
        - Compatible con Odoo 18
    """,
    'author': 'Tu Empresa',
    'website': 'https://github.com/trixocom/odoo-invoice-compact-layout',
    'license': 'LGPL-3',
    'depends': ['account'],
    'data': [
        'views/report_invoice_compact.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'odoo_invoice_compact/static/src/scss/report_invoice_compact.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
