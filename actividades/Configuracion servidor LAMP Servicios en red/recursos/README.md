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
- Imágenes extraídas del documento original en `media/`, ordenadas por aparición en el documento fuente y ubicación en los pasos. Los pasos las referencian como `../recursos/media/<archivo>` desde su ubicación en `pasos/`:
  - `image1.jpg`: portada y diagrama conceptual del stack LAMP (`pasos/00-presentacion.md`).
  - `image2.png`: configuración de red NAT y botón **Reenvío de puertos** en VirtualBox (`pasos/01-reto-0-preparacion-entorno.md`).
  - `image3.png`: reglas de reenvío de puertos SSH, HTTP y HTTPS configuradas en VirtualBox (`pasos/01-reto-0-preparacion-entorno.md`).
  - `image4.png`: salida de `sudo systemctl status ssh` mostrando el servicio activo y habilitado (`pasos/01-reto-0-preparacion-entorno.md`).
  - `image5.png`: conexión SSH exitosa desde PowerShell al servidor Ubuntu (`pasos/01-reto-0-preparacion-entorno.md`).
  - `image6.png`: sello de licencia Creative Commons BY-NC-SA 4.0 (PNG); no se referencia directamente en los pasos porque se usa la versión SVG (`image7.svg`).
  - `image7.svg`: sello de licencia Creative Commons BY-NC-SA 4.0 en formato SVG (`pasos/00-presentacion.md`).
  - `image8.png`: edición de `/etc/hosts` con el nuevo hostname en nano (`pasos/02-reto-1-personalizacion-servidor.md`).
  - `image9.png`: página por defecto de Apache2 Ubuntu Default Page (`pasos/04-reto-3-apache.md`).
  - `image10.png`: página de Apache personalizada con el nombre del alumno tras `It works!` (`pasos/04-reto-3-apache.md`).
  - `image11.png`: versión de PHP y listado del socket de PHP-FPM en `/run/php/` (`pasos/09-reto-8-php-fpm.md`).
  - `image12.png`: salida de `phpinfo()` mostrando `Server API: FPM/FastCGI` (`pasos/09-reto-8-php-fpm.md`).
  - `image13.jpg`: ilustración de cierre del aula completando la instalación LAMP (`pasos/13-reflexion.md`).
- Máquina virtual base: `ubuntu server-24.ova` (proporcionada durante el curso).
