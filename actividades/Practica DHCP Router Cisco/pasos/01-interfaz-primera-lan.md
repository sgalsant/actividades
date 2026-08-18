---
id: interfaz-primera-lan
titulo: Configurar la puerta de enlace de la primera LAN
duracion_minutos: 15
obligatorio: true
---

La interfaz del router debe pertenecer a la LAN antes de entregar direcciones DHCP.

```text
enable
configure terminal
hostname R_APELLIDO_NOMBRE
interface g0/0/0
 ip address 172.16.0.1 255.255.0.0
 no shutdown
exit
```

:::task{id="configurar-g000" required="true"}
Configura `G0/0/0` con `172.16.0.1/16` y actívala.
:::

Comprueba el resultado:

```text
show ip interface brief
```

`G0/0/0` debe mostrar `172.16.0.1` y estado `up/up`.

:::evidence{id="estado-g000" type="screenshot" required="true"}
Captura de la salida de `show ip interface brief`.
:::
