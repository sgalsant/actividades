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
1. Antes de clonar, abre **Archivo → Preferencias → General** y configura la carpeta predeterminada de máquinas como `D:\2smr`.

![Preferencias de VirtualBox con la carpeta predeterminada](recursos/media/image2.png)

2. Haz clic derecho sobre la máquina base de Ubuntu Desktop y selecciona **Clonar**. En el asistente, escribe un nombre que permita identificar el equipo, por ejemplo, `ubuntu-desktop-red`, confirma la ruta y selecciona **Generar nuevas direcciones MAC para todos los adaptadores de red**.

![Nombre, ruta y política de direcciones MAC](recursos/media/image3.png)

3. En la pantalla **Tipo de clonación**, selecciona **Clonación enlazada** y termina el asistente.

![Selección de clonación enlazada](recursos/media/image4.png)

4. Repite los mismos pasos con la máquina base de Ubuntu Server y asígnale un nombre como `ubuntu-server-gateway`.
:::

:::evidence{id="captura-maquinas" type="screenshot" required="true"}
Adjunta una captura de VirtualBox donde se vean las dos máquinas creadas.
:::
