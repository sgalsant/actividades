---
id: reto-0-preparacion-entorno
titulo: Reto 0 - Preparacion del entorno virtual
duracion_minutos: 30
obligatorio: true
---

## Port forwarding

Cuando una VM usa NAT, el anfitrion puede acceder a ella mediante reenvio de puertos. Es como indicarle a un recepcionista que las llamadas a una extension concreta deben pasar a una oficina interior.

:::task{id="importar-vm" required="true"}
Importa la OVA `ubuntu server-24.ova` en VirtualBox y renombra la VM a `LAMP_[tu_nombre]`.
:::

:::task{id="configurar-puertos" required="true"}
Configura estas reglas de reenvio de puertos en el Adaptador 1 (NAT).

En la configuracion de red de la VM, con el Adaptador 1 en NAT, abre las opciones avanzadas y pulsa **Reenvio de puertos**:

![Configuracion de red NAT y boton Reenvio de puertos](recursos/media/image2.png)

Añade las siguientes reglas:

| Nombre | Protocolo | IP anfitrion | Puerto anfitrion | Puerto invitado |
|---|---|---|---|---|
| SSH | TCP | 127.0.0.1 | 2222 | 22 |
| HTTP | TCP | 127.0.0.1 | 8080 | 80 |
| HTTPS | TCP | 127.0.0.1 | 8443 | 443 |

![Reglas de reenvio de puertos configuradas](recursos/media/image3.png)
:::

:::task{id="arrancar-vm" required="true"}
Arranca la VM, inicia sesion con usuario `analuisa` y contrasena `analuisa`.
:::

## Instalacion de OpenSSH Server

:::task{id="instalar-ssh" required="true"}
Instala OpenSSH Server, habilitalo y verifica que esta activo y habilitado al arranque.
:::

```bash
sudo apt update
sudo apt install -y openssh-server
sudo systemctl enable --now ssh
sudo systemctl status ssh
sudo systemctl is-enabled ssh
```

La salida de `sudo systemctl status ssh` debe mostrar el servicio **active (running)** y **enabled**:

![Estado del servicio SSH activo y habilitado](recursos/media/image4.png)

:::task{id="probar-ssh" required="true"}
Desde PowerShell en el anfitrion conectate por SSH:
:::

```powershell
ssh analuisa@localhost -p 2222
```

Si la conexion es correcta, veras el prompt de tu servidor listo para recibir comandos:

![Conexion SSH exitosa desde PowerShell](recursos/media/image5.png)

:::question{id="ventaja-ssh" type="short-text" required="true"}
Indica dos ventajas de trabajar por SSH frente a la consola de VirtualBox.
:::
