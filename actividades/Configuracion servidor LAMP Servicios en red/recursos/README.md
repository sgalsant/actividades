---
id: recursos-configuracion-servidor-lamp-servicios-en-red
tipo: index
dominio: programaciones-didacticas
estado: activo
prioridad_consulta: media
vigencia: no_aplica
fuente_rol: patron
vigencia_estado: no_aplica
related:
  - "[[Configuracion servidor LAMP Servicios en red/README]]"
tags:
  - recursos
  - actividad
---

# Recursos

- Documento original: `RAW/1 actividad_lamp.docx`
- Imagenes extraidas del documento original en `media/`, ordenadas por aparicion en el documento fuente y ubicacion en los pasos:
  - `image1.jpg`: portada y diagrama conceptual del stack LAMP (`pasos/00-presentacion.md`).
  - `image2.png`: configuracion de red NAT y boton **Reenvio de puertos** en VirtualBox (`pasos/01-reto-0-preparacion-entorno.md`).
  - `image3.png`: reglas de reenvio de puertos SSH, HTTP y HTTPS configuradas en VirtualBox (`pasos/01-reto-0-preparacion-entorno.md`).
  - `image4.png`: salida de `sudo systemctl status ssh` mostrando el servicio activo y habilitado (`pasos/01-reto-0-preparacion-entorno.md`).
  - `image5.png`: conexion SSH exitosa desde PowerShell al servidor Ubuntu (`pasos/01-reto-0-preparacion-entorno.md`).
  - `image6.png`: sello de licencia Creative Commons BY-NC-SA 4.0 (PNG); no se referencia directamente en los pasos porque se usa la version SVG (`image7.svg`).
  - `image7.svg`: sello de licencia Creative Commons BY-NC-SA 4.0 en formato SVG (`pasos/00-presentacion.md`).
  - `image8.png`: edicion de `/etc/hosts` con el nuevo hostname en nano (`pasos/02-reto-1-personalizacion-servidor.md`).
  - `image9.png`: pagina por defecto de Apache2 Ubuntu Default Page (`pasos/04-reto-3-apache.md`).
  - `image10.png`: pagina de Apache personalizada con el nombre del alumno tras `It works!` (`pasos/04-reto-3-apache.md`).
  - `image11.png`: version de PHP y listado del socket de PHP-FPM en `/run/php/` (`pasos/09-reto-8-php-fpm.md`).
  - `image12.png`: salida de `phpinfo()` mostrando `Server API: FPM/FastCGI` (`pasos/09-reto-8-php-fpm.md`).
  - `image13.jpg`: ilustracion de cierre del aula completando la instalacion LAMP (`pasos/13-reflexion.md`).
- Maquina virtual base: `ubuntu server-24.ova` (proporcionada durante el curso).
