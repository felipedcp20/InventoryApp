# App Inventory

## Instalación

1. Clona este repositorio:

 git clone https://github.com/felipedcp20/inventoryAPP.git
   

2. Crea un ambiente virtual:

python3 -m venv env
   


3. Activa el ambiente virtual:
- En Windows:
env\Scripts\activate
     
En macOS y Linux:
source env/bin/activate
     


4. Instala las dependencias del proyecto:
pip install -r requirements.txt
   


## Endpoints

### USERS
- `GET /users`: Obtiene una lista de todos los usuarios.
- `GET /user/{user_id}`: Obtiene información detallada sobre un usuario específico.
- `POST /user`: Crea un nuevo usuario.
- `PUT /user/{user_id}`: Actualiza la información de un usuario existente.
- `DELETE /user/{user_id}`: Elimina un usuario existente.

### ITEMS
- `GET /items`: Obtiene una lista de todos los items.
- `GET /item/{item_id}`: Obtiene información detallada sobre un item específico.
- `POST /item`: Crea un nuevo item.
- `PUT /item/{item_id}`: Actualiza la información de un item existente.
- `DELETE /item/{item_id}`: Elimina un item existente.

### CREATE SQL COMMANDS

CREATE DATABASE inventario;

USE inventario;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    full_name VARCHAR(50) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT true,
    is_superuser BOOLEAN NOT NULL DEFAULT false,
    role ENUM('empleado', 'TI') NOT NULL DEFAULT 'empleado'
);

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(100),
    owner_id INT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES users (id)
);
