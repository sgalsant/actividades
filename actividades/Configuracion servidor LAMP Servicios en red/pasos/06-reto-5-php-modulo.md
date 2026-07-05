---
id: reto-5-php-modulo
titulo: Reto 5 - Instalación de PHP como módulo de Apache
duracion_minutos: 25
obligatorio: true
---

PHP permite crear páginas dinámicas que interactúan con bases de datos. En este paso lo instalamos como módulo de Apache (`mod_php`).

:::task{id="instalar-php" required="true"}
Instala PHP y los módulos necesarios.
:::

```bash
sudo apt install -y php libapache2-mod-php php-mysql
```

:::task{id="verificar-php" required="true"}
Comprueba la versión de PHP y que el módulo está cargado.
:::

```bash
php -v
apache2ctl -M | grep php
```

:::task{id="priorizar-index-php" required="true"}
Edita `/etc/apache2/mods-enabled/dir.conf` para que `index.php` aparezca primero en `DirectoryIndex`.
:::

```bash
sudo nano /etc/apache2/mods-enabled/dir.conf
```

Ejemplo de línea a dejar:

```
DirectoryIndex index.php index.html index.cgi index.pl index.xhtml index.htm
```

:::task{id="reiniciar-apache-php" required="true"}
Reinicia Apache y crea `/var/www/html/index.php`.
:::

```bash
sudo systemctl restart apache2
sudo nano /var/www/html/index.php
```

Contenido de ejemplo:

```php
<?php
echo "[tu_nombre]\n";
phpinfo();
```

:::task{id="probar-index-php" required="true"}
Accede a `http://localhost:8080` y comprueba que se muestra tu nombre y la información de PHP.
:::

:::warning{}
En producción, nunca dejes accesible `phpinfo()` públicamente porque revela información sensible del servidor.
:::

:::evidence{id="captura-php" type="screenshot" required="true"}
Captura del navegador mostrando la página `index.php` con tu nombre y la información de PHP.
:::
