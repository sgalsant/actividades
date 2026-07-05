---
id: reto-9-gestion-bd
titulo: Reto 9 - Gestión básica de bases de datos
duracion_minutos: 35
obligatorio: true
---

Aplicarás el principio de mínimo privilegio creando un usuario administrador con control total sobre tu base de datos y un usuario operador con permisos CRUD.

:::warning{}
Sustituye `bd_ejemplo` por el nombre único que elijas para tu base de datos, por ejemplo `bd_[tu_nombre]`.
:::

:::task{id="crear-bd" required="true"}
Conéctate a MariaDB como root y crea tu base de datos.
:::

```bash
sudo mysql -u root -p
```

```sql
-- Sustituye 'bd_ejemplo' por el nombre que hayas elegido para tu base de datos.
CREATE DATABASE bd_ejemplo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

:::task{id="crear-admin-bd" required="true"}
Crea el usuario administrador y otórgale todos los permisos sobre tu base de datos.
:::

```sql
-- Sustituye 'bd_ejemplo' por el nombre de tu base de datos.
CREATE USER 'admin_bd_ejemplo'@'localhost' IDENTIFIED BY 'PassAdmin123!';
GRANT ALL PRIVILEGES ON bd_ejemplo.* TO 'admin_bd_ejemplo'@'localhost';
```

:::task{id="crear-operador-bd" required="true"}
Crea el usuario operador con permisos limitados.
:::

```sql
-- Sustituye 'bd_ejemplo' por el nombre de tu base de datos.
CREATE USER 'operador_bd_ejemplo'@'localhost' IDENTIFIED BY 'PassOper456!';
GRANT SELECT, INSERT, UPDATE, DELETE ON bd_ejemplo.* TO 'operador_bd_ejemplo'@'localhost';
```

:::task{id="aplicar-permisos" required="true"}
Aplica los cambios, verifica los usuarios creados y sal.
:::

```sql
-- Sustituye 'bd_ejemplo' por el nombre de tu base de datos.
FLUSH PRIVILEGES;
SELECT user, host FROM mysql.user WHERE user LIKE '%bd_ejemplo%';
EXIT;
```

:::task{id="probar-admin-phpmyadmin" required="true"}
En phpMyAdmin, conéctate como `admin_bd_ejemplo` y crea una tabla `clientes` con columnas `id` (INT, AUTO_INCREMENT, Primary) y `nombre` (VARCHAR(100)).
:::

:::task{id="probar-operador-phpmyadmin" required="true"}
Cierra la sesión del administrador, conéctate como `operador_bd_ejemplo` e inserta dos registros en la tabla `clientes`.
:::

:::evidence{id="captura-usuarios-bd" type="screenshot" required="true"}
Captura del resultado de la consulta mostrando los dos usuarios creados.
:::

:::evidence{id="captura-tabla-clientes" type="screenshot" required="true"}
Captura de phpMyAdmin mostrando la tabla `clientes` con los dos registros insertados por el operador.
:::
