---
id: kea-dhcp-servicios-en-red
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
  - "RAW/practica_1_kea_dhcp.docx"
related:
  - "[[Indice de actividades]]"
  - "[[Actividad - Practica Kea DHCP Servicios en red]]"
  - "[[Fuente - Practica Kea DHCP Servicios en red]]"
  - "[[Patron - Practica Kea DHCP Servicios en red]]"
tags:
  - actividad
  - aula-step
  - kea
  - dhcp
---

# Kea DHCP Servicios en red

Actividad AulaStep para montar, verificar y ampliar un servidor DHCP con Kea en Ubuntu Server dentro del modulo [[0227 - Servicios en red]].

## Ruta de la actividad

- [[pasos/00-presentacion]]: objetivos y topología del escenario.
- `actividad.yml`: configuracion global.
- [[pasos/01-instalacion]]: instalacion de Kea y preparacion del entorno.
- [[pasos/02-subred-3]]: primera subred DHCP para la red interna 3.
- [[pasos/03-verificacion]]: comprobacion de servicio, concesiones y logs.
- [[pasos/04-subred-2-y-reserva]]: segunda subred y reserva por MAC.
- [[pasos/05-pruebas-finales]]: validación de las redes internas 2 y 3.
- [[pasos/06-relay-red-interna-1]]: extensión a la red interna 1 mediante un relay DHCP.
- [[pasos/07-reflexion]]: reflexión y entrega.

## Enfoque didactico

La actividad trabaja configuración de servicios de red, lectura de logs, verificación de clientes y uso de evidencias. Primero comprueba las redes conectadas directamente a Kea; después incorpora una red remota atendida mediante relay DHCP.
