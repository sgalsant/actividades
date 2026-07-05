---
id: presentacion-actividad
titulo: Presentación, objetivos y escenario
duracion_minutos: 15
obligatorio: true
---

## Objetivos de la práctica

- Configurar un servidor Ubuntu Server virtualizado con acceso remoto por SSH.
- Instalar y poner en marcha un stack LAMP (Linux, Apache, MariaDB, PHP).
- Desplegar páginas web estáticas y dinámicas.
- Gestionar usuarios y permisos de bases de datos.
- Aplicar buenas prácticas básicas de seguridad en servidores.

## Escenario

Trabajarás con una máquina virtual Ubuntu Server 24.04 LTS importada en VirtualBox. Desde tu equipo anfitrión accederás por SSH y navegador gracias al reenvío de puertos.

| Servicio | IP anfitrión | Puerto anfitrión | Puerto invitado |
|---|---|---|---|
| SSH | 127.0.0.1 | 2222 | 22 |
| HTTP | 127.0.0.1 | 8080 | 80 |
| HTTPS | 127.0.0.1 | 8443 | 443 |

## Tabla de registro de configuraciones

Completa esta tabla a medida que avances. La necesitarás durante toda la actividad.

| Concepto | Usuario/Valor | Contraseña | Notas |
|---|---|---|---|
| Hostname del servidor | `server_[tu_nombre]` | - | - |
| Usuario Ubuntu | `analuisa` | `analuisa` | Usuario por defecto de la OVA |
| Usuario root MySQL | `root` | - | NO usar en producción |
| Base de datos | - | - | Nombre de tu BD |
| Usuario Admin BD | - | - | Permisos completos sobre tu BD |
| Usuario CRUD BD | - | - | Solo SELECT, INSERT, UPDATE, DELETE |
| Puerto SSH anfitrión | - | - | Por defecto: 2222 |
| Puerto HTTP anfitrión | - | - | Por defecto: 8080 |

:::note{}
Sustituye `[tu_nombre]` por tu nombre en hostname, usuarios y base de datos para personalizar la actividad.
:::

:::tip{}
**Flujo conceptual del stack LAMP:** el navegador del cliente envía una petición HTTP a Apache; si el contenido es estático, Apache lo sirve directamente, y si es dinámico, lo delega a PHP (`mod_php` o PHP-FPM). Cuando PHP necesita datos, consulta MariaDB/MySQL.
:::

![Portada y diagrama conceptual del stack LAMP](recursos/media/image1.jpg)

## Licencia

Esta actividad se distribuye bajo la licencia Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional.

![Licencia CC BY-NC-SA 4.0](recursos/media/image7.svg)
