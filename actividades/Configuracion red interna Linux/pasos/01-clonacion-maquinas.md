---
id: clonacion-maquinas
titulo: Crea las máquinas virtuales
duracion_minutos: 20
obligatorio: true
---

Parte de las máquinas base de Ubuntu Desktop y Ubuntu Server en VirtualBox. Crea una clonación enlazada de cada una y genera nuevas direcciones MAC para todos sus adaptadores.

![Asistente de clonación enlazada de VirtualBox](recursos/media/image2.png)

![Selección de nombre para la máquina clonada](recursos/media/image3.png)

![Confirmación de la clonación en VirtualBox](recursos/media/image4.png)

:::tip{}
Una clonación enlazada reutiliza el disco base y reduce el espacio ocupado. No uses la misma MAC en las dos máquinas: VirtualBox y la red no podrían distinguirlas correctamente.
:::

Antes de clonar, configura las preferencias de VirtualBox para que las máquinas se guarden en `D:\2smr`. Comprueba que esa carpeta aparece como ubicación de destino durante el asistente de clonación.

:::task{id="crear-maquinas" required="true"}
Crea primero el clon enlazado de Ubuntu Desktop y después el de Ubuntu Server. Asígnales nombres que permitan diferenciarlas claramente, por ejemplo, `ubuntu-desktop-red` y `ubuntu-server-gateway`.
:::

:::evidence{id="captura-maquinas" type="screenshot" required="true"}
Adjunta una captura de VirtualBox donde se vean las dos máquinas creadas.
:::
