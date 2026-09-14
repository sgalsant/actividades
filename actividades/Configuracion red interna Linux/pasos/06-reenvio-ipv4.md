---
id: reenvio-ipv4
titulo: Habilita el reenvío IPv4
duracion_minutos: 20
obligatorio: true
---

El reenvío IPv4 permite que un equipo reciba un paquete por una interfaz de red y lo envíe por otra según su tabla de rutas. En esta topología, el Ubuntu Server recibe por su interfaz interna los paquetes del cliente Ubuntu Desktop y debe reenviarlos por su interfaz NAT para que puedan salir hacia Internet.

El servidor no reenvía paquetes entre interfaces por defecto: actúa como destino final de los paquetes que recibe. Activar `net.ipv4.ip_forward` lo convierte en un encaminador. Este ajuste no modifica direcciones IP; la traducción de direcciones necesaria para salir a Internet se configurará mediante NAT en el paso siguiente. 

:::task{id="habilitar-ip-forward" required="true"}
1. En el servidor, activamos ip_forward registrandolo en un nuevo fichero de configuración en el directorio /etc/sysctl.d:

```bash
echo 'net.ipv4.ip_forward = 1' | sudo tee /etc/sysctl.d/99-ip-forward.conf
```

2. Rearga la configuración sin reiniciar:

```bash
sudo sysctl --system
```

3. Comprueba el valor activo. Debe mostrar `net.ipv4.ip_forward = 1`:

```bash
sysctl net.ipv4.ip_forward
```
:::

:::question{id="funcion-ip-forward" type="long-text" required="true"}
Explica por qué necesitas habilitar el reenvío IPv4 en esta topología y qué ocurriría con los paquetes del cliente si `net.ipv4.ip_forward` estuviera a `0`.
:::
