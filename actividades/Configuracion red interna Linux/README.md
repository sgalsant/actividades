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
  - "RAW/configuracion red linux.docx"
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
  - nat
---

# Configuración de una red interna Linux

Actividad AulaStep para configurar Ubuntu Server como gateway de una red interna Ubuntu mediante Netplan, reenvío IPv4 y NAT.

## Prerrequisitos

Necesitas las máquinas base de Ubuntu Desktop y Ubuntu Server en VirtualBox. Completa el reto 1 antes de continuar con el reto 2: el segundo router reutiliza el gateway y la salida a Internet ya configurados.

## Reto 1: gateway con NAT

- [[pasos/00-presentacion]]: objetivo, topología y evidencias.
- [[pasos/01-clonacion-maquinas]]: creación de las máquinas virtuales.
- [[pasos/02-red-virtualbox]]: adaptadores NAT y redes internas.
- [[pasos/03-reenvio-puertos-ssh]]: reenvío de puertos y acceso SSH desde Windows.
- [[pasos/04-red-servidor]]: Netplan e interfaces del gateway.
- [[pasos/05-red-escritorio]]: configuración del cliente.
- [[pasos/06-reenvio-ipv4]]: habilitación persistente del reenvío.
- [[pasos/07-nat-iptables]]: traducción de direcciones y persistencia.
- [[pasos/08-pruebas-entrega]]: comprobaciones y evidencias del reto 1.

## Reto 2: tres subredes y dos routers

- [[pasos/09-subredes-enrutamiento]]: ampliación a tres subredes, configuración completa de los dos routers y evidencias de conectividad.
- [[pasos/10-reflexion]]: reflexión y entrega.
