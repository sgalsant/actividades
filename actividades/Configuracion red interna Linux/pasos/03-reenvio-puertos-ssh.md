---
id: reenvio-puertos-ssh
titulo: Configura el acceso SSH desde Windows
duracion_minutos: 20
obligatorio: true
---

SSH (Secure Shell) es un protocolo que permite abrir una terminal remota de forma cifrada. En las actividades, podrás administrar el servidor Linux desde Windows sin usar directamente la consola de VirtualBox.

El adaptador NAT del servidor permite que la máquina virtual salga a Internet, pero el sistema operativo anfitrión Windows no puede iniciar conexiones hacia ella directamente. Para esto vamos a usar el reenvío de puertos que nos ofrece Virtualbox.

Configura una regla de reenvío de puertos en la máquina virtual del servidor para que VirtualBox dirija las conexiones SSH desde Windows al servidor Linux. De esta forma, podrás acceder desde la terminal de Windows al servidor y te resultará más cómodo trabajar con dicha máquina además de que esta es la forma real con la que se suele trabajar con los servidores en remoto.

:::task{id="configurar-reenvio-ssh" required="true"}
Con la máquina virtual del servidor apagada, abre **Configuración → Red → Adaptador 1 (NAT) → Avanzadas → Reenvío de puertos** y añade esta regla:

| Nombre | Protocolo | IP anfitrión | Puerto anfitrión | Puerto invitado |
|---|---|---|---:|---:|
| SSH | TCP | 127.0.0.1 | 2222 | 22 |

La dirección `127.0.0.1` limita el acceso al propio equipo anfitrión. El puerto `2222` evita interferir con un posible servidor SSH instalado en Windows.
:::

:::task{id="instalar-ssh" required="true"}
Inicia el servidor desde VirtualBox e instala OpenSSH Server. Habilítalo para que arranque automáticamente y comprueba que está activo:

```bash
sudo apt update
sudo apt install -y openssh-server
sudo systemctl enable --now ssh
sudo systemctl status ssh
```

El estado debe indicar `active (running)`.
:::

:::task{id="probar-ssh-windows" required="true"}
Desde PowerShell en Windows, conecta con el usuario de tu servidor:

```powershell
ssh TU_USUARIO@localhost -p 2222
```

Sustituye `TU_USUARIO` por el nombre del usuario empleado en el servidor. Si has clonado la máquina base proporcionada para la actividad, el usuario y contraseña son `analuisa`. Si es la primera conexión, confirma la huella SSH escribiendo `yes`. 
:::

:::warning{}
Si en el momento de conectar con ssh al servidor se indica que ya se encuentra registrada una clave identificativa para ese servidor "remote host identification has changed, elimina dicha huella, ejecutando en la máquina anfitriona Windows: 

```powershell
ssh-keygen -R "[localhost]:2222"
```
:::

:::evidence{id="captura-ssh-windows" type="screenshot" required="true"}
Adjunta una captura de PowerShell que muestre una sesión SSH conectada al servidor Linux mediante el puerto `2222`.
:::
