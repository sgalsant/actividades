---
id: reflexion-entrega
titulo: Reflexión y entrega
duracion_minutos: 15
obligatorio: true
---

:::question{id="funcion-gateway" type="long-text" required="true"}
¿Qué función cumple Ubuntu Server en esta topología?
:::

:::question{id="definicion-iptables" type="long-text" required="true"}
¿Qué es `iptables`?
:::

:::question{id="funcion-nat" type="long-text" required="true"}
¿Por qué es necesario NAT y cómo funciona la regla `MASQUERADE`?
:::

:::reflection{id="reflexion-final" required="true"}
Indica los problemas que encontraste, cómo los diagnosticastes y qué comprobarías primero en una topología similar.
:::

:::file{id="pdf-configuracion-red" accept=".pdf" required="true"}
Adjunta un único PDF con la configuración completa de red de los dos servidores. Debe incluir, para Servidor 1 y Servidor 2, los nombres de interfaz, direcciones IP y prefijos, gateway o rutas estáticas y DNS cuando corresponda. Copia también el contenido completo de los ficheros Netplan de ambos servidores (`/etc/netplan/*.yaml`).
:::

Exporta tu trabajo como archivo `.aulawork` antes de entregarlo.
