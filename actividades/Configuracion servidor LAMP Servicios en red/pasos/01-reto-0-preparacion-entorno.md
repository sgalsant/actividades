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
Configura estas reglas de reenvio de puertos en el Adaptador 1 (NAT):

| Nombre | Protocolo | IP anfitrion | Puerto anfitrion | Puerto invitado |
|---|---|---|---|---|
| SSH | TCP | 127.0.0.1 | 2222 | 22 |
| HTTP | TCP | 127.0.0.1 | 8080 | 80 |
| HTTPS | TCP | 127.0.0.1 | 8443 | 443 |
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

:::task{id="probar-ssh" required="true"}
Desde PowerShell en el anfitrion conectate por SSH:
:::

```powershell
ssh analuisa@localhost -p 2222
```

:::question{id="ventaja-ssh" type="short-text" required="true"}
Indica dos ventajas de trabajar por SSH frente a la consola de VirtualBox.
:::
