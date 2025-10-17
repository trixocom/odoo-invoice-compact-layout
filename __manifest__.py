{
    'name': 'Invoice Compact Layout',
    'version': '18.0.1.0.2',
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
        - Approach ultra-agresivo para máxima compatibilidad
        
        Changelog v1.0.2:
        - Corregido: Herencia de templates base (web.external_layout_standard)
        - Mejorado: CSS ultra-agresivo que sobrescribe todo
        - Agregado: Soporte para múltiples variantes de reportes (copy, copy_1, etc)
        - Optimizado: Selectores CSS más específicos y fuertes
    """,
    'author': 'TrixoCom',
    'website': 'https://github.com/trixocom/odoo-invoice-compact-layout',
    'license': 'LGPL-3',
    'depends': ['account', 'web'],
    'data': [
        'views/report_invoice_compact.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
