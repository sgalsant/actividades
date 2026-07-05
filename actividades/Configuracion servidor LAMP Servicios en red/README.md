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
familia_profesional: Informatica y Comunicaciones
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

# Configuracion servidor LAMP Servicios en red

Actividad AulaStep para instalar y configurar un servidor LAMP (Linux, Apache, MariaDB, PHP) en Ubuntu Server dentro del modulo [[0227 - Servicios en red]].

## Ruta de la actividad

- [[pasos/00-presentacion]]: objetivos, escenario y tabla de registro.
- `actividad.yml`: configuracion global.
- [[pasos/01-reto-0-preparacion-entorno]]: importacion de la VM y reenvio de puertos.
- [[pasos/02-reto-1-personalizacion-servidor]]: hostname y `/etc/hosts`.
- [[pasos/03-reto-2-firewall]]: configuracion de UFW.
- [[pasos/04-reto-3-apache]]: instalacion de Apache Web Server.
- [[pasos/05-reto-4-mariadb]]: instalacion y asegurado de MariaDB.
- [[pasos/06-reto-5-php-modulo]]: instalacion de PHP como modulo de Apache.
- [[pasos/07-reto-6-paginas-web]]: creacion y transferencia de paginas web.
- [[pasos/08-reto-7-phpmyadmin]]: instalacion de phpMyAdmin.
- [[pasos/09-reto-8-php-fpm]]: migracion a PHP-FPM.
- [[pasos/10-reto-9-gestion-bd]]: gestion de bases de datos y permisos.
- [[pasos/11-troubleshooting]]: problemas comunes y soluciones.
- [[pasos/12-verificacion-entrega]]: checklist final y recursos.
- [[pasos/13-reflexion]]: reflexion y entrega.

## Enfoque didactico

La actividad trabaja configuracion de servicios web, bases de datos, seguridad basica, transferencia de archivos y gestion de permisos. La secuencia sigue el patron reutilizable derivado de la fuente original e incluye el escenario inicial y los objetivos de la practica.
