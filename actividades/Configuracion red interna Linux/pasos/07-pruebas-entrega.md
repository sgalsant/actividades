---
id: pruebas-entrega
titulo: Verificar conectividad y recopilar evidencias
duracion_minutos: 25
obligatorio: true
---

Realiza las pruebas desde ambos equipos. Cada prueba verifica una capa distinta del escenario.

:::task{id="verificar-conectividad-final" required="true"}
Desde Ubuntu Desktop, ejecuta:

```bash
ping 192.168.1.1
ping 8.8.8.8
ping www.google.es
```

Desde Ubuntu Server, comprueba también:

```bash
ping 8.8.8.8
ping www.google.es
```
:::

:::note{}
Si `ping 8.8.8.8` funciona pero `ping www.google.es` falla, la conectividad y NAT están operativos; el problema está en la resolución DNS del cliente.
:::

:::task{id="reiniciar-y-comprobar" required="true"}
Reinicia ambas máquinas virtuales y repite las pruebas. La dirección interna, el reenvío y las reglas NAT deben seguir funcionando después del reinicio.
:::

:::evidence{id="captura-conectividad-internet" type="screenshot" required="true"}
Adjunta una captura de Ubuntu Desktop con conectividad al gateway, a `8.8.8.8` y a `www.google.es`.
:::

:::file{id="adjunto-netplan-final" accept=".yaml,.txt" required="true"}
Adjunta una copia de tu archivo final de Netplan, sin incluir datos personales o contraseñas.
:::
