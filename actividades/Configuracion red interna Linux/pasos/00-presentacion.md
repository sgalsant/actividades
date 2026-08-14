---
id: presentacion-red-interna
titulo: Presentación, objetivos y topología
duracion_minutos: 10
obligatorio: true
---

## Objetivo de la actividad

Crearás una red interna entre Ubuntu Desktop y Ubuntu Server. Al terminar, Ubuntu Server actuará como **gateway**: el equipo de escritorio se comunicará con el servidor y accederá a Internet a través de él.

## Topología y direccionamiento

| Equipo | Interfaz | Configuración |
|---|---|---|
| Ubuntu Server | Adaptador 1 | NAT por DHCP, con acceso a Internet |
| Ubuntu Server | Adaptador 2 | Red interna `192.168.1.1/24` |
| Ubuntu Desktop | Adaptador 1 | Red interna `192.168.1.2/24` |

En Ubuntu Desktop usarás como gateway `192.168.1.1` y como DNS `8.8.8.8`.

:::note{}
Los nombres de interfaz pueden variar. La guía usa `enp0s3` para el adaptador NAT y `enp0s8` para la red interna porque son los nombres habituales con ese orden en VirtualBox. Compruébalos siempre con `ip a`.
:::

:::checkpoint{id="check-topologia" required="true"}
He identificado qué adaptador conecta a Internet y cuál conecta con la red interna en cada máquina virtual.
:::
