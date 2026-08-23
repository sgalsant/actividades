---
id: presentacion-red-interna
titulo: Presentación y escenario
duracion_minutos: 10
obligatorio: true
---

![Topología del reto 1](recursos/media/image1.png)

Empezamos con una configuración básica donde simulamos una intranet de una empresa conectada a Internet a través de un router Ubuntu Server.

En esta actividad configurarás dos máquinas virtuales: un Ubuntu Server que funcionará como un router y un Ubuntu Desktop que será una máquina de trabajo conectada a la intranet de la empresa.

Es importante habituarse al trabajo con máquinas virtuales y configuración de multiples redes ya que será nuestro escenario habitual de trabajo.

:::warning{}
Recuerda realizar copias de las máquinas virtuales al final de la jornada porque podría ocurrir que la máquina se corrompa y no pueda iniciarse o incluso pueda desaparecer del equipo ya que tu ordenador es usado por otros alumnos y alumnas.
:::

## Objetivos

- Configurar direcciones IP, gateway y DNS.
- Usar Ubuntu Server como encaminador IPv4.
- Aplicar NAT para que el cliente privado acceda a Internet.
- Diagnosticar conectividad local, externa y resolución DNS.


:::checkpoint{id="roles-topologia" required="true"}
Distingo los roles de la topología: la interfaz NAT del servidor sale a Internet, su interfaz de red interna conecta con Ubuntu Desktop y el servidor será el gateway del cliente.
:::
