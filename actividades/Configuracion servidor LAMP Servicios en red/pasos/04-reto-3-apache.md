---
id: reto-3-apache
titulo: Reto 3 - Instalacion de Apache Web Server
duracion_minutos: 20
obligatorio: true
---

Apache HTTP Server recibe peticiones HTTP de los navegadores y responde con paginas web, imagenes y otros recursos.

:::task{id="instalar-apache" required="true"}
Instala Apache y verifica que el servicio esta activo y habilitado al arranque.
:::

```bash
sudo apt install -y apache2
sudo systemctl status apache2
sudo systemctl is-enabled apache2
```

:::task{id="probar-apache" required="true"}
Abre el navegador en el anfitrion y visita `http://localhost:8080`. Deberias ver la pagina por defecto de Apache.
:::

:::task{id="personalizar-index" required="true"}
Edita `/var/www/html/index.html` para que aparezca tu nombre tras el texto `It works!`.
:::

```bash
sudo nano /var/www/html/index.html
```

:::question{id="documentroot-apache" type="short-text" required="true"}
Cual es el DocumentRoot por defecto de Apache en Ubuntu?
:::

:::evidence{id="captura-apache" type="screenshot" required="true"}
Captura del navegador mostrando la pagina de Apache personalizada con tu nombre.
:::
