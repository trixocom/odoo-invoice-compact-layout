# 📦 Invoice Compact Layout - Odoo 18

[![Version](https://img.shields.io/badge/version-18.0.1.0.9-blue.svg)](https://github.com/trixocom/odoo-invoice-compact-layout)
[![License: LGPL-3](https://img.shields.io/badge/license-LGPL--3-green.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo](https://img.shields.io/badge/Odoo-18.0-purple.svg)](https://www.odoo.com)

## 🎯 ¿Qué hace este módulo?

Reduce **drásticamente** el espacio entre el encabezado de la empresa y la información del cliente en los reportes de factura de Odoo 18, optimizando el uso del papel sin perder legibilidad.

### 🔧 Versión 1.0.9 - CRITICAL FIX ✅

**🚨 ERRORES RESUELTOS:**
- ✅ `Element odoo has extra content: template, line 16`
- ✅ `Element odoo has extra content: data, line 3`

**Cambio v1.0.9:**
- 🔧 **Removido tag `<data>`** - En Odoo 18 los templates van directamente en `<odoo>`
- ✅ Estructura XML 100% compatible con Odoo 18
- ✅ El módulo se instala/actualiza sin errores

Esta versión está basada en el **análisis del código fuente REAL** de tus templates y aplica estrategias de compactación CSS ultra-agresivas.

**Templates soportados:**
- ✅ `account.report_invoice_copy_1` (template principal)
- ✅ `account.report_invoice_document_copy_1`
- ✅ `l10n_ar.report_invoice_document_copy_1` (localización argentina)
- ✅ Customizaciones de Studio
- ✅ Cualquier template que herede de los anteriores

## 🚀 Instalación Rápida

```bash
# Si ya lo tienes instalado, ACTUALIZA:
cd /ruta/addons/odoo_invoice_compact
git pull origin main

# Si es NUEVO:
cd /ruta/addons/
git clone https://github.com/trixocom/odoo-invoice-compact-layout.git odoo_invoice_compact

# Reinicia Odoo
sudo systemctl restart odoo
# O Docker:
docker-compose restart odoo
```

### En Odoo:
1. **Modo Desarrollador** → Configuración → Activar (`?debug=1`)
2. **Apps** → ⋮ → **Actualizar lista de aplicaciones**
3. Buscar **"Invoice Compact Layout"**
4. Click en **Instalar** (o **Actualizar** si ya estaba)
5. ¡Abrir una factura y ver los cambios!

## 📋 Características

### CSS Ultra-Específico
- ✅ Reset completo de header (margin/padding = 0)
- ✅ Article sin padding superior
- ✅ Eliminación total de espacios en company_address
- ✅ Rows compactas (0mm margin/padding)
- ✅ Anulación de TODOS los margins Bootstrap
- ✅ Anulación de TODOS los paddings Bootstrap
- ✅ Ocultación de divs vacíos
- ✅ Compactación de .oe_structure (Studio)
- ✅ BR tags ultra-compactos
- ✅ Line-height de 1.1 global
- ✅ Headers y párrafos sin márgenes
- ✅ Tablas optimizadas

### Ventajas
- **Compatible** con Odoo 18
- **Compatible** con localización argentina (l10n_ar)
- **No afecta** otros reportes
- **Herencia limpia** mediante XPath
- **Sobrescribe** customizaciones de Studio
- **Fácil desinstalación**
- **Estructura XML válida para Odoo 18** ✓

## 🛠️ Solución de Problemas

### ⚠️ Error XML

**✅ TODOS LOS ERRORES XML SOLUCIONADOS en v1.0.9**

Si aún ves errores XML:
```bash
cd /ruta/addons/odoo_invoice_compact
git pull origin main
```

Luego en Odoo → Apps → Invoice Compact Layout → **Actualizar**

### No veo cambios

1. **Verifica instalación:** Apps → "Invoice Compact" → debe decir "Instalado"
2. **Limpia caché:** Ctrl + F5 (Windows/Linux) o Cmd + Shift + R (Mac)
3. **Reinicia Odoo:**
   ```bash
   sudo systemctl restart odoo
   ```
4. **Verifica templates:** Configuración → Técnico → Vistas → buscar `report_invoice_copy_1_ultra_compact`

### Necesito MÁS compactación

Edita `views/report_invoice_compact.xml` y cambia:
- `padding-top: 1mm` → `padding-top: 0mm`
- `margin: 1mm` → `margin: 0mm`
- `line-height: 1.1` → `line-height: 1.0`

Luego actualiza el módulo.

## 📝 Estructura

```
odoo_invoice_compact/
├── __init__.py
├── __manifest__.py
└── views/
    └── report_invoice_compact.xml   (✅ Estructura XML v1.0.9 - Sin tag data)
```

## 📊 Changelog

### v1.0.9 (2025-10-17) - CRITICAL FIX
- 🔧 **FIXED:** Removido tag `<data>` - Odoo 18 no lo requiere
- ✅ Resuelve: "Element odoo has extra content: data, line 3"
- ✅ Templates ahora van directamente dentro de `<odoo>`

### v1.0.8 (2025-10-17)
- 🔧 Agregado tag `<data>` (causó conflicto en Odoo 18)
- ✅ Resuelve: Error de línea 16

### v1.0.7 (2025-10-17)
- 🔧 Corregido error de validación XML
- ✅ Cambio de `position="replace"` a `position="after"`

### v1.0.0 (2025-10-17)
- 🎉 Release inicial

## 🔗 Links

- [Repositorio GitHub](https://github.com/trixocom/odoo-invoice-compact-layout)
- [Reportar Bug](https://github.com/trixocom/odoo-invoice-compact-layout/issues)
- [Documentación Odoo 18](https://www.odoo.com/documentation/18.0/)

## 👨‍💻 Autor

**TrixoCom**
- GitHub: [@trixocom](https://github.com/trixocom)
- Email: hectorquiroz@trixocom.com

## 📄 Licencia

LGPL-3.0

---

⭐ **Si este módulo te fue útil, dale una estrella en GitHub!**

**Última actualización:** 2025-10-17 v1.0.9 ✅
