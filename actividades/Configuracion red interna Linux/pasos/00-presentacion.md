---
id: presentacion-red-interna
titulo: Presentación y escenario
duracion_minutos: 10
obligatorio: true
---

![Topología del reto 1](recursos/media/image1.png)

Empezamosxxx con una configuración básica donde tendremos la intranet de la empresa conectada a Internet a través de un router.

Configurarás dos máquinas virtuales: un Ubuntu Server con una interfaz NAT y otra de red interna que funcionará como un router y un Ubuntu Desktop que será una máquina de trabajo conectado la intranet de la empresa.

## Objetivos

- Configurar direcciones IP, gateway y DNS.
- Usar Ubuntu Server como encaminador IPv4.
- Aplicar NAT para que el cliente privado acceda a Internet.
- Diagnosticar conectividad local, externa y resolución DNS.

:::note{}
El reenvío IPv4 mueve paquetes entre interfaces. NAT traduce las direcciones privadas del cliente para que puedan salir por la interfaz pública del servidor. Necesitas ambas cosas para dar acceso a Internet.
:::

:::checkpoint{id="roles-topologia" required="true"}
Distingo los roles de la topología: la interfaz NAT del servidor sale a Internet, su interfaz de red interna conecta con Ubuntu Desktop y el servidor será el gateway del cliente.
:::
