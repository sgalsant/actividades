---
id: subred-2-y-reserva
titulo: Segunda subred y reserva por MAC
duracion_minutos: 30
obligatorio: true
---

Amplía el servicio para cubrir la red interna **192.168.2.0/24** y añade una reserva fija para Ubuntu Server 1.

:::task{id="ampliar-configuracion" required="true"}
Actualiza `kea-dhcp4.conf` para incluir la nueva subred y una reserva por `hw-address`.
:::

```bash
sudo nano /etc/kea/kea-dhcp4.conf
sudo systemctl restart kea-dhcp4-server
```

:::warning{}
No copies la MAC de ejemplo: usa la MAC real de la interfaz que conecta Ubuntu Server 1 con la red interna 2.
:::

:::task{id="cambiar-server1-a-dhcp" required="true"}
Cambia la interfaz de Ubuntu Server 1 que conecta con la red interna 2 para que obtenga configuración por DHCP.
:::

:::evidence{id="captura-reserva" type="screenshot" required="true"}
Captura de la reserva configurada y del archivo final de Kea.
:::

:::question{id="ip-reservada" type="short-text" required="true"}
¿Qué dirección debe quedar reservada para Ubuntu Server 1?
:::
