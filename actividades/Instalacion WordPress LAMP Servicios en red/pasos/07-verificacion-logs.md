---
id: verificacion-logs-wordpress
titulo: Verificación final y logs
duracion_minutos: 45
obligatorio: true
---

## H. Verificación de logs

Los logs independientes permiten analizar este sitio sin mezclar sus accesos y errores con otros VirtualHost del servidor.

:::task{id="generar-y-revisar-logs" required="true"}
Visita la portada y `/wp-admin`, provoca una petición controlada a una URL inexistente y revisa los registros del sitio.

```bash
sudo tail -n 20 /var/log/apache2/wordpress_access.log
sudo tail -n 20 /var/log/apache2/wordpress_error.log
```

No generes errores destructivos ni expongas contraseñas para obtener la evidencia.
:::

:::task{id="checklist-tecnico-final" required="true"}
Confirma cada condición antes de preparar la entrega:

- El dominio resuelve y sirve WordPress por HTTPS.
- HTTP redirige a HTTPS.
- La base de datos usa un usuario limitado.
- `wp-admin` pide primero autenticación HTTP.
- Los archivos son de `www-data` y no tienen permisos globales de escritura.
- Los logs específicos contienen actividad.
- El tema distinto y la entrada publicada son visibles.
:::

:::evidence{id="captura-logs-wordpress" type="screenshot" required="true"}
Adjunta una captura de la terminal mostrando ambos archivos de log con actividad.
:::

:::question{id="incidencia-resuelta" type="long-text" required="true"}
Describe un problema real que hayas encontrado, qué comprobaste para diagnosticarlo y cómo lo resolviste. Si no hubo incidencias, explica qué verificación preventiva habría detectado una configuración incorrecta.
:::
