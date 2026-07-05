---
id: reto-7-phpmyadmin
titulo: Reto 7 - Instalacion de phpMyAdmin
duracion_minutos: 20
obligatorio: true
---

phpMyAdmin es una herramienta web escrita en PHP para administrar MariaDB/MySQL mediante una interfaz grafica.

:::task{id="instalar-phpmyadmin" required="true"}
Instala phpMyAdmin y sigue el asistente:

- Servidor web a configurar: selecciona `apache2`.
- Configurar base de datos con dbconfig-common: `Yes`.
- Contrasena de aplicacion MySQL: introduce una contrasena y anotala.
:::

```bash
sudo apt install -y phpmyadmin
```

:::task{id="habilitar-mbstring" required="true"}
Habilita la extension `mbstring` de PHP y reinicia Apache.
:::

```bash
sudo phpenmod mbstring
sudo systemctl restart apache2
```

:::task{id="probar-phpmyadmin" required="true"}
Accede a `http://localhost:8080/phpmyadmin` e inicia sesion con usuario `root` y la contrasena de root de MariaDB.
:::

:::task{id="opcional-alias" required="false"}
Opcional: cambia el alias de phpMyAdmin editando `/etc/apache2/conf-available/phpmyadmin.conf` y reinicia Apache.
:::

:::warning{}
En produccion, cambia la URL por defecto, restringe el acceso por IP y usa HTTPS.
:::

:::evidence{id="captura-phpmyadmin" type="screenshot" required="true"}
Captura del panel principal de phpMyAdmin tras iniciar sesion correctamente.
:::
