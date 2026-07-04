---
id: pruebas-finales
titulo: Pruebas finales del escenario
duracion_minutos: 20
obligatorio: true
---

Ahora toca demostrar que todo funciona junto.

:::task{id="reiniciar-servicio" required="true"}
Reinicia Kea y comprueba que no quedan errores pendientes.
:::

```bash
sudo systemctl restart kea-dhcp4-server
sudo systemctl status kea-dhcp4-server
```

:::checkpoint{id="subredes-operativas" required="true"}
Las dos redes internas quedan atendidas por Kea según la configuración prevista.
:::

:::task{id="comprobar-server1" required="true"}
Verifica que Ubuntu Server 1 recibe la reserva esperada en la red interna 2.
:::

:::task{id="comprobar-desktop2" required="true"}
Verifica que Ubuntu Desktop 2 sigue recibiendo una IP de la red interna 3.
:::

:::evidence{id="captura-pruebas-finales" type="screenshot" required="true"}
Captura de las pruebas finales con los dos clientes funcionando.
:::
