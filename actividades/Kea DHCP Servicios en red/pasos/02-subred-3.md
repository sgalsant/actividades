---
id: subred-3
titulo: Primera subred DHCP para la red interna 3
duracion_minutos: 20
obligatorio: true
---

Configura Kea para repartir direcciones en la red interna **192.168.3.0/24**.

### Configuración base de Kea

```json
{
  "Dhcp4": {
    "interfaces-config": {
      "interfaces": [ "enp0s8" ]
    },
    "lease-database": {
      "type": "memfile",
      "persist": true,
      "name": "/var/lib/kea/kea-leases4.csv"
    },
    "subnet4": [
      {
        "subnet": "192.168.3.0/24",
        "pools": [
          { "pool": "192.168.3.100 - 192.168.3.200" }
        ],
        "option-data": [
          { "name": "routers", "data": "192.168.3.1" },
          { "name": "domain-name-servers", "data": "8.8.8.8" }
        ]
      }
    ]
  }
}
```

:::task{id="configurar-subred-3" required="true"}
Edita `/etc/kea/kea-dhcp4.conf`, define la interfaz correcta y crea un pool para `192.168.3.100 - 192.168.3.200`.
:::

```bash
cd /etc/kea
sudo mv kea-dhcp4.conf kea-dhcp4.conf.old
sudo nano kea-dhcp4.conf
sudo systemctl restart kea-dhcp4-server
```

:::warning{}
La interfaz de red puede no llamarse igual en todos los equipos. Verifica el nombre real antes de guardar la configuración.
:::

:::question{id="rango-subred-3" type="short-text" required="true"}
¿Qué rango de direcciones debe entregar Kea en esta primera parte?
:::

:::evidence{id="captura-config-subred3" type="screenshot" required="true"}
Captura de la configuración de Kea o del fragmento relevante del archivo `kea-dhcp4.conf`.
:::
