---
id: presentacion-actividad
titulo: Presentación, objetivos y topología
duracion_minutos: 15
obligatorio: true
---

## Objetivos de la práctica

- Configurar un servidor DHCP con Kea en Ubuntu Server 2.
- Repartir direcciones IP dinámicas en la red interna 3 (`192.168.3.0/24`).
- Ampliar la configuración para dar servicio también en la red interna 2 (`192.168.2.0/24`).
- Crear una reserva de IP fija para Ubuntu Server 1 en la red interna 2.

## Escenario de la topología

Según la topología ya desplegada en VirtualBox:

- Ubuntu Server 1:
  - `eth0`: DHCP (internet)
  - `eth1`: `192.168.1.1` (red interna 1)
  - `eth2`: `192.168.2.1` (red interna 2)
- Ubuntu Server 2 (servidor DHCP):
  - `eth0`: `192.168.2.2` (red interna 2)
  - `eth1`: `192.168.3.1` (red interna 3)
- Ubuntu Desktop 1: `192.168.1.2` (red interna 1, cliente de Server 1)
- Ubuntu Desktop 2: `192.168.3.2` (red interna 3, cliente de Server 2 vía DHCP)

![Topología del escenario](recursos/media/image1.png)

:::note{}
Antes de seguir, identifica qué interfaz de red conecta cada máquina con la red interna que vas a usar.
:::
