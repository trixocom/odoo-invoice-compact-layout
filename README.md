# Invoice Compact Layout - Odoo 18

Módulo para optimizar el espaciado en reportes de facturas de Odoo 18, reduciendo el espacio entre el encabezado de la empresa y la información del cliente.

## Características

- ✅ Reduce significativamente el espacio entre encabezado y datos del cliente
- ✅ Optimiza el uso del papel en impresiones
- ✅ Mantiene la legibilidad del documento
- ✅ Compatible con layouts estándar de Odoo 18
- ✅ Fácil instalación y desinstalación

## Instalación

### Método 1: Instalación Manual

1. Copia la carpeta `odoo_invoice_compact` a tu directorio de addons de Odoo:
   ```bash
   cp -r odoo_invoice_compact /ruta/a/odoo/addons/
   ```

2. Reinicia el servicio de Odoo:
   ```bash
   sudo systemctl restart odoo
   # o si usas Docker:
   docker-compose restart odoo
   ```

3. Actualiza la lista de aplicaciones:
   - Ve a Aplicaciones
   - Click en "Actualizar lista de aplicaciones"
   - Busca "Invoice Compact Layout"
   - Click en "Instalar"

### Método 2: Con Docker/Portainer

Si usas Docker Compose:

```yaml
services:
  odoo:
    volumes:
      - ./odoo_invoice_compact:/mnt/extra-addons/odoo_invoice_compact
```

Luego reinicia el contenedor y actualiza la lista de módulos.

### Método 3: Desde GitHub

```bash
cd /ruta/a/odoo/addons/
git clone https://github.com/trixocom/odoo-invoice-compact-layout.git odoo_invoice_compact
sudo systemctl restart odoo
```

## Configuración

No requiere configuración adicional. Una vez instalado, el módulo aplicará automáticamente los estilos compactos a todos los reportes de factura.

## Personalización

Si deseas ajustar el espaciado, edita el archivo:
```
static/src/scss/report_invoice_compact.scss
```

Variables principales:
- `$compact-padding`: Espaciado interno (default: 1mm)
- `$compact-margin`: Margen entre secciones (default: 2mm)
- `$minimal-gap`: Espacio mínimo (default: 0mm)

Después de modificar, regenera los assets:
```bash
./odoo-bin -c /etc/odoo/odoo.conf -d tu_base_de_datos -u odoo_invoice_compact
```

## Desinstalación

1. Ve a Aplicaciones
2. Busca "Invoice Compact Layout"
3. Click en "Desinstalar"

## Compatibilidad

- ✅ Odoo 18.0
- ✅ Odoo Community y Enterprise
- ✅ Compatible con módulo account

## Soporte

Si encuentras algún problema, abre un issue en:
https://github.com/trixocom/odoo-invoice-compact-layout/issues

## Licencia

LGPL-3

## Autor

Desarrollado para optimizar reportes de facturación en Odoo 18.
