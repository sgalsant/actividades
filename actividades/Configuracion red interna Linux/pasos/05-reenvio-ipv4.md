---
id: reenvio-ipv4
titulo: Habilita el reenvío IPv4
duracion_minutos: 20
obligatorio: true
---

El servidor no reenvía paquetes entre interfaces por defecto. Activa el reenvío de forma persistente en `/etc/sysctl.conf`:

:::task{id="habilitar-ip-forward" required="true"}
Descomenta o añade la siguiente línea y carga la configuración:

```ini
net.ipv4.ip_forward=1
```

```bash
sudo sysctl -p
sysctl net.ipv4.ip_forward
```
:::

:::question{id="funcion-ip-forward" type="long-text" required="true"}
Explica qué ocurriría con los paquetes del cliente si `net.ipv4.ip_forward` estuviera a `0`.
:::
