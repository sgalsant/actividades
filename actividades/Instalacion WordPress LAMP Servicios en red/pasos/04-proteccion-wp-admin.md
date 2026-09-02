---
id: proteccion-wp-admin
titulo: Protección HTTP adicional de wp-admin
duracion_minutos: 60
obligatorio: true
---

## E. Protección del panel de administración

La cuenta de Apache es una barrera independiente de la cuenta administradora de WordPress. Ambas deben ser diferentes y sus contraseñas no deben aparecer en capturas ni en el informe entregado.

:::task{id="crear-usuario-apache" required="true"}
Crea un archivo de credenciales fuera del DocumentRoot y añade una persona usuaria para Apache.

```bash
sudo htpasswd -c /etc/apache2/.htpasswd-wordpress nombre_usuario_web
sudo chmod 640 /etc/apache2/.htpasswd-wordpress
sudo chown root:www-data /etc/apache2/.htpasswd-wordpress
```

Usa `htpasswd /etc/apache2/.htpasswd-wordpress otro_usuario` para añadir más cuentas sin sobrescribir el archivo.
:::

:::task{id="proteger-directorio-admin" required="true"}
Añade este bloque dentro del VirtualHost HTTPS y vuelve a validar la configuración antes de recargar Apache.

```apache
<Directory /var/www/wordpress/wp-admin>
    AuthType Basic
    AuthName "Administración de WordPress"
    AuthUserFile /etc/apache2/.htpasswd-wordpress
    Require valid-user
</Directory>
```

```bash
sudo apache2ctl configtest
sudo systemctl reload apache2
```
:::

:::warning{}
No sitúes el archivo `.htpasswd` dentro de `/var/www/wordpress`. Debe quedar fuera de los archivos que Apache puede servir directamente.
:::

:::evidence{id="captura-auth-admin" type="screenshot" required="true"}
Adjunta una captura de la ventana de autenticación HTTP al abrir `/wp-admin` antes de entrar a WordPress.
:::

:::question{id="doble-autenticacion" type="long-text" required="true"}
¿Qué protege la autenticación HTTP que no protege por sí sola el inicio de sesión de WordPress?
:::
