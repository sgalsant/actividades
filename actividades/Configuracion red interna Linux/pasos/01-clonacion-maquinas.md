---
id: clonacion-maquinas
titulo: Crea las máquinas virtuales
duracion_minutos: 20
obligatorio: true
---

Parte de las máquinas base de Ubuntu Desktop y Ubuntu Server en VirtualBox. Crea una clonación enlazada de cada una y genera nuevas direcciones MAC para todos sus adaptadores.

:::tip{}
Una clonación enlazada reutiliza el disco base y reduce el espacio ocupado. No uses la misma MAC en las dos máquinas: VirtualBox y la red no podrían distinguirlas correctamente.
:::

:::task{id="crear-maquinas" required="true"}
Crea las dos máquinas y asígnales nombres que permitan diferenciarlas claramente, por ejemplo, `ubuntu-desktop-red` y `ubuntu-server-gateway`.
:::

:::evidence{id="captura-maquinas" type="screenshot" required="true"}
Adjunta una captura de VirtualBox donde se vean las dos máquinas creadas.
:::
