---
id: virtualhost-https-wordpress
titulo: VirtualHost, HTTPS y logs independientes
duracion_minutos: 90
obligatorio: true
---

## C y D. Configuración del VirtualHost y SSL/HTTPS

Necesitas dos VirtualHost: uno para redirigir HTTP y otro para servir WordPress mediante TLS. Usa los certificados autofirmados creados en la práctica anterior o un certificado equivalente disponible en tu servidor.

:::task{id="crear-virtualhost-wordpress" required="true"}
Crea `/etc/apache2/sites-available/wordpress.conf`. Sustituye las rutas del certificado por las que existan realmente en tu servidor.

```apache
<VirtualHost *:80>
    ServerName wordpress.127.0.0.1.nip.io
    Redirect permanent / https://wordpress.127.0.0.1.nip.io/
</VirtualHost>

<VirtualHost *:443>
    ServerName wordpress.127.0.0.1.nip.io
    DocumentRoot /var/www/wordpress

    SSLEngine on
    SSLCertificateFile /ruta/al/certificado.crt
    SSLCertificateKeyFile /ruta/a/la-clave.key

    ErrorLog ${APACHE_LOG_DIR}/wordpress_error.log
    CustomLog ${APACHE_LOG_DIR}/wordpress_access.log combined

    <Directory /var/www/wordpress>
        Options FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

Si tu VM publica `443` como `8443` en el equipo anfitrión, accede por `https://wordpress.127.0.0.1.nip.io:8443/` y ajusta la redirección para que conserve el puerto publicado. Explica esa decisión en tu documentación.
:::

:::task{id="habilitar-sitio-https" required="true"}
Habilita los módulos y el sitio, valida la sintaxis y recarga Apache solo si la comprobación es correcta.

```bash
sudo a2enmod ssl rewrite
sudo a2ensite wordpress.conf
sudo apache2ctl configtest
sudo systemctl reload apache2
```
:::

:::task{id="verificar-https-redireccion" required="true"}
Comprueba que HTTP redirige a HTTPS y que se generan los dos logs propios.

```bash
curl -I http://wordpress.127.0.0.1.nip.io/
sudo ls -l /var/log/apache2/wordpress_access.log /var/log/apache2/wordpress_error.log
```
:::

:::evidence{id="captura-virtualhost" type="screenshot" required="true"}
Adjunta una captura del contenido completo de `wordpress.conf`.
:::

:::evidence{id="captura-https" type="screenshot" required="true"}
Adjunta una captura del navegador mostrando WordPress con HTTPS. Si el certificado es autofirmado, documenta la advertencia aceptada en el laboratorio.
:::
