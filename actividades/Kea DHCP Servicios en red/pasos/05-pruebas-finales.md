---
id: pruebas-finales
titulo: Pruebas de las redes internas 2 y 3
duracion_minutos: 20
obligatorio: true
---

Antes de incorporar el relay, las pruebas se centran en las dos redes conectadas directamente a Kea.

:::task{id="reiniciar-servicio" required="true"}
En Ubuntu Server 2, valida la configuración final y revisa el resultado. `systemctl status kea-dhcp4-server` permite consultar el estado; después de validar cambios de configuración, ejecuta `sudo systemctl restart kea-dhcp4-server` para que Kea los cargue. Si la validación falla, no reinicies: corrige el archivo primero. Ejecuta cada comando por separado. La tarea termina cuando el servicio está activo y el registro no muestra errores de configuración del último arranque.

```bash
sudo -u _kea kea-dhcp4 -t /etc/kea/kea-dhcp4.conf
```
Revisa la salida. Si la configuración es válida, reinicia el servicio y comprueba su estado y los registros recientes:

```bash
sudo systemctl restart kea-dhcp4-server
systemctl status kea-dhcp4-server --no-pager
sudo journalctl -u kea-dhcp4-server -n 30 --no-pager
```
:::

:::checkpoint{id="subredes-operativas" required="true"}
Las dos redes internas quedan atendidas por Kea según la configuración prevista.
:::

:::task{id="comprobar-server1" required="true"}
En Ubuntu Server 1, comprueba en el archivo de Netplan que la interfaz de la red interna 2 tiene `dhcp4: true` y no una dirección estática. Sustituye `INTERFAZ` por su nombre real: `ip` debe mostrar `192.168.2.1` y, si Netplan usa `systemd-networkd`, `networkctl status INTERFAZ` debe mostrar los datos DHCP de **esa** interfaz. La dirección correcta por sí sola no prueba la reserva si la interfaz siguiera configurada de forma estática. Si no aparece, revisa la MAC de esa interfaz frente a `hw-address` y los mensajes de Kea en Ubuntu Server 2.

```bash
ip -br -4 address
networkctl status INTERFAZ
```
:::

:::task{id="comprobar-desktop2" required="true"}
En Ubuntu Desktop 2, reconecta la interfaz de la red interna 3 desde la interfaz gráfica para solicitar una concesión nueva. Comprueba con `ip -br -4 address` que la dirección se mantiene dentro de `192.168.3.100 - 192.168.3.200`. Si conserva `192.168.3.2`, revisa que IPv4 esté configurado en automático y no en manual.

```bash
ip -br -4 address
```
En Ubuntu Server 2, confirma que la concesión de Desktop 2 está registrada en el CSV persistente de Kea:

```bash
sudo grep -F 'IP_OBTENIDA' /var/lib/kea/kea-leases4.csv
```

Sustituye `IP_OBTENIDA` por la dirección del pool `192.168.3.100–192.168.3.200` obtenida por el cliente y confirma que la línea corresponde a esa concesión.
:::

:::evidence{id="captura-pruebas-finales" type="screenshot" required="true"}
Captura de las pruebas de Ubuntu Server 1 y Ubuntu Desktop 2 con sus direcciones asignadas.
:::
