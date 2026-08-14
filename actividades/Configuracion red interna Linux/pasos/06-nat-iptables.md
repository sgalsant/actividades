---
id: nat-iptables
titulo: Configura NAT con iptables
duracion_minutos: 30
obligatorio: true
---

La red `192.168.1.0/24` usa direcciones privadas. NAT con `MASQUERADE` sustituye la dirección de origen del cliente por la de la interfaz externa del servidor.

:::task{id="configurar-nat" required="true"}
1. Sustituye `enp0s3` si tu interfaz de salida tiene otro nombre y añade la regla NAT:

```bash
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
```

2. Desde Ubuntu Desktop, confirma que el cliente ya puede acceder a Internet:

```bash
ping 8.8.8.8
```
:::

![Instalación de iptables-persistent](recursos/media/image6.png)

:::task{id="persistir-reglas-iptables" required="true"}
1. Instala `iptables-persistent` para conservar las reglas después de reiniciar:

```bash
sudo apt install iptables-persistent
```

2. Guarda la configuración actual y consulta las reglas almacenadas:

```bash
sudo netfilter-persistent save
sudo iptables-save
```
:::

Las reglas persistentes se guardan en `/etc/iptables/rules.v4`. Si las modificas después de instalar `iptables-persistent`, vuelve a ejecutar `sudo netfilter-persistent save` para no perderlas al reiniciar.

Para borrar las reglas actuales antes de volver a probar una configuración, usa:

```bash
sudo iptables -F
sudo iptables -t nat -F
```

:::warning{}
Activar `ip_forward` sin una regla NAT no basta: el cliente reenviará paquetes, pero las redes externas no sabrán cómo devolver tráfico a su dirección privada.
:::
