---
id: reenvio-ipv4
titulo: Habilitar el reenvío IPv4
duracion_minutos: 15
obligatorio: true
---

Un gateway debe recibir paquetes por una interfaz y reenviarlos por otra. Linux lo controla mediante el parámetro `net.ipv4.ip_forward`.

:::task{id="activar-ip-forward" required="true"}
Edita la configuración de `sysctl`:

```bash
sudo nano /etc/sysctl.conf
```

Busca y descomenta, o añade si no existe, esta línea:

```text
net.ipv4.ip_forward=1
```

Aplica el cambio y consulta su valor:

```bash
sudo sysctl -p
sysctl net.ipv4.ip_forward
```
:::

:::note{}
El valor `1` indica que el reenvío está activo. El valor `0` lo desactiva; cualquier valor distinto de cero implica activación.
:::

:::question{id="funcion-ip-forward" type="long-text" required="true"}
Explica por qué el reenvío de paquetes es necesario para que Ubuntu Server actúe como gateway.
:::
