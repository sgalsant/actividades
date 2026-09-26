---
id: subred-2-y-reserva
titulo: Segunda subred y reserva por MAC
duracion_minutos: 30
obligatorio: true
---

Esta ampliación cubre la red interna **192.168.2.0/24** y añade una reserva fija para Ubuntu Server 1.

### Configuración ampliada de Kea

```json
{
  "Dhcp4": {
    "interfaces-config": {
      "interfaces": [ "enp0s8", "enp0s3" ]
    },
    "lease-database": {
      "type": "memfile",
      "persist": true,
      "name": "/var/lib/kea/kea-leases4.csv"
    },
    "subnet4": [
      {
        "id": 1,
        "subnet": "192.168.3.0/24",
        "pools": [
          { "pool": "192.168.3.100 - 192.168.3.200" }
        ],
        "option-data": [
          { "name": "routers", "data": "192.168.3.1" },
          { "name": "domain-name-servers", "data": "8.8.8.8" }
        ]
      },
      {
        "id": 2,
        "subnet": "192.168.2.0/24",
        "pools": [
          { "pool": "192.168.2.100 - 192.168.2.150" }
        ],
        "reservations": [
          {
            "hw-address": "08:00:27:de:ad:be",
            "ip-address": "192.168.2.1"
          }
        ]
      }
    ]
  }
}
```

Los parámetros de la primera subred se explican en el [paso anterior](paso:subred-3). La ampliación añade:

| Parámetro | Función en esta práctica |
|---|---|
| `interfaces-config.interfaces` (segunda entrada) | Hace que Kea también escuche en la interfaz de Ubuntu Server 2 conectada a la red interna 2. Ambos nombres del ejemplo son orientativos. |
| `subnet4` (segundo objeto) | Define `192.168.2.0/24` además de la red 3; no reemplaza la primera subred. |
| `id` (segundo objeto) | Asigna el ID único `2` a `192.168.2.0/24`; la primera subred conserva el ID `1`. Los ID deben ser enteros positivos, únicos en la configuración y mantenerse sin cambios al ampliarla. |
| `pools.pool` de la red 2 | Reserva `192.168.2.100 - 192.168.2.150` para concesiones dinámicas. |
| `reservations` | Define una asignación específica dentro de la subred 2. |
| `hw-address` | Identifica la MAC de **la interfaz de Ubuntu Server 1 conectada a la red 2**, no la de otra tarjeta. La MAC mostrada es solo un ejemplo. |
| `ip-address` | Concede `192.168.2.1` a esa MAC. Está en la subred 2 y fuera del pool dinámico, para que no se asigne a otro cliente. |

La red 2 no anuncia DNS ni puerta de enlace en este ejemplo; no se deducen esas opciones de la red 3. La reserva **no cambia la interfaz del cliente a DHCP**: hay que configurar Ubuntu Server 1 aparte.

:::task{id="ampliar-configuracion" required="true"}
En Ubuntu Server 1, consulta la MAC de la interfaz conectada a la red interna 2 con `ip link show` y anótala. En Ubuntu Server 2, identifica con `ip -br -4 address` sus interfaces de las redes 2 y 3. Antes de editar `kea-dhcp4.conf`, guarda una copia de seguridad; luego aplica el ejemplo ampliado, conserva la red 3, sustituye los nombres de interfaz y la MAC, y comprueba que `192.168.2.1` no aparece en el pool dinámico ni está asignada a otro equipo. Ejecuta los comandos uno por uno. Valida el archivo y revisa el resultado antes de reiniciar; si la validación falla, detente, restaura la copia y vuelve a validarla. Reinicia Kea solo cuando la prueba pase.

```bash
ip -br -4 address
sudo cp --archive --no-clobber /etc/kea/kea-dhcp4.conf /etc/kea/kea-dhcp4.conf.pre-subnet-2.bak
sudo nano /etc/kea/kea-dhcp4.conf
```
Valida el archivo y revisa el resultado. Si Kea informa un error, detente y corrige o restaura la copia; no reinicies.

```bash
sudo -u _kea kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
```
Solo si la validación pasa sin errores, reinicia Kea y consulta el estado:

```bash
sudo systemctl restart kea-dhcp4-server
systemctl status kea-dhcp4-server --no-pager
```
Para restaurar la copia tras un error, ejecuta este comando desde Ubuntu Server 2:

```bash
sudo cp /etc/kea/kea-dhcp4.conf.pre-subnet-2.bak /etc/kea/kea-dhcp4.conf
```
Valida la configuración restaurada y revisa la salida:

```bash
sudo -u _kea kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
```
Solo si la validación pasa, reinicia Kea y comprueba el estado:

```bash
sudo systemctl restart kea-dhcp4-server
systemctl status kea-dhcp4-server --no-pager
```

La opción `--no-clobber` conserva la primera copia de seguridad si repites el paso.
La tarea termina con la configuración válida y `systemctl status kea-dhcp4-server` muestra `active (running)` en Ubuntu Server 2. `status` consulta el estado; `sudo systemctl restart kea-dhcp4-server` reinicia el servicio para cargar la configuración validada.
:::

:::warning{}
No copies la MAC de ejemplo: usa la MAC real de la interfaz que conecta Ubuntu Server 1 con la red interna 2.
:::

:::task{id="cambiar-server1-a-dhcp" required="true"}
Desde la **consola de VirtualBox** de Ubuntu Server 1, localiza con `ip -br -4 address` la interfaz de la red interna 2 y el archivo de Netplan que la configura en `/etc/netplan/`. Guarda una copia de ese archivo. Cambia **solo esa interfaz** de dirección estática `192.168.2.1` a `dhcp4: true`, sin alterar las interfaces de las redes 1 o Internet. Aplica la configuración desde la consola y comprueba que la interfaz recibe `192.168.2.1`.

```bash
ip -br -4 address
ls /etc/netplan/
sudo cp /etc/netplan/NOMBRE.yaml /etc/netplan/NOMBRE.yaml.bak
sudo nano /etc/netplan/NOMBRE.yaml
sudo netplan generate
sudo netplan apply
ip -br -4 address
```

Sustituye `NOMBRE.yaml` por el nombre real; no copies el marcador literalmente. Si `netplan generate` informa errores, corrige el archivo antes de aplicar. Si tras `netplan apply` no aparece la dirección reservada o se pierde conectividad, restaura **desde la consola** la copia y reaplica la configuración anterior:

```bash
sudo cp /etc/netplan/NOMBRE.yaml.bak /etc/netplan/NOMBRE.yaml
sudo netplan apply
```

Revisa después la MAC, la interfaz, el servicio y la subred antes de repetir la prueba. No uses SSH para este cambio: podrías quedarte fuera del equipo.
:::

Cuando Ubuntu Server 1 haya recibido la reserva, comprueba en Ubuntu Server 2 que Kea la registró en su fichero de concesiones:

```bash
sudo grep -F '192.168.2.1' /var/lib/kea/kea-leases4.csv
```

La línea encontrada debe corresponder a la IP reservada `192.168.2.1` y a la MAC real configurada en `hw-address`. Si no aparece, confirma que Server 1 solicitó la dirección por DHCP y que Kea usa el backend `memfile` con ese nombre de fichero.

:::evidence{id="captura-reserva" type="screenshot" required="true"}
Captura de la reserva configurada y del archivo final de Kea.
:::

:::question{id="ip-reservada" type="short-text" required="true"}
¿Qué dirección debe quedar reservada para Ubuntu Server 1?
:::
