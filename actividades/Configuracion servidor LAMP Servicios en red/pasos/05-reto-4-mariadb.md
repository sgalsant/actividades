---
id: reto-4-mariadb
titulo: Reto 4 - Instalacion de MariaDB
duracion_minutos: 25
obligatorio: true
---

MariaDB es un sistema de gestion de bases de datos relacional, fork de MySQL. Permite almacenar y consultar datos de forma estructurada mediante SQL.

:::task{id="instalar-mariadb" required="true"}
Instala MariaDB Server.
:::

```bash
sudo apt install -y mariadb-server
```

:::task{id="segurizar-mariadb" required="true"}
Ejecuta `mysql_secure_installation` y responde al asistente:

- Enter current password for root: introduce la contrasena de root elegida.
- Switch to unix_socket authentication? `N`.
- Change the root password? `Y` y anotala.
- Remove anonymous users? `Y`.
- Disallow root login remotely? `Y`.
- Remove test database? `Y`.
- Reload privilege tables now? `Y`.
:::

```bash
sudo mysql_secure_installation
```

:::task{id="probar-mariadb" required="true"}
Conectate como root, consulta la version y sal.
:::

```bash
sudo mysql -u root -p
SELECT VERSION();
EXIT;
```

:::task{id="habilitar-mariadb" required="true"}
Verifica que MariaDB se inicia automaticamente.
:::

```bash
sudo systemctl is-enabled mariadb
```

:::evidence{id="captura-mariadb" type="screenshot" required="true"}
Captura de la pantalla final de `mysql_secure_installation` con el mensaje `All done!`.
:::
