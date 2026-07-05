---
id: troubleshooting-comun
titulo: Troubleshooting - Problemas comunes
duracion_minutos: 15
obligatorio: true
---

## Apache no arranca

```bash
sudo apache2ctl configtest
sudo tail -n 50 /var/log/apache2/error.log
sudo netstat -tlnp | grep :80
```

## No puedo conectar por SSH

```bash
sudo systemctl status ssh
sudo ufw status
```

Verifica también el reenvío de puertos en VirtualBox.

## Error de permisos al acceder a páginas web

```bash
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
sudo chmod 644 /var/www/html/*.html /var/www/html/*.php
```

## Las páginas PHP no funcionan

Con `mod_php`:

```bash
apache2ctl -M | grep php
```

Con PHP-FPM:

```bash
sudo systemctl status phpX.X-fpm
apache2ctl configtest
```

## phpMyAdmin muestra página en blanco

```bash
sudo tail -n 50 /var/log/apache2/error.log
php -m | grep mbstring
sudo systemctl restart apache2
```

## Error "Access denied" en MariaDB

```bash
sudo mysql -u root -p -e "SELECT user, host FROM mysql.user;"
sudo mysql -u root -p -e "SHOW GRANTS FOR 'tu_usuario'@'localhost';"
```

Recuerda ejecutar `FLUSH PRIVILEGES;` tras cambiar permisos.

## Error "Permission denied" al transferir archivos

Verifica primero que SSH funciona:

```powershell
ssh analuisa@localhost -p 2222
```

Si usas `scp`, el puerto se indica con `-P` mayúscula:

```powershell
scp -P 2222 archivo.txt analuisa@localhost:/home/analuisa/
```

Comprueba también los permisos del directorio destino en el servidor:

```bash
ls -ld /home/analuisa
```

## No aparece nada en el navegador

```bash
sudo systemctl status apache2
sudo ufw status
curl localhost
```

Verifica también el reenvío de puertos en VirtualBox.

:::question{id="primer-diagnostico" type="short-text" required="true"}
Si Apache no sirve una página, indica los dos primeros comandos que ejecutarías para diagnosticar el problema.
:::
