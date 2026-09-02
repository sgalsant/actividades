---
id: preparacion-entorno-wordpress
titulo: Preparación del entorno y descarga
duracion_minutos: 60
obligatorio: true
---

## A. Preparación del entorno

Comprueba los requisitos de PHP, MariaDB/MySQL y Apache de la versión de WordPress que vayas a instalar. Registra la versión descargada: usar `latest.tar.gz` no elimina la obligación de documentar qué versión concreta has desplegado.

:::task{id="descargar-wordpress" required="true"}
Crea el directorio de destino, descarga WordPress desde su origen oficial, extrae el archivo y deja sus archivos directamente en `/var/www/wordpress`.

```bash
cd /tmp
wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz
sudo mkdir -p /var/www/wordpress
sudo cp -a wordpress/. /var/www/wordpress/
grep '\$wp_version' /var/www/wordpress/wp-includes/version.php
```

No copies el directorio contenedor `wordpress` dentro de `/var/www/wordpress`: el `index.php` debe quedar en el DocumentRoot.
:::

:::task{id="ajustar-permisos-wordpress" required="true"}
Asigna la propiedad a Apache y aplica permisos base seguros. Revisa después que los directorios sean ejecutables y los archivos no sean escribibles para otros usuarios.

```bash
sudo chown -R www-data:www-data /var/www/wordpress
sudo find /var/www/wordpress -type d -exec chmod 755 {} \;
sudo find /var/www/wordpress -type f -exec chmod 644 {} \;
sudo ls -ld /var/www/wordpress
```
:::

:::warning{}
No uses permisos `777`. Si WordPress pide FTP durante una actualización, revisa la propiedad y los permisos antes de ampliar privilegios.
:::

:::evidence{id="captura-descarga-extraccion" type="screenshot" required="true"}
Adjunta una captura de la terminal donde se vean la descarga, extracción y versión de WordPress.
:::

:::question{id="version-wordpress" type="short-text" required="true"}
¿Qué versión de WordPress has instalado?
:::
