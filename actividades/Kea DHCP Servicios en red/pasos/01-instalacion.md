---
id: instalacion-kea
titulo: Instalación de Kea DHCP
duracion_minutos: 15
obligatorio: true
---

Instala Kea en **Ubuntu Server 2** y comprueba que el paquete queda disponible para la práctica.

:::task{id="instalar-kea" required="true"}
En Ubuntu Server 2, instala `kea-dhcp4-server` y comprueba que systemd reconoce el servicio. Un estado inicial inactivo o fallido no impide continuar: todavía no has adaptado la configuración a tu red.

```bash
sudo apt update
sudo apt install kea-dhcp4-server -y
systemctl status kea-dhcp4-server --no-pager
```
:::

:::note{}
Si el servicio no arranca todavía, no pasa nada: en este paso solo queremos dejarlo instalado y listo para configurar.
:::

:::evidence{id="captura-instalacion" type="screenshot" required="true"}
Captura donde se vea el paquete instalado o el estado inicial del servicio.
:::
