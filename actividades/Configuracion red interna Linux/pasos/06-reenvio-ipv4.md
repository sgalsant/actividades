---
id: reenvio-ipv4
titulo: Habilita el reenvío IPv4
duracion_minutos: 20
obligatorio: true
---

El reenvío IPv4 permite que un equipo reciba un paquete por una interfaz de red y lo envíe por otra según su tabla de rutas. En esta topología, el Ubuntu Server recibe por su interfaz interna los paquetes del cliente Ubuntu Desktop y debe reenviarlos por su interfaz NAT para que puedan salir hacia Internet.

El servidor no reenvía paquetes entre interfaces por defecto: actúa como destino final de los paquetes que recibe. Activar `net.ipv4.ip_forward` lo convierte en un encaminador. Este ajuste no modifica direcciones IP; la traducción de direcciones necesaria para salir a Internet se configurará mediante NAT en el paso siguiente. Activa el reenvío de forma persistente en `/etc/sysctl.conf`.

:::task{id="habilitar-ip-forward" required="true"}
1. Abre el archivo de configuración de `sysctl`:

```bash
sudo nano /etc/sysctl.conf
```

2. Busca la línea siguiente. Si empieza por `#`, elimina ese carácter; si no existe, añádela. El valor `1` activa el reenvío, `0` lo desactiva y cualquier valor distinto de cero lo mantiene activo:

```ini
net.ipv4.ip_forward=1
```

3. Guarda el archivo y carga la configuración sin reiniciar:

```bash
sudo sysctl -p
```

4. Comprueba el valor activo. Debe mostrar `net.ipv4.ip_forward = 1`:

```bash
sysctl net.ipv4.ip_forward
```
:::

:::question{id="funcion-ip-forward" type="long-text" required="true"}
Explica por qué necesitas habilitar el reenvío IPv4 en esta topología y qué ocurriría con los paquetes del cliente si `net.ipv4.ip_forward` estuviera a `0`.
:::
