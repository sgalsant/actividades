---
id: reto-9-gestion-bd
titulo: Reto 9 - Gestión básica de bases de datos
duracion_minutos: 35
obligatorio: true
---

Aplicarás el principio de mínimo privilegio creando un usuario administrador con control total sobre tu base de datos y un usuario operador con permisos CRUD.

:::note{}
En seguridad informática, cada usuario debe tener únicamente los permisos necesarios para realizar su trabajo. A esto se le llama **principio de mínimo privilegio**.
:::

:::warning{}
Elige un sufijo único para tu base de datos (por ejemplo, tu `apellido_nombre`) y úsalo de forma consistente en los tres identificadores:

| Elemento | Ejemplo |
|---|---|
| Base de datos | `bd_apellido_nombre` |
| Usuario administrador | `admin_bd_apellido_nombre` |
| Usuario operador | `operador_bd_apellido_nombre` |

En los comandos siguientes, sustituye `apellido_nombre` por el sufijo que hayas elegido.
:::

:::task{id="crear-bd" required="true"}
Conéctate a MariaDB como root y crea tu base de datos.

```bash
sudo mysql -u root -p
```

```sql
-- Sustituye 'apellido_nombre' por tu sufijo.
CREATE DATABASE bd_apellido_nombre CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
:::

:::note{}
- `CHARACTER SET utf8mb4`: soporte completo de UTF-8, incluidos emojis.
- `COLLATE utf8mb4_unicode_ci`: reglas de comparación insensibles a mayúsculas/minúsculas.
:::

:::task{id="crear-admin-bd" required="true"}
Crea el usuario administrador y otórgale todos los permisos sobre tu base de datos.

```sql
-- Sustituye 'apellido_nombre' por tu sufijo.
CREATE USER 'admin_bd_apellido_nombre'@'localhost' IDENTIFIED BY 'PassAdmin123!';
GRANT ALL PRIVILEGES ON bd_apellido_nombre.* TO 'admin_bd_apellido_nombre'@'localhost';
```
:::

:::note{}
- `ALL PRIVILEGES`: todos los permisos (`CREATE`, `DROP`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc.).
- `bd_apellido_nombre.*`: sobre todas las tablas de esa base de datos.
- `'admin_bd_apellido_nombre'@'localhost'`: solo desde localhost, nunca desde la red.
:::

:::task{id="crear-operador-bd" required="true"}
Crea el usuario operador con permisos limitados.

```sql
-- Sustituye 'apellido_nombre' por tu sufijo.
CREATE USER 'operador_bd_apellido_nombre'@'localhost' IDENTIFIED BY 'PassOper456!';
GRANT SELECT, INSERT, UPDATE, DELETE ON bd_apellido_nombre.* TO 'operador_bd_apellido_nombre'@'localhost';
```
:::

:::note{}
El usuario operador **no** tiene permisos para `CREATE`, `DROP`, `ALTER` ni `GRANT`: no puede modificar la estructura de la base de datos ni gestionar permisos de otros usuarios.
:::

:::task{id="aplicar-permisos" required="true"}
Aplica los cambios, verifica los usuarios creados y sal.

```sql
-- Sustituye 'apellido_nombre' por tu sufijo.
FLUSH PRIVILEGES;
SELECT user, host FROM mysql.user WHERE user LIKE '%bd_apellido_nombre%';
EXIT;
```
:::

:::task{id="probar-admin-phpmyadmin" required="true"}
En phpMyAdmin, conéctate como `admin_bd_apellido_nombre` (sustituye `apellido_nombre` por tu sufijo) y crea una tabla `clientes` con columnas `id` (INT, AUTO_INCREMENT, Primary) y `nombre` (VARCHAR(100)).
:::

:::task{id="probar-operador-phpmyadmin" required="true"}
Cierra la sesión del administrador, conéctate como `operador_bd_apellido_nombre` (sustituye `apellido_nombre` por tu sufijo) e inserta dos registros en la tabla `clientes`.
:::

:::evidence{id="captura-usuarios-bd" type="screenshot" required="true"}
Captura del resultado de la consulta mostrando los dos usuarios creados.
:::

:::evidence{id="captura-tabla-clientes" type="screenshot" required="true"}
Captura de phpMyAdmin mostrando la tabla `clientes` con los dos registros insertados por el operador.
:::
