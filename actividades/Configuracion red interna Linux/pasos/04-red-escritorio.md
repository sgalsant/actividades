---
id: red-escritorio
titulo: Configura el cliente Ubuntu Desktop
duracion_minutos: 20
obligatorio: true
---

En la configuración de red de Ubuntu Desktop asigna estos valores a la conexión de red interna:

![Configuración de red estática en Ubuntu Desktop](recursos/media/image5.png)

| Parámetro | Valor |
|---|---|
| Dirección IP | `192.168.1.2/24` |
| Gateway | `192.168.1.1` |
| DNS | `8.8.8.8` |

:::task{id="configurar-cliente" required="true"}
Aplica la configuración y comprueba que el cliente alcanza al servidor:

```bash
ping 192.168.1.1
```
:::

:::evidence{id="captura-cliente-gateway" type="screenshot" required="true"}
Adjunta una captura del ping correcto al gateway.
:::
