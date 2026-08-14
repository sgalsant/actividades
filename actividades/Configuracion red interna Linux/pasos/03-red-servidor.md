---
id: red-servidor-netplan
titulo: Configurar Ubuntu Server con Netplan
duracion_minutos: 30
obligatorio: true
---

El adaptador NAT recibirá su dirección por DHCP. La interfaz de red interna tendrá la dirección fija `192.168.1.1/24`.

:::task{id="crear-netplan-servidor" required="true"}
Revisa primero los nombres reales de las interfaces:

```bash
ip a
```

Elimina las configuraciones previas de Netplan y crea el archivo nuevo:

```bash
sudo rm /etc/netplan/*
sudo nano /etc/netplan/network-config.yaml
```

Adapta los nombres de interfaz si tu salida de `ip a` es diferente:

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

Aplica la configuración y comprueba que ambas interfaces tienen la dirección esperada:

```bash
sudo netplan apply
sudo ip a
```
:::

:::note{}
La nomenclatura predecible describe la posición de la interfaz: `en` identifica Ethernet, `p0` el bus PCI y `s3` la ranura. No presupongas que un equipo usará siempre los mismos nombres.
:::

:::task{id="proteger-netplan" required="true"}
Restringe el acceso al archivo de configuración para que solo root pueda leerlo y escribirlo:

```bash
sudo chmod 600 /etc/netplan/network-config.yaml
```
:::

:::evidence{id="captura-ip-servidor" type="screenshot" required="true"}
Adjunta una captura de `ip a` donde se vean la interfaz NAT y la interfaz interna con `192.168.1.1/24`.
:::
