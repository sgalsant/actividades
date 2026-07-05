---
id: reto-8-php-fpm
titulo: Reto 8 - PHP-FPM (FastCGI Process Manager)
duracion_minutos: 25
obligatorio: true
---

PHP-FPM ejecuta PHP como un proceso separado que se comunica con Apache mediante FastCGI. Frente a `mod_php`, consume menos memoria y escala mejor.

| Caracteristica | mod_php | PHP-FPM |
|---|---|---|
| Integracion | Modulo dentro de Apache | Proceso independiente |
| Consumo de memoria | Mayor | Menor |
| Contenido estatico | Menos eficiente | Mas eficiente |
| Escalabilidad | Limitada | Mejor |
| Uso ideal | Sitios pequenos/medios | Alto trafico, multisitio |

:::task{id="instalar-php-fpm" required="true"}
Instala PHP-FPM y anota la version y el socket.
:::

```bash
sudo apt install -y php-fpm
php -v
ls /run/php/
```

Anota el socket de PHP-FPM que aparece en `/run/php/`, por ejemplo `php8.3-fpm.sock`:

![Version de PHP y socket de PHP-FPM en /run/php](recursos/media/image11.png)

:::task{id="deshabilitar-mod-php" required="true"}
Deshabilita `mod_php` y habilita los modulos necesarios para PHP-FPM. Sustituye `X.X` por tu version de PHP.
:::

```bash
sudo a2dismod phpX.X
sudo a2enmod proxy_fcgi setenvif
sudo a2enconf phpX.X-fpm
```

:::task{id="reiniciar-servicios-fpm" required="true"}
Reinicia Apache y PHP-FPM, y verifica que PHP-FPM esta corriendo.
:::

```bash
sudo systemctl restart apache2
sudo systemctl status phpX.X-fpm
```

:::task{id="verificar-fpm" required="true"}
Accede de nuevo a `http://localhost:8080/index.php`, busca la linea `Server API` y comprueba que ahora indica `FPM/FastCGI`.

![phpinfo() mostrando Server API FPM/FastCGI](recursos/media/image12.png)
:::

:::evidence{id="captura-fpm" type="screenshot" required="true"}
Captura de `phpinfo()` mostrando `Server API: FPM/FastCGI`.
:::
