---
id: reto-6-paginas-web
titulo: Reto 6 - Creacion y transferencia de paginas web
duracion_minutos: 25
obligatorio: true
---

Aprenderas a crear una pagina HTML en el anfitrion y transferirla al servidor mediante SFTP, que funciona sobre SSH.

:::task{id="crear-html-anfitrion" required="true"}
En tu equipo anfitrion crea una carpeta `web_lamp` y un archivo `index.html` con este contenido:
:::

```html
<!DOCTYPE html>
<html lang="es">
<body>
   <h1>¡Bienvenido a mi Servidor LAMP!</h1>
   <h2>Alumno/a: [TU NOMBRE COMPLETO]</h2>
</body>
</html>
```

:::task{id="transferir-sftp" required="true"}
Desde PowerShell, conectate por SFTP y sube el archivo.
:::

```powershell
cd Desktop\web_lamp
sftp -P 2222 analuisa@localhost:
put index.html
```

:::task{id="mover-html" required="true"}
En el servidor, mueve el archivo al DocumentRoot y ajusta los permisos.
:::

```bash
ls -lh /home/analuisa/index.html
sudo mv /home/analuisa/index.html /var/www/html/
sudo chown www-data:www-data /var/www/html/index.html
sudo chmod 644 /var/www/html/index.html
```

:::task{id="probar-html" required="true"}
Abre `http://localhost:8080/index.html` y comprueba que se muestra tu pagina personalizada.
:::

:::question{id="usuario-apache" type="short-text" required="true"}
Bajo que usuario de sistema se ejecuta Apache en Ubuntu?
:::

:::evidence{id="captura-html" type="screenshot" required="true"}
Captura del navegador mostrando tu pagina HTML personalizada.
:::
