{
    'name': 'Invoice Compact Layout',
    'version': '18.0.2.0.0',
    'category': 'Accounting/Accounting',
    'summary': '🔥 DEFINITIVO v2.0.0 - CSS Reset Nuclear en external_layout_standard',
    'description': """
        Invoice Compact Layout - v2.0.0 🔥 DEFINITIVO
        =============================================
        
        🎯 CAMBIO RADICAL v2.0.0: SOLUCIÓN NUCLEAR
        
        Esta versión usa un approach completamente diferente:
        ✅ Modifica external_layout_standard (el layout que TODOS usan)
        ✅ CSS Reset completo con * { margin: 0; padding: 0; }
        ✅ Inyecta estilos DENTRO del body (Odoo lo procesa en PDFs)
        ✅ !important en ABSOLUTAMENTE TODO
        ✅ Compatible con localización argentina y customizaciones
        
        POR QUÉ las versiones anteriores NO funcionaban:
        ❌ v1.x: CSS inline en templates NO se procesa bien en PDFs
        ❌ v1.x: Assets SCSS requieren compilación que no ocurría
        ❌ v1.x: Heredábamos templates específicos, no el layout base
        
        POR QUÉ esta versión SÍ funciona:
        ✅ Modifica external_layout_standard = afecta TODO
        ✅ CSS inyectado en body = Odoo lo procesa en PDFs
        ✅ Reset completo = sobrescribe TODO (Bootstrap, Studio, etc)
        ✅ Selector * = máxima prioridad + !important
        
        Qué hace:
        - Elimina COMPLETAMENTE el espacio entre encabezado y cliente
        - Reset de margins/padding en TODO el documento
        - Line-height compacto (1.15) para mejor uso del papel
        - Oculta divs vacíos automáticamente
        - Compacta tablas manteniendo legibilidad
        - Anula TODAS las clases de Bootstrap (mt-*, mb-*, pt-*, pb-*)
        - Sobrescribe estilos inline si existen
        
        Instalación:
        ============
        1. cd /mnt/extra-addons/odoo-invoice-compact-layout
        2. git pull origin main
        3. systemctl restart odoo
        4. Apps → Invoice Compact Layout → DESINSTALAR
        5. Apps → Invoice Compact Layout → INSTALAR
        6. Imprimir factura → CTRL+F5 para limpiar caché
        7. ¡LISTO! 🎉
        
        Importante:
        - Si ya tenías instalado el módulo, DEBES desinstalar y reinstalar
        - NO basta con actualizar, hay que reinstalar completamente
        - Después de reinstalar, hacer CTRL+F5 en el navegador
        
        Compatibilidad:
        ✅ Odoo 18.0
        ✅ Localización Argentina (l10n_ar)
        ✅ Customizaciones de Studio
        ✅ Todos los tipos de reportes de factura
        
        Esta ES la solución definitiva. Si no funciona con esta versión,
        el problema es otro (caché de assets, permisos, etc).
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
