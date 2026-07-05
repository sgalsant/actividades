---
id: configuracion-servidor-lamp-servicios-en-red
tipo: overview
dominio: programaciones-didacticas
estado: activo
prioridad_consulta: alta
vigencia: no_aplica
fuente_rol: patron
vigencia_estado: no_aplica
etapa: Grado Medio
familia_profesional: Informática y Comunicaciones
ciclo: SMR
curso: "2"
modulo_materia: "0227 Servicios en red"
fuente_local:
  - "RAW/1 actividad_lamp.docx"
related:
  - "[[Indice de actividades]]"
  - "[[Actividad - Configuracion servidor LAMP Servicios en red]]"
  - "[[Fuente - Actividad LAMP Servicios en red]]"
  - "[[Patron - Practica LAMP Servicios en red]]"
tags:
  - actividad
  - aula-step
  - lamp
  - apache
  - mariadb
  - php
---

# Configuración servidor LAMP Servicios en red

Actividad AulaStep para instalar y configurar un servidor LAMP (Linux, Apache, MariaDB, PHP) en Ubuntu Server dentro del módulo [[0227 - Servicios en red]].

## Ruta de la actividad

- [[pasos/00-presentacion]]: objetivos, escenario y tabla de registro.
- `actividad.yml`: configuración global.
- [[pasos/01-reto-0-preparacion-entorno]]: importación de la VM y reenvío de puertos.
- [[pasos/02-reto-1-personalizacion-servidor]]: hostname y `/etc/hosts`.
- [[pasos/03-reto-2-firewall]]: configuración de UFW.
- [[pasos/04-reto-3-apache]]: instalación de Apache Web Server.
- [[pasos/05-reto-4-mariadb]]: instalación y asegurado de MariaDB.
- [[pasos/06-reto-5-php-modulo]]: instalación de PHP como módulo de Apache.
- [[pasos/07-reto-6-paginas-web]]: creación y transferencia de páginas web.
- [[pasos/08-reto-7-phpmyadmin]]: instalación de phpMyAdmin.
- [[pasos/09-reto-8-php-fpm]]: migración a PHP-FPM.
- [[pasos/10-reto-9-gestion-bd]]: gestión de bases de datos y permisos.
- [[pasos/11-troubleshooting]]: problemas comunes y soluciones.
- [[pasos/12-verificacion-entrega]]: checklist final y recursos.
- [[pasos/13-reflexion]]: reflexión y entrega.

## Enfoque didáctico

La actividad trabaja configuración de servicios web, bases de datos, seguridad básica, transferencia de archivos y gestión de permisos. La secuencia sigue el patrón reutilizable derivado de la fuente original e incluye el escenario inicial y los objetivos de la práctica.
