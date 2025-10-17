{
    'name': 'Invoice Compact Layout',
    'version': '18.0.1.0.6',
    'category': 'Accounting/Accounting',
    'summary': 'DEFINITIVA - Spacing reduction based on real template code',
    'description': """
        Invoice Compact Layout - VERSIÓN DEFINITIVA v1.0.6
        ===================================================
        
        Esta versión está basada en el análisis del código fuente REAL de tus templates:
        - account.report_invoice_copy_1 (template principal)
        - account.report_invoice_document_copy_1
        - l10n_ar.report_invoice_document_copy_1 (localización argentina)
        
        Características v1.0.6:
        ✅ Herencia DIRECTA de los templates exactos que usas
        ✅ Reemplaza el CSS existente con versión ultra-específica
        ✅ 20 estrategias diferentes de compactación
        ✅ Sobrescribe customizaciones de Studio
        ✅ Compatible con localización argentina
        
        Qué hace:
        - Elimina el espacio entre "Inicio de actividades" y datos del cliente
        - Reduce márgenes y paddings en TODO el documento
        - Anula TODOS los margins/paddings de Bootstrap
        - Oculta elementos vacíos
        - Compacta tablas y textos
        
        Esta versión DEBE funcionar porque está hecha específicamente para
        tu estructura de templates.
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
