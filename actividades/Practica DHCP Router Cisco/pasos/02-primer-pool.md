---
id: primer-pool
titulo: Crear el primer pool DHCP
duracion_minutos: 20
obligatorio: true
---

Configura el pool que entregará direcciones a la red `172.16.0.0/16`.

```text
ip dhcp pool DHCP_APELLIDO
 network 172.16.0.0 255.255.0.0
 default-router 172.16.0.1
exit
```

En cada PC selecciona **Desktop > IP Configuration > DHCP**. No asignes direcciones manuales.

:::task{id="crear-pool-primero" required="true"}
Crea el pool `DHCP_APELLIDO` y configura PC1, PC2 y PC3 para que obtengan la IP automáticamente.
:::

En PC1 ejecuta:

```text
ipconfig /all
```

:::question{id="gateway-primera-lan" type="short-text" required="true"}
¿Qué puerta de enlace recibió PC1?
:::

:::evidence{id="ipconfig-pc1" type="screenshot" required="true"}
Captura de `ipconfig /all` de PC1 donde se vea su dirección y puerta de enlace.
:::
