{
    'name': 'Invoice Compact Layout',
    'version': '18.0.1.0.3',
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
        - Espaciado compacto entre secciones mediante CSS
        - Tablas optimizadas
        - Compatible con Odoo 18
        - Approach ultra-simplificado - solo CSS global
        
        Changelog v1.0.3:
        - Corregido: XPath simplificado a solo //head (siempre existe)
        - Simplificado: Un solo template que agrega CSS global
        - Compatible: Funciona con CUALQUIER reporte de Odoo
    """,
    'author': 'TrixoCom',
    'website': 'https://github.com/trixocom/odoo-invoice-compact-layout',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'views/report_invoice_compact.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
