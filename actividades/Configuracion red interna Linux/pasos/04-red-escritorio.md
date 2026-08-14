---
id: red-escritorio
titulo: Configurar Ubuntu Desktop
duracion_minutos: 15
obligatorio: true
---

Configura la interfaz de red de Ubuntu Desktop desde la interfaz gráfica de red con estos valores:

| Campo | Valor |
|---|---|
| Dirección IP | `192.168.1.2` |
| Máscara o prefijo | `255.255.255.0` o `/24` |
| Gateway | `192.168.1.1` |
| DNS | `8.8.8.8` |

:::task{id="configurar-cliente-estatico" required="true"}
Guarda la configuración y verifica desde Ubuntu Desktop que puedes alcanzar al servidor:

```bash
ping 192.168.1.1
```
:::

:::warning{}
No continúes hasta que este ping funcione. El NAT no resolverá un error previo de direccionamiento, máscara o red interna de VirtualBox.
:::

:::evidence{id="captura-ping-gateway" type="screenshot" required="true"}
Adjunta una captura del ping exitoso desde Ubuntu Desktop a `192.168.1.1`.
:::
