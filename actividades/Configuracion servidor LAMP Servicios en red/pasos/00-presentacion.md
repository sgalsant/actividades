---
id: presentacion-actividad
titulo: Presentacion, objetivos y escenario
duracion_minutos: 15
obligatorio: true
---

## Objetivos de la practica

- Configurar un servidor Ubuntu Server virtualizado con acceso remoto por SSH.
- Instalar y poner en marcha un stack LAMP (Linux, Apache, MariaDB, PHP).
- Desplegar paginas web estaticas y dinamicas.
- Gestionar usuarios y permisos de bases de datos.
- Aplicar buenas practicas basicas de seguridad en servidores.

## Escenario

Trabajaras con una maquina virtual Ubuntu Server 24.04 LTS importada en VirtualBox. Desde tu equipo anfitrion accederas por SSH y navegador gracias al reenvio de puertos.

| Servicio | IP anfitrion | Puerto anfitrion | Puerto invitado |
|---|---|---|---|
| SSH | 127.0.0.1 | 2222 | 22 |
| HTTP | 127.0.0.1 | 8080 | 80 |
| HTTPS | 127.0.0.1 | 8443 | 443 |

## Tabla de registro de configuraciones

Completa esta tabla a medida que avances. La necesitaras durante toda la actividad.

| Concepto | Usuario/Valor | Contrasena | Notas |
|---|---|---|---|
| Hostname del servidor | `server_[tu_nombre]` | - | - |
| Usuario Ubuntu | `analuisa` | `analuisa` | Usuario por defecto de la OVA |
| Usuario root MySQL | `root` | - | NO usar en produccion |
| Base de datos | - | - | Nombre de tu BD |
| Usuario Admin BD | - | - | Permisos completos sobre tu BD |
| Usuario CRUD BD | - | - | Solo SELECT, INSERT, UPDATE, DELETE |
| Puerto SSH anfitrion | - | - | Por defecto: 2222 |
| Puerto HTTP anfitrion | - | - | Por defecto: 8080 |

:::note{}
Sustituye `[tu_nombre]` por tu nombre en hostname, usuarios y base de datos para personalizar la actividad.
:::

![Portada y diagrama conceptual del stack LAMP](recursos/media/image1.jpg)

## Licencia

Esta actividad se distribuye bajo la licencia Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional.

![Licencia CC BY-NC-SA 4.0](recursos/media/image7.svg)
