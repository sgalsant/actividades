---
id: reto-5-php-modulo
titulo: Reto 5 - Instalacion de PHP como modulo de Apache
duracion_minutos: 25
obligatorio: true
---

PHP permite crear paginas dinamicas que interactuan con bases de datos. En este paso lo instalamos como modulo de Apache (`mod_php`).

:::task{id="instalar-php" required="true"}
Instala PHP y los modulos necesarios.
:::

```bash
sudo apt install -y php libapache2-mod-php php-mysql
```

:::task{id="verificar-php" required="true"}
Comprueba la version de PHP y que el modulo esta cargado.
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

Ejemplo de linea a dejar:

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
Accede a `http://localhost:8080` y comprueba que se muestra tu nombre y la informacion de PHP.
:::

:::warning{}
En produccion, nunca dejes accesible `phpinfo()` publicamente porque revela informacion sensible del servidor.
:::

:::evidence{id="captura-php" type="screenshot" required="true"}
Captura del navegador mostrando la pagina `index.php` con tu nombre y la informacion de PHP.
:::
