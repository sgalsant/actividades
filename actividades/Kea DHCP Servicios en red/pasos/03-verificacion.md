---
id: verificacion-servicio
titulo: Verificación del servicio y del cliente
duracion_minutos: 15
obligatorio: true
---

Comprueba que el servidor DHCP funciona y que el cliente recibe una dirección correcta.

:::task{id="verificar-servicio" required="true"}
En Ubuntu Server 2, comprueba que Kea permanece activo y revisa sus mensajes recientes. Si hay un error, corrige la configuración, vuelve a ejecutar `sudo -u _kea kea-dhcp4 -t /etc/kea/kea-dhcp4.conf` y reinicia solo cuando la prueba sea correcta.

```bash
systemctl status kea-dhcp4-server --no-pager
sudo journalctl -u kea-dhcp4-server -n 30 --no-pager
```
En Ubuntu Desktop 2, confirma que la interfaz de la red interna 3 está configurada para obtener IPv4 automáticamente y renueva su conexión desde la interfaz gráfica de red. Comprueba con `ip -br -4 address` que recibe una dirección entre `192.168.3.100` y `192.168.3.200`, no la antigua `192.168.3.2` estática. Un servicio activo no demuestra por sí solo que el cliente haya recibido una concesión. En Ubuntu Server 2, busca la IP obtenida en el fichero persistente de concesiones:

```bash
sudo grep -F 'IP_OBTENIDA' /var/lib/kea/kea-leases4.csv
```

Sustituye `IP_OBTENIDA` por la dirección que recibió Desktop 2. La línea encontrada debe corresponder a esa IP y al cliente probado.
:::

:::checkpoint{id="cliente-recibe-ip" required="true"}
El cliente de la red interna 3 obtiene una IP del rango esperado.
:::

:::question{id="puerto-dhcp" type="single-choice" required="true"}
¿En qué puerto escucha el servicio DHCP?

- [ ] TCP 67
- [x] UDP 67
- [ ] UDP 68
:::

:::evidence{id="captura-cliente-subred3" type="screenshot" required="true"}
Captura del cliente con la IP asignada por Kea.
:::
