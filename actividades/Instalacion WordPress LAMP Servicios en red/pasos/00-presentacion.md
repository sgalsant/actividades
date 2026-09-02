---
id: presentacion-wordpress
titulo: Presentación, escenario y requisitos
duracion_minutos: 30
obligatorio: true
---

El Instituto Tecnológico Central necesita publicar su portal institucional con WordPress. Trabajarás como administrador o administradora junior y realizarás una instalación manual, sin instaladores automáticos.

:::note{}
El objetivo no es solo que WordPress funcione: debes demostrar que puedes desplegar una aplicación web sobre LAMP con HTTPS, aislamiento de base de datos, permisos correctos, registros propios y una protección adicional del panel administrativo.
:::

## Resultado esperado

- Dominio: `wordpress.127.0.0.1.nip.io`.
- Directorio web: `/var/www/wordpress`.
- HTTPS obligatorio en el puerto publicado por tu práctica (`443` o `8443`).
- HTTP redirigido automáticamente a HTTPS.
- Base de datos y usuario exclusivos para WordPress; nunca el usuario `root`.
- `/wp-admin` protegido mediante autenticación HTTP y con el acceso de WordPress.
- Logs independientes: `/var/log/apache2/wordpress_access.log` y `/var/log/apache2/wordpress_error.log`.
- Un tema no predeterminado y una entrada de blog publicada.

## Antes de empezar

1. Lee toda la actividad y crea un snapshot de la máquina virtual.
2. Comprueba que Apache, MariaDB y PHP del servidor LAMP previo están operativos.
3. Anota las decisiones, errores y tiempo invertido mientras trabajas; no intentes reconstruirlos al final.
4. Consulta primero la documentación oficial de WordPress cuando necesites confirmar un requisito o resolver un error.

:::question{id="plan-despliegue" type="long-text" required="true"}
Escribe tu plan de trabajo en cinco fases, indicando qué comprobarás antes de avanzar a la siguiente fase.
:::

:::checkpoint{id="entorno-lamp-listo" required="true"}
Tengo un snapshot de la VM y he comprobado que los servicios LAMP previos están disponibles.
:::
