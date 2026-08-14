---
id: subredes-enrutamiento
titulo: Amplía la red con un segundo router
duracion_minutos: 55
obligatorio: true
---

En el reto 2 añadirás una segunda red `192.168.2.0/24`, un segundo Ubuntu Server y una tercera red `192.168.3.0/24`.

![Topología del reto 2](recursos/media/image7.png)

| Equipo | Interfaces relevantes |
|---|---|
| Servidor 1 | `192.168.1.1/24`, `192.168.2.1/24` y ruta a `192.168.3.0/24` vía `192.168.2.2` |
| Servidor 2 | `192.168.2.2/24`, `192.168.3.1/24` y ruta por defecto vía `192.168.2.1` |
| Desktop 2 | `192.168.3.2/24`, gateway `192.168.3.1`, DNS `8.8.8.8` |

:::task{id="configurar-segundo-router" required="true"}
Añade en el primer servidor una interfaz para `192.168.2.1/24` y la ruta hacia `192.168.3.0/24` a través de `192.168.2.2`. En el segundo servidor habilita `ip_forward`, configura ambas interfaces y su ruta por defecto.
:::

:::task{id="probar-tres-subredes" required="true"}
Desde Desktop 2 prueba conectividad con el segundo servidor, el primer servidor y `8.8.8.8`. Reinicia las máquinas y repite la verificación.
:::
