---
id: instalacion-web-wordpress
titulo: Instalación web y configuración inicial
duracion_minutos: 75
obligatorio: true
---

## F. Configuración de WordPress

Abre la URL HTTPS del sitio. Completa el instalador usando la base de datos y el usuario creados en el paso anterior. WordPress generará `wp-config.php`; revisa que sus valores de `DB_NAME`, `DB_USER`, `DB_PASSWORD` y `DB_HOST` coinciden con tu configuración.

:::task{id="configurar-wordpress-web" required="true"}
Completa el asistente con un título de sitio, una cuenta administradora de WordPress, una contraseña robusta y una dirección de correo válida.

No uses como nombre de cuenta `admin`, no reutilices las credenciales de MariaDB ni las de la autenticación HTTP, y no documentes contraseñas reales en la tabla de credenciales.
:::

:::task{id="revisar-wp-config" required="true"}
Comprueba que el archivo de configuración no tiene permisos excesivos y que Apache conserva la propiedad necesaria.

```bash
sudo chown www-data:www-data /var/www/wordpress/wp-config.php
sudo chmod 640 /var/www/wordpress/wp-config.php
sudo ls -l /var/www/wordpress/wp-config.php
```
:::

:::evidence{id="captura-panel-wordpress" type="screenshot" required="true"}
Adjunta una captura del escritorio de `/wp-admin` tras superar la autenticación HTTP y el acceso de WordPress.
:::

:::file{id="adjunto-wordpress-conf" accept=".conf,.txt" required="true"}
Adjunta una copia saneada de `wordpress.conf`. Elimina o sustituye cualquier dato secreto antes de adjuntarla.
:::
