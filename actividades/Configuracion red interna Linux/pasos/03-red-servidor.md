---
id: red-servidor
titulo: Configura el gateway con Netplan
duracion_minutos: 35
obligatorio: true
---

En Ubuntu Server, la interfaz NAT obtiene su dirección por DHCP y la interfaz de red interna usa `192.168.1.1/24`.

:::task{id="netplan-servidor" required="true"}
Identifica los nombres de las interfaces con `ip a`. Crea `/etc/netplan/network-config.yaml` y ajusta los nombres si no son `enp0s3` y `enp0s8`:

```yaml
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: true
    enp0s8:
      addresses:
        - 192.168.1.1/24
```

Aplica y verifica la configuración:

```bash
sudo netplan apply
sudo ip a
```
:::

:::note{}
Los nombres como `enp0s3` describen una interfaz Ethernet situada en un bus y ranura PCI. No los copies sin verificar: cambian según el orden de adaptadores de cada máquina virtual.
:::
