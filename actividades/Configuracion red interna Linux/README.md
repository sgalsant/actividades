---
id: configuracion-red-interna-linux
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
  - "RAW/configuracion red linux - completa.docx"
related:
  - "[[Indice de actividades]]"
  - "[[Actividad - Configuracion red interna Linux]]"
  - "[[Fuente - Configuracion red interna Linux]]"
  - "[[Patron - Red interna Linux con gateway y NAT]]"
tags:
  - actividad
  - aula-step
  - linux
  - red-interna
  - netplan
  - nat
---

# Configuración de red interna Linux

Actividad AulaStep para configurar una red interna entre Ubuntu Desktop y Ubuntu Server, usando el servidor como gateway para el acceso a Internet dentro del módulo [[0227 - Servicios en red]].

## Ruta de la actividad

- [[pasos/00-presentacion]]: objetivos, topología y direccionamiento.
- `actividad.yml`: configuración global.
- [[pasos/01-clonacion-maquinas]]: creación de las máquinas virtuales.
- [[pasos/02-red-virtualbox]]: adaptadores NAT y red interna.
- [[pasos/03-red-servidor]]: Netplan en Ubuntu Server.
- [[pasos/04-red-escritorio]]: configuración del cliente Ubuntu Desktop.
- [[pasos/05-reenvio-ipv4]]: activación de `ip_forward`.
- [[pasos/06-nat-iptables]]: NAT y persistencia con `iptables`.
- [[pasos/07-pruebas-entrega]]: pruebas y evidencias.
- [[pasos/08-reflexion]]: reflexión y exportación.

## Enfoque didáctico

La secuencia conecta la configuración de interfaces, el direccionamiento IP, el reenvío de paquetes y la traducción NAT. Las pruebas distinguen conectividad local, acceso por dirección IP externa y resolución DNS.
