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

En VirtualBox añade al primer servidor un tercer adaptador en modo **Red interna** con nombre `red-interna-2`. Crea el segundo Ubuntu Server con dos adaptadores, ambos en modo **Red interna**: `red-interna-2` y `red-interna-3`.

:::task{id="configurar-segundo-router" required="true"}
Comprueba primero los nombres reales con `ip a`. En el primer servidor añade `enp0s9` para `192.168.2.1/24` y la ruta hacia `192.168.3.0/24` a través de `192.168.2.2`:

```yaml
enp0s9:
  addresses:
    - 192.168.2.1/24
  routes:
    - to: 192.168.3.0/24
      via: 192.168.2.2
```

En el segundo servidor habilita `ip_forward` y configura `enp0s3` y `enp0s8`:

```yaml
enp0s3:
  addresses:
    - 192.168.2.2/24
  nameservers:
    addresses: [8.8.8.8]
  routes:
    - to: default
      via: 192.168.2.1
enp0s8:
  addresses:
    - 192.168.3.1/24
```
:::

:::task{id="probar-tres-subredes" required="true"}
Desde Desktop 2 prueba conectividad con el segundo servidor, el primer servidor y `8.8.8.8`. Reinicia las máquinas y repite la verificación.
:::
