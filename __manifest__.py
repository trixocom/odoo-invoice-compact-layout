{
    'name': 'Invoice Compact Layout',
    'version': '18.0.1.0.8',
    'category': 'Accounting/Accounting',
    'summary': 'FIXED - XML structure corrected with data tag',
    'description': """
        Invoice Compact Layout - v1.0.8 FIXED
        ======================================
        
        Cambio v1.0.8: 🔧 CRITICAL FIX - Estructura XML corregida
        - ✅ Agregado tag <data> requerido por Odoo
        - ✅ Resuelve: "Element odoo has extra content: template, line 16"
        - ✅ Ahora el módulo puede instalarse/actualizarse sin errores
        
        Cambio v1.0.7: Corregido error de validación XML
        - Cambio de position="replace" a position="after"
        - Ahora el CSS se AGREGA en lugar de reemplazar
        - Validación XML correcta
        
        Esta versión está basada en el análisis del código fuente REAL de tus templates:
        - account.report_invoice_copy_1 (template principal)
        - account.report_invoice_document_copy_1
        - l10n_ar.report_invoice_document_copy_1 (localización argentina)
        
        Características:
        ✅ Herencia DIRECTA de los templates exactos que usas
        ✅ CSS ultra-específico con máxima prioridad
        ✅ 20 estrategias diferentes de compactación
        ✅ Sobrescribe customizaciones de Studio
        ✅ Compatible con localización argentina
        ✅ Validación XML CORRECTA (tag <data> agregado)
        
        Qué hace:
        - Elimina el espacio entre "Inicio de actividades" y datos del cliente
        - Reduce márgenes y paddings en TODO el documento
        - Anula TODOS los margins/paddings de Bootstrap
        - Oculta elementos vacíos
        - Compacta tablas y textos
        
        Instalación:
        1. git pull en tu servidor Odoo
        2. Actualizar módulo desde Apps
        3. El error XML ya no aparecerá ✓
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
