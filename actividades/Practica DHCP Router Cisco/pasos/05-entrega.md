---
id: entrega
titulo: Verificar y preparar la entrega
duracion_minutos: 15
obligatorio: true
---

Revisa que la práctica contiene las dos LAN y que las evidencias proceden de tu propia topología.

## Checklist

- El router está identificado y las dos interfaces están activas.
- Los dos pools DHCP tienen la red y puerta de enlace correctas.
- Los rangos reservados no se entregan a los clientes.
- `show ip dhcp binding` muestra las concesiones.
- PC1 tiene una IP, máscara y puerta de enlace válidas.
- El archivo se guarda como `APELLIDOS_Nombre_Grupo_DHCP.pkt`.

:::question{id="mac-pc1" type="short-text" required="true"}
Según `show ip dhcp binding`, ¿qué MAC tiene PC1?
:::

:::question{id="ip-pc1" type="short-text" required="true"}
Según `show ip dhcp binding`, ¿qué IP recibió PC1?
:::

:::evidence{id="entrega-final" type="file" required="true"}
Adjunta el archivo `.pkt` y las capturas solicitadas por tu docente.
:::
