---
id: red-virtualbox
titulo: Configura los adaptadores en VirtualBox
duracion_minutos: 20
obligatorio: true
---

Configura los adaptadores antes de iniciar las máquinas:

| Máquina | Adaptador | Modo |
|---|---|---|
| Ubuntu Server | 1 | NAT |
| Ubuntu Server | 2 | Red interna `red-interna` |
| Ubuntu Desktop | 1 | Red interna `red-interna` |

En VirtualBox, selecciona cada máquina, abre **Configuración → Red**, selecciona el adaptador indicado y aplica el modo correspondiente antes de pasar al siguiente.

:::warning{}
El nombre de la red interna debe coincidir exactamente en ambos adaptadores. Si difiere, las máquinas quedarán aisladas aunque sus direcciones pertenezcan a la misma subred.
:::

:::checkpoint{id="adaptadores-listos" required="true"}
He configurado NAT únicamente en el servidor y la misma red interna en servidor y cliente.
:::
