---
id: reflexion-final
titulo: Reflexión y entrega final
duracion_minutos: 10
obligatorio: true
---

:::question{id="quiz-broadcast-relay" type="single-choice" required="true"}
¿Por qué hace falta un relay DHCP para atender una red situada detrás de Ubuntu Server 1?

- [ ] Porque los routers reenvían automáticamente los broadcast DHCP a todas las redes conectadas.
- [x] Porque el broadcast inicial del cliente no cruza el router; el relay lo recibe en la red local y lo reenvía al servidor Kea.
- [ ] Porque Kea solo puede conceder direcciones si está instalado también en el cliente.
:::

:::question{id="quiz-roles-giaddr" type="single-choice" required="true"}
¿Qué afirmación describe correctamente el trabajo de Kea y del relay?

- [x] El relay transporta las solicitudes y respuestas; Kea asigna la dirección y usa `giaddr` para identificar la subred correspondiente.
- [ ] El relay asigna la dirección del pool y Kea solo registra la concesión; `giaddr` identifica al relay para la puerta de enlace.
- [ ] Kea reenvía el broadcast entre redes y el relay decide qué subred y pool debe utilizarse.
:::

:::question{id="quiz-ids-subred" type="single-choice" required="true"}
¿Cómo deben configurarse los valores `id` de los objetos `subnet4`?

- [ ] Se pueden repetir entre subredes si cada una tiene un prefijo de red distinto.
- [x] Deben ser únicos en la configuración; conviene conservarlos al ampliarla para que cada subred mantenga una identidad estable.
- [ ] Deben coincidir con el último octeto de la puerta de enlace de cada subred.
:::

:::question{id="quiz-validacion-kea" type="single-choice" required="true"}
¿Cuál es la secuencia adecuada antes de reiniciar Kea tras editar su configuración?

- [ ] Reiniciar el servicio y después ejecutar la validación como `root`.
- [x] Validar `/etc/kea/kea-dhcp4.conf` como usuario `_kea` y reiniciar solo si la validación no informa errores.
- [ ] Reiniciar primero el relay y luego editar la configuración de Kea sin validarla.
:::

:::question{id="quiz-registro-concesion" type="single-choice" required="true"}
¿Cómo puedes comprobar que Kea registró la concesión asignada a un cliente?

- [ ] Buscar la dirección asignada en `/etc/kea/kea-dhcp4.conf`.
- [ ] Consultar únicamente el estado `active` de `kea-dhcp4-server`.
- [x] Buscar la IP obtenida o la MAC del cliente en `/var/lib/kea/kea-leases4.csv`.
:::

:::question{id="quiz-tipos-direccion-ip" type="single-choice" required="true"}
Relaciona cada definición con el tipo de dirección usado en esta actividad:

1. Configurada manualmente en el propio cliente.
2. Reservada por Kea para la MAC de un cliente concreto.
3. Elegida por Kea de un pool y concedida mediante DHCP.

- [ ] 1. IP fija; 2. IP dinámica; 3. IP estática.
- [x] 1. IP estática; 2. IP fija; 3. IP dinámica.
- [ ] 1. IP dinámica; 2. IP estática; 3. IP fija.
:::

:::reflection{id="reflexion-final" required="true"}
¿Qué parte te resultó más delicada: la configuración inicial, la reserva por MAC o el relay para la red interna 1? Si Ubuntu Desktop 1 no recibiera una dirección, ¿qué comprobarías primero en el cliente, en el relay y en Kea?
:::

:::question{id="valoracion-actividad" type="numeric" required="false"}
¿Qué te ha parecido la actividad? Valórala en conjunto teniendo en cuenta su claridad, interés y utilidad. Las estrellas son solo visuales: escribe únicamente el número entero que corresponda.

- **1** · ⭐☆☆☆☆ · Muy mala
- **2** · ⭐⭐☆☆☆ · Floja
- **3** · ⭐⭐⭐☆☆ · Aceptable
- **4** · ⭐⭐⭐⭐☆ · Buena
- **5** · ⭐⭐⭐⭐⭐ · Excelente
:::

:::question{id="comentario-actividad" type="long-text" required="false"}
¿Qué parte te resultó más útil y qué mejorarías de la actividad?
:::

:::task{id="exportar-aulawork" required="true"}
Revisa que has completado las respuestas y adjuntado las capturas pedidas. Después exporta el trabajo en formato `.aulawork` y comprueba que el archivo se ha descargado con el nombre esperado antes de cerrar la actividad.
:::
