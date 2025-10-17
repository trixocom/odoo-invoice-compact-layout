# Invoice Compact Layout - Odoo 18 🎯

<div align="center">

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-blue)
![License](https://img.shields.io/badge/License-LGPL--3-green)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

Módulo para optimizar el espaciado en reportes de facturas de Odoo 18, reduciendo el espacio entre el encabezado de la empresa y la información del cliente.

[Instalación](#-instalación-rápida) • [Características](#-características) • [Documentación](INSTALACION.md) • [Soporte](#-soporte)

</div>

---

## 📸 Antes y Después

### ❌ ANTES (Layout Estándar)
```
[Logo Empresa]
Inicio de actividades: XX/XX/XXXX


        ← ESPACIO EXCESIVO (20-30mm) →


Cliente: Juan Pérez
RUT: XX.XXX.XXX-X
...
```

### ✅ DESPUÉS (Layout Compacto)
```
[Logo Empresa]
Inicio de actividades: XX/XX/XXXX
Cliente: Juan Pérez ← ESPACIO REDUCIDO (2-3mm)
RUT: XX.XXX.XXX-X
...
```

**Resultado:** Reduce el espacio en un 85-90%, optimizando el uso del papel.

---

## ✨ Características

- ✅ **Reducción significativa** del espacio entre encabezado y datos del cliente
- ✅ **Optimización del papel** para impresiones más eficientes
- ✅ **Mantiene la legibilidad** del documento
- ✅ **Compatible** con layouts estándar de Odoo 18
- ✅ **Fácil instalación y desinstalación**
- ✅ **Sin configuración** adicional requerida
- ✅ **Personalizable** mediante variables SCSS
- ✅ **Compatible** con Odoo Community y Enterprise

---

## 🚀 Instalación Rápida

### Método Automático (Recomendado)

```bash
curl -sSL https://raw.githubusercontent.com/trixocom/odoo-invoice-compact-layout/main/install.sh | bash
```

O descarga y ejecuta el script:

```bash
wget https://raw.githubusercontent.com/trixocom/odoo-invoice-compact-layout/main/install.sh
chmod +x install.sh
./install.sh
```

### Método Manual

```bash
# 1. Clonar el repositorio
cd /ruta/de/tus/addons/
git clone https://github.com/trixocom/odoo-invoice-compact-layout.git odoo_invoice_compact

# 2. Establecer permisos
chown -R odoo:odoo odoo_invoice_compact/
chmod -R 755 odoo_invoice_compact/

# 3. Reiniciar Odoo
sudo systemctl restart odoo
# o con Docker:
docker-compose restart odoo
```

### Pasos en Odoo

1. **Activar modo desarrollador**: Configuración → Activar el modo desarrollador
2. **Actualizar lista**: Aplicaciones → Actualizar Lista de Aplicaciones
3. **Instalar módulo**: Buscar "Invoice Compact" → Instalar
4. **Verificar**: Imprimir una factura de prueba

📖 **[Ver guía completa de instalación](INSTALACION.md)**

---

## 📁 Estructura del Proyecto

```
odoo_invoice_compact/
├── __init__.py                              # Inicialización del módulo
├── __manifest__.py                          # Configuración del módulo
├── README.md                                # Este archivo
├── INSTALACION.md                           # Guía de instalación detallada
├── install.sh                               # Script de instalación automática
├── views/
│   └── report_invoice_compact.xml          # Templates XML para reportes
└── static/
    └── src/
        └── scss/
            └── report_invoice_compact.scss  # Estilos SCSS
```

---

## 🎨 Personalización

Si deseas ajustar el espaciado, edita:
```
static/src/scss/report_invoice_compact.scss
```

### Variables Principales

```scss
$compact-padding: 1mm;      // Espaciado interno
$compact-margin: 2mm;       // Margen entre secciones
$minimal-gap: 0mm;          // Espacio mínimo
$compact-line-height: 1.2;  // Altura de línea
```

**Para aplicar cambios:**

```bash
# Regenerar assets
./odoo-bin -c /etc/odoo/odoo.conf -d tu_bd -u odoo_invoice_compact
```

O desde la interfaz web:
1. Modo desarrollador activado
2. Configuración → Técnico → Interfaz de usuario → Vistas
3. Buscar vistas de `odoo_invoice_compact`
4. Click en **Regenerar Assets**

---

## 🐳 Instalación con Docker

### Docker Compose

Agrega el volumen en tu `docker-compose.yml`:

```yaml
services:
  odoo:
    image: odoo:18.0
    volumes:
      - ./odoo_invoice_compact:/mnt/extra-addons/odoo_invoice_compact
```

### Portainer

1. Ve a tu stack de Odoo
2. Edita el stack y agrega el volumen
3. Redeploy el stack
4. Continúa con los pasos de instalación en Odoo

---

## 📊 Impacto

| Métrica | Antes | Después | Mejora |
|---------|-------|---------|--------|
| Espacio encabezado-cliente | 20-30mm | 2-3mm | **85-90%** |
| Líneas por página | ~30 | ~40 | **+33%** |
| Uso de papel | 100% | ~75% | **-25%** |

---

## 🔧 Solución de Problemas

### El módulo no aparece

```bash
# Verificar ruta
ls -la /ruta/a/addons/odoo_invoice_compact/

# Verificar permisos
ls -l /ruta/a/addons/odoo_invoice_compact/__manifest__.py

# Revisar log
tail -f /var/log/odoo/odoo-server.log
```

### Los estilos no se aplican

```bash
# Regenerar assets
./odoo-bin -c /etc/odoo/odoo.conf -d nombre_bd -u odoo_invoice_compact

# Limpiar caché del navegador
Ctrl + Shift + R (o Cmd + Shift + R en Mac)
```

### Error al instalar

- Verificar que el módulo `account` esté instalado
- Verificar versión de Odoo: debe ser 18.0
- Revisar logs para más detalles

---

## 🆘 Soporte

- 📖 **Documentación**: [INSTALACION.md](INSTALACION.md)
- 🐛 **Issues**: [GitHub Issues](https://github.com/trixocom/odoo-invoice-compact-layout/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/trixocom/odoo-invoice-compact-layout/discussions)

---

## 📋 Requisitos

- Odoo 18.0 (Community o Enterprise)
- Módulo `account` instalado
- Acceso de administrador

---

## 📝 Compatibilidad

| Versión | Estado |
|---------|--------|
| Odoo 18.0 | ✅ Compatible |
| Odoo 17.0 | ⚠️ No probado |
| Odoo 16.0 | ❌ No compatible |

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la licencia LGPL-3. Ver el archivo `LICENSE` para más detalles.

---

## 👨‍💻 Autor

**TrixoCom**
- GitHub: [@trixocom](https://github.com/trixocom)
- Website: [https://trixocom.com](https://trixocom.com)

---

## ⭐ ¿Te fue útil?

Si este módulo te ayudó, considera:
- Darle una ⭐ al repositorio
- Compartirlo con otros usuarios de Odoo
- Reportar bugs o sugerir mejoras

---

<div align="center">

**Hecho con ❤️ para la comunidad Odoo**

</div>
