---
id: reto-6-paginas-web
titulo: Reto 6 - Creación y transferencia de páginas web
duracion_minutos: 25
obligatorio: true
---

Aprenderás a crear una página HTML en el anfitrión y transferirla al servidor mediante **SFTP** (SSH File Transfer Protocol), que funciona sobre SSH.

:::note{}
SFTP es un protocolo de red que permite transferir archivos de forma segura entre dos ordenadores a través de una red, incluso si esta es insegura. En nuestro caso, al no disponer de `scp` en los equipos Windows de clase, usamos `sftp`.
:::

:::tip{}
**Flujo de trabajo:**

1. Crear el archivo en el anfitrión (Notepad, VS Code, etc.).
2. Guardarlo en una carpeta conocida.
3. Copiarlo al servidor con SFTP.
4. Moverlo al DocumentRoot de Apache.
5. Ajustar los permisos.
6. Probarlo en el navegador.
:::

:::task{id="crear-html-anfitrion" required="true"}
En tu equipo anfitrión crea una carpeta `web_lamp` y un archivo `index.html` con este contenido:
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
Desde PowerShell, conéctate por SFTP y sube el archivo.
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

:::note{}
- `www-data`: usuario bajo el que se ejecuta Apache en Ubuntu.
- `644`: lectura y escritura para el propietario, y solo lectura para el resto.
:::

:::task{id="probar-html" required="true"}
Abre `http://localhost:8080/index.html` y comprueba que se muestra tu página personalizada.
:::

:::question{id="usuario-apache" type="short-text" required="true"}
¿Bajo qué usuario de sistema se ejecuta Apache en Ubuntu?
:::

:::evidence{id="captura-html" type="screenshot" required="true"}
Captura del navegador mostrando tu página HTML personalizada.
:::
