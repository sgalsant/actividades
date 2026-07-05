---
id: reto-2-firewall
titulo: Reto 2 - Configuración del firewall (UFW)
duracion_minutos: 15
obligatorio: true
---

Un firewall es un sistema que controla el tráfico de red entrante y saliente según reglas de seguridad. UFW (Uncomplicated Firewall) permite gestionar el firewall de Ubuntu de forma sencilla.

:::note{}
**Principio de mínimo privilegio:** por defecto cerraremos todos los puertos y solo abriremos los necesarios (SSH, HTTP y HTTPS). Esto reduce la superficie de ataque del servidor.
:::

:::warning{}
Permite SSH **antes** de activar UFW. Si no, perderás el acceso remoto.
:::

:::task{id="permitir-ssh" required="true"}
Permite el tráfico SSH.
:::

```bash
sudo ufw allow 22/tcp
```

:::task{id="permitir-web" required="true"}
Permite el tráfico web.
:::

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

:::task{id="activar-ufw" required="true"}
Activa el firewall y verifica las reglas.
:::

```bash
sudo ufw enable
sudo ufw status verbose
```

:::question{id="principio-minimo-privilegio" type="short-text" required="true"}
Explica con tus palabras qué significa aplicar el principio de mínimo privilegio en un firewall.
:::

:::evidence{id="captura-ufw" type="screenshot" required="true"}
Captura de `sudo ufw status verbose` mostrando las reglas configuradas.
:::
