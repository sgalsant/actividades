---
id: verificacion-entrega
titulo: Verificación final y entrega
duracion_minutos: 15
obligatorio: true
---

## Checklist de cumplimiento

Revisa que has completado cada punto antes de entregar.

:::checkpoint{id="check-ova" required="true"}
OVA importada y renombrada correctamente.
:::

:::checkpoint{id="check-puertos" required="true"}
Reenvío de puertos configurado en VirtualBox.
:::

:::checkpoint{id="check-ssh" required="true"}
OpenSSH Server instalado y funcionando desde el anfitrión.
:::

:::checkpoint{id="check-hostname" required="true"}
Hostname personalizado y reflejado en `/etc/hosts`.
:::

:::checkpoint{id="check-tabla" required="true"}
Tabla de credenciales completada.
:::

:::checkpoint{id="check-ufw" required="true"}
Firewall UFW configurado y activo.
:::

:::checkpoint{id="check-apache" required="true"}
Apache sirviendo páginas web.
:::

:::checkpoint{id="check-mariadb" required="true"}
MariaDB instalada y asegurada.
:::

:::checkpoint{id="check-php" required="true"}
PHP funcionando con mod_php y después con PHP-FPM.
:::

:::checkpoint{id="check-paginas" required="true"}
Página HTML estática y página PHP desplegadas.
:::

:::checkpoint{id="check-phpmyadmin" required="true"}
phpMyAdmin accesible.
:::

:::checkpoint{id="check-bd" required="true"}
Base de datos creada con dos usuarios de distintos permisos.
:::

:::checkpoint{id="check-sql" required="false"}
Si generaste un script SQL aparte, comprueba que se ejecutó correctamente: la base de datos, el usuario administrador y el usuario operador se crearon sin errores y los permisos se aplicaron con `FLUSH PRIVILEGES`.
:::

:::checkpoint{id="check-php-datos" required="false"}
Si creaste un script PHP adicional que consulte la base de datos, comprueba que devuelve los registros esperados. La página `index.php` de información de PHP ya se verifica en el reto correspondiente.
:::

:::checkpoint{id="check-capturas" required="true"}
Todas las evidencias solicitadas capturadas.
:::

## Comandos de referencia rápida

:::tip{}
Conserva esta tabla para consultar los comandos más habituales del servidor LAMP.
:::

### Gestión de servicios

```bash
sudo systemctl start [servicio]    # Iniciar
sudo systemctl stop [servicio]     # Detener
sudo systemctl restart [servicio]  # Reiniciar
sudo systemctl status [servicio]   # Ver estado
sudo systemctl enable [servicio]   # Inicio automático
```

### Apache

```bash
sudo apache2ctl configtest  # Probar configuración
sudo a2enmod [modulo]       # Habilitar módulo
sudo a2dismod [modulo]      # Deshabilitar módulo
sudo a2ensite [sitio]       # Habilitar sitio
sudo a2dissite [sitio]      # Deshabilitar sitio
```

### MariaDB

```bash
sudo mysql -u root -p                    # Conectar como root
mysql -u usuario -p base_datos           # Conectar como usuario
mysqldump -u usuario -p bd > backup.sql  # Copia de seguridad
mysql -u usuario -p bd < backup.sql      # Restaurar
```

### Logs importantes

| Log | Ruta |
|---|---|
| Errores de Apache | `/var/log/apache2/error.log` |
| Accesos de Apache | `/var/log/apache2/access.log` |
| Errores de MariaDB/MySQL | `/var/log/mysql/error.log` |
| Log general del sistema | `/var/log/syslog` |

## Recursos adicionales

| Recurso | Ruta |
|---|---|
| Documento original | `RAW/1 actividad_lamp.docx` |
| Ficha de actividad | [[Actividad - Configuracion servidor LAMP Servicios en red]] |
| Patrón reusable | [[Patron - Practica LAMP Servicios en red]] |

:::task{id="snapshot" required="false"}
Opcional pero recomendado: haz un snapshot de la máquina virtual para poder retomar el estado actual en futuras actividades.
:::
