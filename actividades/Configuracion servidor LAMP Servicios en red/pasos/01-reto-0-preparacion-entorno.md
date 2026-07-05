---
id: reto-0-preparacion-entorno
titulo: Reto 0 - Preparación del entorno virtual
duracion_minutos: 30
obligatorio: true
---

## Port forwarding

Cuando una VM usa NAT, el anfitrión puede acceder a ella mediante reenvío de puertos. Es como indicarle a un recepcionista que las llamadas a una extensión concreta deben pasar a una oficina interior.

:::note{}
**Ejemplo práctico:** cuando escribes `http://localhost:8080` en el navegador del anfitrión, VirtualBox redirige la petición al puerto 80 del servidor virtual. El servidor Apache responde y VirtualBox devuelve la página a tu navegador.
:::

:::task{id="importar-vm" required="true"}
Importa la OVA `ubuntu server-24.ova` en VirtualBox y renombra la VM a `LAMP_[tu_nombre]`.
:::

:::task{id="configurar-puertos" required="true"}
Configura estas reglas de reenvío de puertos en el Adaptador 1 (NAT).

En la configuración de red de la VM, con el Adaptador 1 en NAT, abre las opciones avanzadas y pulsa **Reenvío de puertos**:

![Configuración de red NAT y botón Reenvío de puertos](recursos/media/image2.png)

Añade las siguientes reglas:

| Nombre | Protocolo | IP anfitrión | Puerto anfitrión | Puerto invitado |
|---|---|---|---|---|
| SSH | TCP | 127.0.0.1 | 2222 | 22 |
| HTTP | TCP | 127.0.0.1 | 8080 | 80 |
| HTTPS | TCP | 127.0.0.1 | 8443 | 443 |

![Reglas de reenvío de puertos configuradas](recursos/media/image3.png)
:::

:::task{id="arrancar-vm" required="true"}
Arranca la VM, inicia sesión con usuario `analuisa` y contraseña `analuisa`.
:::

## Instalación de OpenSSH Server

:::note{}
**SSH** (Secure Shell) es un protocolo que permite acceder de forma segura a la terminal de un servidor remoto. Te permitirá trabajar cómodamente desde tu sistema operativo anfitrión y transferir archivos.
:::

:::task{id="instalar-ssh" required="true"}
Instala OpenSSH Server, habilítalo y verifica que está activo y habilitado al arranque.
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
Desde PowerShell en el anfitrión conéctate por SSH:
:::

```powershell
ssh analuisa@localhost -p 2222
```

Si la conexión es correcta, verás el prompt de tu servidor listo para recibir comandos:

![Conexión SSH exitosa desde PowerShell](recursos/media/image5.png)

:::tip{}
Trabajar por SSH desde el anfitrión te permite:

- Copiar y pegar comandos fácilmente.
- Mantener varias ventanas abiertas.
- Trabajar cómodamente desde tu escritorio habitual.
- Transferir archivos con SFTP/SCP.
:::

:::question{id="ventaja-ssh" type="short-text" required="true"}
Indica dos ventajas de trabajar por SSH frente a la consola de VirtualBox.
:::
