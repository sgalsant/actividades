---
id: base-datos-wordpress
titulo: Base de datos con mínimo privilegio
duracion_minutos: 60
obligatorio: true
---

## B. Configuración de base de datos

WordPress necesita una base de datos propia y un usuario que solo pueda operar sobre ella. El usuario de la aplicación no debe ser `root` ni tener privilegios globales.

:::task{id="crear-bd-y-usuario" required="true"}
Accede a MariaDB/MySQL como administrador y adapta los marcadores por nombres y una contraseña robusta que hayas elegido. Conserva los comandos realmente ejecutados para tu documento final.

```sql
CREATE DATABASE wordpress_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'wordpress_user'@'localhost' IDENTIFIED BY 'cambia-esta-contrasena';
GRANT SELECT, INSERT, UPDATE, DELETE ON wordpress_db.* TO 'wordpress_user'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'wordpress_user'@'localhost';
```

Puedes crear la base de datos antes de conceder privilegios; no concedas `ALL PRIVILEGES`, `DROP` ni permisos sobre otras bases de datos salvo que hayas justificado una necesidad real.
:::

:::task{id="verificar-usuario-bd" required="true"}
Comprueba que el usuario puede conectarse a su base de datos y que sus permisos están restringidos a ella.

```bash
mysql -u wordpress_user -p wordpress_db
```
:::

:::evidence{id="captura-bd-usuario" type="screenshot" required="true"}
Adjunta una captura de MariaDB/MySQL mostrando la base de datos, el usuario y sus privilegios. No muestres la contraseña.
:::

:::question{id="principio-minimo-privilegio" type="long-text" required="true"}
Explica por qué no debes configurar WordPress con el usuario root de MariaDB/MySQL.
:::
