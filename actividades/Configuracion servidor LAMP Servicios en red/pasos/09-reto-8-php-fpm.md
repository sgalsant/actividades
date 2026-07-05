---
id: reto-8-php-fpm
titulo: Reto 8 - PHP-FPM (FastCGI Process Manager)
duracion_minutos: 25
obligatorio: true
---

PHP-FPM ejecuta PHP como un proceso separado que se comunica con Apache mediante FastCGI. Frente a `mod_php`, consume menos memoria y escala mejor.

| Característica | mod_php | PHP-FPM |
|---|---|---|
| Integración | Módulo dentro de Apache | Proceso independiente |
| Consumo de memoria | Mayor (PHP en cada proceso Apache) | Menor (procesos separados) |
| Rendimiento con contenido estático | Menos eficiente | Más eficiente |
| Configuración | Más simple | Más compleja |
| Escalabilidad | Limitada | Mejor escalabilidad |
| Permisos | Todos los procesos con los mismos permisos | Puede usar diferentes usuarios por pool |
| Uso ideal | Sitios pequeños/medios | Alto tráfico, multisitio |

:::note{}
**¿Cuándo usar cada uno?**

- **`mod_php`:** proyectos pequeños o de desarrollo, cuando la simplicidad es prioritaria, bajo volumen de visitas o un solo sitio web en el servidor.
- **`PHP-FPM`:** servidores con múltiples sitios web, alto tráfico, necesidad de optimizar recursos, requisitos de seguridad avanzada (aislamiento entre sitios) o uso con otros servidores web como Nginx.
:::

:::tip{}
**Arquitectura PHP-FPM:**

`Cliente → Apache → PHP-FPM (proceso separado) → MariaDB`

Apache delega las peticiones PHP a PHP-FPM mediante FastCGI. Esto permite:

- Apache gestiona el contenido estático de forma eficiente.
- PHP-FPM procesa solo las peticiones PHP.
- Mejor aislamiento y seguridad.
- Posibilidad de reiniciar PHP sin afectar a Apache.
:::

:::task{id="instalar-php-fpm" required="true"}
Instala PHP-FPM y anota la versión y el socket.
:::

```bash
sudo apt install -y php-fpm
php -v
ls /run/php/
```

Anota el socket de PHP-FPM que aparece en `/run/php/`, por ejemplo `php8.3-fpm.sock`:

![Versión de PHP y socket de PHP-FPM en /run/php](recursos/media/image11.png)

:::task{id="deshabilitar-mod-php" required="true"}
Deshabilita `mod_php` y habilita los módulos necesarios para PHP-FPM. Sustituye `X.X` por tu versión de PHP.
:::

```bash
sudo a2dismod phpX.X
sudo a2enmod proxy_fcgi setenvif
sudo a2enconf phpX.X-fpm
```

:::task{id="reiniciar-servicios-fpm" required="true"}
Reinicia Apache y PHP-FPM, y verifica que PHP-FPM está corriendo.
:::

```bash
sudo systemctl restart apache2
sudo systemctl status phpX.X-fpm
```

:::task{id="verificar-fpm" required="true"}
Accede de nuevo a `http://localhost:8080/index.php`, busca la línea `Server API` y comprueba que ahora indica `FPM/FastCGI`.

![phpinfo() mostrando Server API FPM/FastCGI](recursos/media/image12.png)
:::

:::evidence{id="captura-fpm" type="screenshot" required="true"}
Captura de `phpinfo()` mostrando `Server API: FPM/FastCGI`.
:::
