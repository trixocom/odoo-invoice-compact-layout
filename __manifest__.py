{
    'name': 'Invoice Compact Layout',
    'version': '18.0.1.0.1',
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
        - Approach simplificado para máxima compatibilidad
        
        Changelog v1.0.1:
        - Corregido: Uso de XPath simplificado para mejor compatibilidad
        - Mejorado: CSS inline en lugar de archivo SCSS
        - Optimizado: Prioridad 99 para evitar conflictos
    """,
    'author': 'TrixoCom',
    'website': 'https://github.com/trixocom/odoo-invoice-compact-layout',
    'license': 'LGPL-3',
    'depends': ['account'],
    'data': [
        'views/report_invoice_compact.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
