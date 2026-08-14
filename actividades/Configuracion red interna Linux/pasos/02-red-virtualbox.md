---
id: red-virtualbox
titulo: Configurar la red en VirtualBox
duracion_minutos: 15
obligatorio: true
---

Configura los adaptadores antes de iniciar las máquinas.

| Máquina | Adaptador | Modo | Red |
|---|---|---|---|
| Ubuntu Server | 1 | NAT | Internet |
| Ubuntu Server | 2 | Red interna | `red-interna` |
| Ubuntu Desktop | 1 | Red interna | `red-interna` |

:::task{id="configurar-adaptadores" required="true"}
En **Configuración > Red** de cada máquina, crea los adaptadores de la tabla. Las dos interfaces internas deben usar exactamente el mismo nombre de red, por ejemplo `red-interna`.
:::

:::question{id="comprobar-red-interna" type="short-text" required="true"}
¿Qué condición deben cumplir los adaptadores internos de Ubuntu Server y Ubuntu Desktop para poder comunicarse?
:::

:::tip{}
La red NAT del servidor da salida a Internet al servidor, pero no convierte automáticamente al servidor en gateway del cliente. Ese trabajo se hará con reenvío IPv4 y NAT.
:::
