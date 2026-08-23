---
id: red-servidor
titulo: Configura el gateway con Netplan
duracion_minutos: 35
obligatorio: true
---

En Ubuntu Server, la interfaz NAT obtiene su dirección por DHCP y la interfaz de red interna usa `192.168.1.1/24`.

:::task{id="netplan-servidor" required="true"}
1. Identifica los nombres de las interfaces con `ip a`. Antes de sustituir una configuración, haz una copia de seguridad de Netplan. Después retira los YAML anteriores del directorio activo: Netplan combina todos los YAML de `/etc/netplan/`, por lo que un fichero antiguo con DHCP puede alterar esta topología. Esta práctica usa máquinas de laboratorio: no hagas esto en un servidor en producción.

```bash
sudo ip a
sudo mkdir -p /etc/netplan.backup
sudo cp -a /etc/netplan/. /etc/netplan.backup/
sudo rm -f /etc/netplan/*.yaml
```

2. Crea `/etc/netplan/network-config.yaml`. Ajusta los nombres si tus interfaces no son `enp0s3` y `enp0s8`; conserva únicamente la configuración que vayas a usar en esta práctica:

```bash
sudo nano /etc/netplan/network-config.yaml
```

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

3. Protege el archivo antes de aplicar la configuración. Netplan rechaza o avisa sobre ficheros accesibles por otros usuarios:

```bash
sudo chmod 600 /etc/netplan/network-config.yaml
sudo netplan apply
```

4. Comprueba que la interfaz NAT recibió una dirección por DHCP y que la interfaz interna tiene `192.168.1.1/24`:

```bash
sudo ip a
```
:::

:::note{}
Los nombres como `enp0s3` describen una interfaz Ethernet situada en un bus y ranura PCI: `en` significa Ethernet; las interfaces inalámbricas empiezan por `wl`; `p0` identifica el bus PCI 0 y `s3` la ranura 3. No los copies sin verificar: cambian según el orden de adaptadores de cada máquina virtual.
:::
