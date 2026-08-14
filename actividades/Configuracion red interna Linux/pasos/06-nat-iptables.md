---
id: nat-iptables
titulo: Configura NAT con iptables
duracion_minutos: 30
obligatorio: true
---

La red `192.168.1.0/24` usa direcciones privadas. NAT con `MASQUERADE` sustituye la dirección de origen del cliente por la de la interfaz externa del servidor.

:::task{id="configurar-nat" required="true"}
Sustituye `enp0s3` si tu interfaz de salida tiene otro nombre y añade la regla NAT:

```bash
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
sudo apt install iptables-persistent
sudo netfilter-persistent save
sudo iptables-save
```
:::

:::warning{}
Activar `ip_forward` sin una regla NAT no basta: el cliente reenviará paquetes, pero las redes externas no sabrán cómo devolver tráfico a su dirección privada.
:::
