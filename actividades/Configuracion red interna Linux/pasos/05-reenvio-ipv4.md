---
id: reenvio-ipv4
titulo: Habilita el reenvío IPv4
duracion_minutos: 20
obligatorio: true
---

El servidor no reenvía paquetes entre interfaces por defecto. Activa el reenvío de forma persistente en `/etc/sysctl.conf`. El valor `1` lo activa, `0` lo desactiva y cualquier valor distinto de cero lo mantiene activo:

:::task{id="habilitar-ip-forward" required="true"}
Abre el archivo, descomenta o añade la siguiente línea y carga la configuración:

```bash
sudo nano /etc/sysctl.conf
```

```ini
net.ipv4.ip_forward=1
```

```bash
sudo sysctl -p
sysctl net.ipv4.ip_forward
```
:::

:::question{id="funcion-ip-forward" type="long-text" required="true"}
Explica por qué necesitas habilitar el reenvío IPv4 en esta topología y qué ocurriría con los paquetes del cliente si `net.ipv4.ip_forward` estuviera a `0`.
:::
