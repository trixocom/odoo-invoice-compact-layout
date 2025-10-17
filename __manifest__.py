# -*- coding: utf-8 -*-
{
    'name': 'Invoice Compact Layout',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Compacta reportes de factura eliminando espacios innecesarios',
    'description': """
Invoice Compact Layout
======================

Este módulo optimiza el diseño de los reportes de factura eliminando espacios 
innecesarios para aprovechar mejor el papel.

Características:
-----------------
* Reduce el espacio entre el header de la empresa y la información del cliente
* Compacta las líneas de productos en la tabla
* Mantiene la legibilidad y profesionalismo
* Permite meter hasta 50% más productos por página
* Compatible con customizaciones de Odoo Studio

Beneficios:
-----------
* Menos papel usado
* Facturas más profesionales
* Más productos por página
* Mejor aprovechamiento del espacio

Configuración:
--------------
No requiere configuración. Se aplica automáticamente a todos los reportes de factura.
    """,
    'author': 'Miracca - Changsha S.R.L.',
    'website': 'https://github.com/trixocom/odoo-invoice-compact-layout',
    'license': 'LGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'views/report_invoice_compact.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'invoice_compact_layout/static/src/scss/report_invoice_compact.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/icon.png'],
}
