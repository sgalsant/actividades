---
id: clonacion-maquinas
titulo: Crear las máquinas virtuales
duracion_minutos: 20
obligatorio: true
---

Crearás una máquina Ubuntu Desktop y otra Ubuntu Server mediante **clonación enlazada**. Esta modalidad comparte el disco base entre las copias y reduce el espacio ocupado.

:::task{id="clonar-ubuntu-desktop" required="true"}
1. En VirtualBox, selecciona la máquina base de Ubuntu Desktop.
2. Haz clic derecho y elige **Clonar**.
3. Selecciona **Clonación enlazada** y genera nuevas direcciones MAC para todos los adaptadores.
4. Asigna un nombre identificable, por ejemplo, `Ubuntu Desktop 1`.
5. Comprueba que la máquina se guarda en la ubicación de trabajo configurada en VirtualBox.
:::

:::task{id="clonar-ubuntu-server" required="true"}
Repite el proceso a partir de la máquina base de Ubuntu Server. Mantén nombres que permitan distinguir sin ambigüedad el servidor del cliente de escritorio.
:::

:::warning{}
No reutilices las direcciones MAC de la máquina base. Dos máquinas con la misma MAC en la misma red provocan conflictos difíciles de diagnosticar.
:::
