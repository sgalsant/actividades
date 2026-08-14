---
id: nat-iptables
titulo: Configurar NAT y persistencia
duracion_minutos: 30
obligatorio: true
---

Los equipos de la red interna usan direcciones privadas. NAT modifica la dirección de salida para que sus paquetes puedan circular por Internet usando la dirección de la interfaz NAT del servidor.

:::task{id="activar-masquerade" required="true"}
En Ubuntu Server, añade una regla `MASQUERADE` sobre la interfaz que sale a Internet. En el escenario de referencia es `enp0s3`:

```bash
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
```

Comprueba desde Ubuntu Desktop que ya existe acceso a una IP externa:

```bash
ping 8.8.8.8
```
:::

:::task{id="persistir-iptables" required="true"}
Instala el mecanismo de persistencia y guarda las reglas:

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

Consulta las reglas guardadas cuando necesites verificarlas:

```bash
sudo iptables-save
```
:::

:::warning{}
`sudo iptables -F` borra las reglas de filtrado y `sudo iptables -t nat -F` borra las reglas NAT. Úsalos solo si sabes qué vas a reconstruir después.
:::

:::question{id="funcion-nat" type="long-text" required="true"}
¿Por qué se necesita NAT en esta topología y cómo permite que el cliente use Internet?
:::
