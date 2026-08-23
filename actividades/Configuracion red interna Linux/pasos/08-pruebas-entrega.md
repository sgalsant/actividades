---
id: pruebas-reto-uno
titulo: Comprueba la conectividad del reto 1
duracion_minutos: 25
obligatorio: true
---

Ejecuta las pruebas desde Ubuntu Desktop y distingue los fallos de red de los de DNS:

```bash
ping 192.168.1.1
ping 8.8.8.8
ping www.google.es
```

Después, desde Ubuntu Server confirma también el acceso a Internet:

```bash
ping 8.8.8.8
ping www.google.es
```

:::note{}
Si responde `8.8.8.8` pero no el nombre de dominio, NAT funciona y debes revisar DNS. Si no responde ninguna dirección externa, revisa gateway, reenvío IPv4 y la regla `MASQUERADE`.
:::

:::evidence{id="captura-conectividad" type="screenshot" required="true"}
Adjunta una captura con las tres comprobaciones realizadas desde el cliente.
:::

:::task{id="verificar-reinicio-reto-uno" required="true"}
Reinicia Ubuntu Desktop y Ubuntu Server. Después del reinicio, repite desde Desktop `ping 192.168.1.1`, `ping 8.8.8.8` y `ping www.google.es`; desde Server repite `ping 8.8.8.8` y `ping www.google.es`.
:::

:::evidence{id="captura-post-reinicio" type="screenshot" required="true"}
Adjunta una captura posterior al reinicio que muestre una prueba de dirección IP externa y otra de resolución DNS.
:::
