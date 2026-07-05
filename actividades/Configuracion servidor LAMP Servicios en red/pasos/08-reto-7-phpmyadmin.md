---
id: reto-7-phpmyadmin
titulo: Reto 7 - Instalación de phpMyAdmin
duracion_minutos: 20
obligatorio: true
---

phpMyAdmin es una herramienta web escrita en PHP para administrar MariaDB/MySQL mediante una interfaz gráfica.

:::task{id="instalar-phpmyadmin" required="true"}
Instala phpMyAdmin y sigue el asistente:

- Servidor web a configurar: selecciona `apache2`.
- Configurar base de datos con dbconfig-common: `Yes`.
- Contraseña de aplicación MySQL: introduce una contraseña y apúntala.
:::

```bash
sudo apt install -y phpmyadmin
```

:::task{id="habilitar-mbstring" required="true"}
Habilita la extensión `mbstring` de PHP y reinicia Apache.
:::

```bash
sudo phpenmod mbstring
sudo systemctl restart apache2
```

:::task{id="probar-phpmyadmin" required="true"}
Accede a `http://localhost:8080/phpmyadmin` e inicia sesión con usuario `root` y la contraseña de root de MariaDB.
:::

:::warning{}
**Buenas prácticas con phpMyAdmin en producción:**

- Cambia la URL por defecto (por ejemplo, `/gestordb`).
- Configura autenticación adicional con `.htaccess`.
- Restringe el acceso por IP.
- Usa siempre HTTPS.
:::

:::task{id="opcional-alias" required="false"}
Opcional: cambia el alias de phpMyAdmin editando `/etc/apache2/conf-available/phpmyadmin.conf`. Por ejemplo, sustituye `Alias /phpmyadmin /usr/share/phpmyadmin` por `Alias /[tu-nombre]db /usr/share/phpmyadmin` y reinicia Apache.
:::

:::evidence{id="captura-phpmyadmin" type="screenshot" required="true"}
Captura del panel principal de phpMyAdmin tras iniciar sesión correctamente.
:::
