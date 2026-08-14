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

:::checkpoint{id="reinicio-reto-uno" required="true"}
He reiniciado las máquinas y he comprobado que Ubuntu Desktop y Ubuntu Server conservan conectividad entre sí y acceso a Internet.
:::
