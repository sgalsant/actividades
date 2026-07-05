---
id: verificacion-entrega
titulo: Verificacion final y entrega
duracion_minutos: 15
obligatorio: true
---

## Checklist de cumplimiento

Revisa que has completado cada punto antes de entregar.

:::checkpoint{id="check-ova" required="true"}
OVA importada y renombrada correctamente.
:::

:::checkpoint{id="check-puertos" required="true"}
Reenvio de puertos configurado en VirtualBox.
:::

:::checkpoint{id="check-ssh" required="true"}
OpenSSH Server instalado y funcionando desde el anfitrion.
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
Apache sirviendo paginas web.
:::

:::checkpoint{id="check-mariadb" required="true"}
MariaDB instalada y asegurada.
:::

:::checkpoint{id="check-php" required="true"}
PHP funcionando con mod_php y despues con PHP-FPM.
:::

:::checkpoint{id="check-paginas" required="true"}
Pagina HTML estatica y pagina PHP desplegadas.
:::

:::checkpoint{id="check-phpmyadmin" required="true"}
phpMyAdmin accesible.
:::

:::checkpoint{id="check-bd" required="true"}
Base de datos creada con dos usuarios de distintos permisos.
:::

:::checkpoint{id="check-sql" required="true"}
Script SQL ejecutado correctamente: la base de datos, el usuario administrador y el usuario operador se han creado sin errores y los permisos se han aplicado con `FLUSH PRIVILEGES`.
:::

:::checkpoint{id="check-php-datos" required="true"}
Script PHP mostrando datos correctamente: la pagina `index.php` carga en el navegador y muestra la informacion de PHP; si has creado un script adicional que consulte la base de datos, comprueba que devuelve los registros esperados.
:::

:::checkpoint{id="check-capturas" required="true"}
Todas las evidencias solicitadas capturadas.
:::

## Recursos adicionales

| Recurso | Ruta |
|---|---|
| Documento original | `RAW/1 actividad_lamp.docx` |
| Ficha de actividad | [[Actividad - Configuracion servidor LAMP Servicios en red]] |
| Patron reusable | [[Patron - Practica LAMP Servicios en red]] |

:::task{id="snapshot" required="false"}
Opcional pero recomendado: haz un snapshot de la maquina virtual para poder retomar el estado actual en futuras actividades.
:::
