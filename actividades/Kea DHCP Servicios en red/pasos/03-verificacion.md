---
id: verificacion-servicio
titulo: Verificación del servicio y del cliente
duracion_minutos: 15
obligatorio: true
---

Comprueba que el servidor DHCP funciona y que el cliente recibe una dirección correcta.

:::task{id="verificar-servicio" required="true"}
Revisa el estado del servicio y los logs si aparece algún fallo.
:::

```bash
sudo systemctl status kea-dhcp4-server
tail /var/log/syslog -n 20
```

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
