# 📦 Invoice Compact Layout - Odoo 18

[![Version](https://img.shields.io/badge/version-18.0.1.0.6-blue.svg)](https://github.com/trixocom/odoo-invoice-compact-layout)
[![License: LGPL-3](https://img.shields.io/badge/license-LGPL--3-green.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo](https://img.shields.io/badge/Odoo-18.0-purple.svg)](https://www.odoo.com)

## 🎯 ¿Qué hace este módulo?

Reduce **drásticamente** el espacio entre el encabezado de la empresa y la información del cliente en los reportes de factura de Odoo 18, optimizando el uso del papel sin perder legibilidad.

### ✨ Versión 1.0.6 - DEFINITIVA

Esta versión está basada en el **análisis del código fuente REAL** de tus templates y aplica 20 estrategias diferentes de compactación CSS.

**Templates soportados:**
- ✅ `account.report_invoice_copy_1` (template principal)
- ✅ `account.report_invoice_document_copy_1`
- ✅ `l10n_ar.report_invoice_document_copy_1` (localización argentina)
- ✅ Customizaciones de Studio
- ✅ Cualquier template que herede de los anteriores

## 📸 Antes y Después

**Antes:** Espacio excesivo entre "Inicio de actividades" y datos del cliente
**Después:** Espacio mínimo, todo compacto y legible

## 🚀 Instalación

### Opción 1: Git Clone (Recomendado)

```bash
# Navega al directorio de addons de tu Odoo
cd /ruta/a/odoo/addons

# Clona el repositorio
git clone https://github.com/trixocom/odoo-invoice-compact-layout.git odoo_invoice_compact

# Reinicia Odoo
sudo systemctl restart odoo
# O si usas Docker:
docker-compose restart odoo
```

### Opción 2: Descargar ZIP

1. [Descarga el ZIP](https://github.com/trixocom/odoo-invoice-compact-layout/archive/refs/heads/main.zip)
2. Extrae en tu directorio de addons con el nombre `odoo_invoice_compact`
3. Reinicia Odoo

### Opción 3: Docker/Portainer

```bash
# Accede al contenedor
docker exec -it <container_name> bash

# Navega a addons
cd /mnt/extra-addons

# Clona el módulo
git clone https://github.com/trixocom/odoo-invoice-compact-layout.git odoo_invoice_compact

# Sal y reinicia
exit
docker restart <container_name>
```

## ⚙️ Activación en Odoo

1. Activa el **Modo Desarrollador**:
   - Ve a Configuración → Activar modo desarrollador
   - O agrega `?debug=1` a la URL

2. Actualiza la lista de aplicaciones:
   - Apps → ⋮ (menú) → Actualizar lista de aplicaciones

3. Busca e instala:
   - Busca: "Invoice Compact Layout"
   - Click en **Instalar**

4. ¡Listo! Abre cualquier factura y verás los cambios

## 🔄 Actualizar a v1.0.6

Si ya tienes una versión anterior instalada:

```bash
# Actualiza el repositorio
cd /ruta/a/odoo/addons/odoo_invoice_compact
git pull origin main

# Reinicia Odoo
sudo systemctl restart odoo
```

Luego en Odoo:
1. Apps → Buscar "Invoice Compact Layout"
2. Click en **Actualizar**

## 📋 Características v1.0.6

### 🎨 20 Estrategias de Compactación

1. ✅ Reset completo del header (margin/padding 0)
2. ✅ Padding mínimo en article (1mm)
3. ✅ Compactación de página
4. ✅ Eliminación de espacio después de company info
5. ✅ Compactación de todas las rows
6. ✅ Anulación de margins de Bootstrap (mt-*, mb-*, my-*)
7. ✅ Anulación de paddings de Bootstrap (pt-*, pb-*, py-*)
8. ✅ Compactación de elementos #informations
9. ✅ Ocultación de divs vacíos
10. ✅ Compactación de .oe_structure (Studio)
11. ✅ Optimización de br tags
12. ✅ Line-height global de 1.2
13. ✅ Compactación de headers (h1-h6)
14. ✅ Optimización de párrafos
15. ✅ Tablas compactas
16. ✅ Compactación de elementos de dirección
17. ✅ Optimización de external_layout
18. ✅ Compactación de containers
19. ✅ Reducción de espacios en payment_term
20. ✅ Reducción de espacios en right-elements

### 🔥 Ventajas

- **Compatibilidad total** con Odoo 18
- **Compatible** con localización argentina (l10n_ar)
- **No afecta** otros reportes
- **Herencia limpia** mediante XPath
- **CSS ultra-específico** con máxima prioridad
- **Sobrescribe** customizaciones de Studio
- **Fácil desinstalación** (todo vuelve a la normalidad)

## 🛠️ Solución de Problemas

### El módulo instaló pero no veo cambios

1. **Verifica que esté instalado:**
   ```
   Apps → Buscar "Invoice Compact" → Debe decir "Instalado"
   ```

2. **Limpia la caché del navegador:**
   ```
   Ctrl + F5 (Windows/Linux)
   Cmd + Shift + R (Mac)
   ```

3. **Reinicia Odoo:**
   ```bash
   sudo systemctl restart odoo
   ```

4. **Verifica los templates:**
   - Modo desarrollador → Configuración → Técnico → Vistas
   - Busca: `report_invoice_copy_1_ultra_compact`
   - Debe existir y estar activo

### Error al instalar

Si ves un error como "Cannot locate node", verifica:

1. Que uses Odoo 18 (no funciona en v17 o anteriores)
2. Que el módulo `account` esté instalado
3. Que no haya otros módulos conflictivos

### Los cambios se ven pero no son suficientes

Si necesitas aún MÁS compactación, puedes:

1. Editar el archivo `views/report_invoice_compact.xml`
2. Cambiar los valores de `1mm` a `0mm` o `0.5mm`
3. Actualizar el módulo

## 📝 Estructura del Módulo

```
odoo_invoice_compact/
├── __init__.py
├── __manifest__.py
└── views/
    └── report_invoice_compact.xml
```

## 🤝 Contribuciones

¿Tienes ideas para mejorar el módulo? ¡Abre un issue o envía un pull request!

## 📄 Licencia

LGPL-3.0 - Ver [LICENSE](LICENSE) para más detalles

## 👨‍💻 Autor

**TrixoCom**
- GitHub: [@trixocom](https://github.com/trixocom)
- Email: hectorquiroz@trixocom.com

## 🔗 Links

- [Repositorio GitHub](https://github.com/trixocom/odoo-invoice-compact-layout)
- [Reportar un Bug](https://github.com/trixocom/odoo-invoice-compact-layout/issues)
- [Documentación Odoo 18](https://www.odoo.com/documentation/18.0/)

---

⭐ **Si este módulo te fue útil, dale una estrella en GitHub!**
