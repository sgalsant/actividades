---
id: subredes-enrutamiento
titulo: Amplía la red con un segundo router
duracion_minutos: 75
obligatorio: true
---

En el reto 2 añadirás una segunda red `192.168.2.0/24`, un segundo Ubuntu Server y una tercera red `192.168.3.0/24`.

![Topología del reto 2](recursos/media/image7.png)

| Equipo | Interfaz | Conexión y dirección |
|---|---|---|
| Servidor 1 | `enp0s3` | Adaptador NAT de VirtualBox; salida a Internet por DHCP. |
| Servidor 1 | `enp0s8` | Red interna `red-interna`; conecta con Desktop 1 mediante `192.168.1.1/24`. |
| Servidor 1 | `enp0s9` | Nueva red interna `red-interna-2`; conecta directamente con Servidor 2 mediante `192.168.2.1/24`. |
| Servidor 2 | `enp0s3` | Red interna `red-interna-2`; conecta con `enp0s9` de Servidor 1 mediante `192.168.2.2/24`. |
| Servidor 2 | `enp0s8` | Red interna `red-interna-3`; conecta con Desktop 2 mediante `192.168.3.1/24`. |
| Desktop 2 | Adaptador interno | Red interna `red-interna-3`; usa `192.168.3.2/24`, gateway `192.168.3.1` y DNS `8.8.8.8`. |

:::note{}
Servidor 1 conoce directamente las redes `192.168.1.0/24` y `192.168.2.0/24`, pero no conoce `192.168.3.0/24`; por eso su ruta apunta a `192.168.2.2`, que es la interfaz de Servidor 2 conectada a `red-interna-2`. Servidor 2 usa `192.168.2.1` como ruta por defecto porque ese es Servidor 1, el equipo que ya tiene salida a Internet.
:::

En VirtualBox añade al primer servidor un tercer adaptador en modo **Red interna** con nombre `red-interna-2`. Crea el segundo Ubuntu Server con dos adaptadores, ambos en modo **Red interna**: `red-interna-2` y `red-interna-3`.

:::task{id="ampliar-servidor-uno" required="true"}
1. En VirtualBox, añade al primer servidor un tercer adaptador en modo **Red interna** con nombre `red-interna-2`. Será normalmente `enp0s9`, pero compruébalo con `ip a`: esta interfaz conecta Servidor 1 con Servidor 2.

2. Abre `/etc/netplan/network-config.yaml`. Conserva las interfaces existentes (`enp0s3` para NAT y `enp0s8` para `192.168.1.1/24`) y añade, bajo `network.ethernets`, la nueva interfaz y su ruta:

```yaml
    enp0s9:
      addresses:
        - 192.168.2.1/24
      routes:
        - to: 192.168.3.0/24
          via: 192.168.2.2
```

3. Ajusta el nombre de interfaz si es distinto, protege el fichero y aplica los cambios:

```bash
sudo chmod 600 /etc/netplan/network-config.yaml
sudo netplan apply
ip a
ip route
```
:::

:::checkpoint{id="servidor-uno-ampliado" required="true"}
Servidor 1 muestra una interfaz con `192.168.2.1/24` y una ruta a `192.168.3.0/24` vía `192.168.2.2`.
:::

:::task{id="configurar-servidor-dos" required="true"}
1. En VirtualBox, crea el segundo servidor con dos adaptadores en modo **Red interna**: `red-interna-2` conecta con Servidor 1 y `red-interna-3` conecta con Desktop 2. Comprueba con `ip a` que los nombres reales corresponden a esos enlaces; el ejemplo usa `enp0s3` y `enp0s8`.

2. Habilita el reenvío IPv4 como hiciste en el reto 1: añade `net.ipv4.ip_forward=1` en `/etc/sysctl.conf`, ejecuta `sudo sysctl -p` y comprueba el valor con `sysctl net.ipv4.ip_forward`.

3. En una máquina base puede existir un YAML previo. Haz una copia de seguridad y retíralo de `/etc/netplan/` para evitar que Netplan lo fusione con esta configuración. Después crea `/etc/netplan/network-config.yaml`, ajustando los nombres de interfaz si es necesario:

```bash
sudo mkdir -p /etc/netplan.backup
sudo cp -a /etc/netplan/. /etc/netplan.backup/
sudo rm -f /etc/netplan/*.yaml
sudo nano /etc/netplan/network-config.yaml
```

```yaml
network:
  version: 2
  ethernets:
    enp0s3:
      addresses:
        - 192.168.2.2/24
      nameservers:
        addresses: [8.8.8.8]
      routes:
        - to: default
          via: 192.168.2.1
    enp0s8:
      addresses:
        - 192.168.3.1/24
```

4. Protege, aplica y revisa la configuración:

```bash
sudo chmod 600 /etc/netplan/network-config.yaml
sudo netplan apply
ip a
ip route
```
:::

:::checkpoint{id="servidor-dos-configurado" required="true"}
Servidor 2 muestra `192.168.2.2/24` y `192.168.3.1/24`; su ruta por defecto apunta a `192.168.2.1`.
:::

:::task{id="configurar-desktop-dos" required="true"}
1. Crea Desktop 2 en VirtualBox con un adaptador en modo **Red interna** llamado `red-interna-3`.

2. Desde la configuración de red de Ubuntu Desktop, asigna `192.168.3.2/24`, gateway `192.168.3.1` y DNS `8.8.8.8`.

3. Comprueba con `ip a` que Desktop 2 tiene la dirección configurada antes de iniciar las pruebas de conectividad.
:::

:::task{id="probar-tres-subredes" required="true"}
Desde Desktop 2 prueba el enlace directo con Servidor 2, el salto a Servidor 1, la salida a Internet y DNS:

```bash
ping 192.168.3.1
ping 192.168.2.1
ping 8.8.8.8
ping www.google.es
```

Reinicia Desktop 2, Servidor 2 y Servidor 1; después repite las cuatro pruebas.
:::

:::evidence{id="captura-tres-subredes" type="screenshot" required="true"}
Adjunta una captura de Desktop 2 donde se vean los pings a `192.168.3.1`, `192.168.2.1`, `8.8.8.8` y `www.google.es`.
:::

:::evidence{id="captura-tres-subredes-reinicio" type="screenshot" required="true"}
Adjunta una segunda captura posterior al reinicio que muestre conectividad IP externa y resolución DNS.
:::
