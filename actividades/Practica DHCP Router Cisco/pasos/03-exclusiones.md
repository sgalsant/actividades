---
id: exclusiones
titulo: Reservar direcciones y comprobar concesiones
duracion_minutos: 15
obligatorio: true
---

DHCP no debe asignar direcciones reservadas para infraestructura u otros usos estáticos. Declara ambas exclusiones por separado:

```text
ip dhcp excluded-address 172.16.0.1 172.16.0.10
ip dhcp excluded-address 172.16.0.13 172.16.0.20
```

Después, en los PCs renueva la configuración:

```text
ipconfig /renew
```

:::task{id="excluir-rangos" required="true"}
Excluye los rangos `.1-.10` y `.13-.20`, renueva las direcciones de los clientes y comprueba que ninguno usa esos intervalos.
:::

En el router consulta las concesiones:

```text
show ip dhcp binding
```

:::evidence{id="concesiones-primera-lan" type="screenshot" required="true"}
Captura de `show ip dhcp binding` donde se vean las MAC y direcciones entregadas.
:::
