# Discordia App

Proyecto Grupal Integrador de la carrera de Desarrollo en Software.

Este proyecto es una API de clon de Discord desarrollada como parte de nuestro proyecto integrador para la universidad.
Está diseñada para ofrecer una funcionalidad similar a la plataforma Discord, permitiendo a los usuarios crear
servidores, canales de chat, enviar mensajes. Es una solución versátil y escalable que
puede servir como base para la construcción de una aplicación de chat y comunicación en tiempo real.



## Características Clave
- Creación y gestión de servidores y canales de chat.
- Envío de mensajes de texto.
- Integración con avatares y perfiles de usuario.
- Autenticación de usuarios.


### Teconlogias Utilizadas

- ![Flask](https://img.shields.io/badge/Flask-Framework-red?style=for-the-badge&logo=flask)
- ![Python](https://img.shields.io/badge/Python-Programming_Language-blue?style=for-the-badge&logo=python)
- ![MySQL](https://img.shields.io/badge/MySQL-Database-blue)
- ![Postman](https://img.shields.io/badge/Postman-API-orange?style=for-the-badge&logo=postman)
- ![Pycharm](https://img.shields.io/badge/Pycharm-IDE-blue?style=for-the-badge&logo=pycharm)
- ![VSCode](https://img.shields.io/badge/VSCode-IDE-blue?style=for-the-badge&logo=visual-studio-code)
- ![Git](https://img.shields.io/badge/Git-SCM-blue?style=for-the-badge&logo=git)
- ![GitHub](https://img.shields.io/badge/GitHub-SCM-blue?style=for-the-badge&logo=github)
- CORS (Cross-Origin Resource Sharing)

## Table of Contents (Tabla de Contenidos)

1. [Requisitos](#requisitos)
2. [Instalación](#instalación)
3. [Uso](#uso)
4. [Contribución](#contribución)
5. [Licencia](#licencia)
6. [Guia](#guia)

## Requisitos

- Python 3.9 / 3.10.8
- Flask 2.3.2
- pip
- virtualenv (opcional)
- git
- [requirements.txt](requirements.txt)

## Instalación

- Clonar el repositorio desde GitHub [Integrador](https://github.com/gaston010/Integrador)
- renombrar el archivo .env.example a .env
- Crear un entorno virtual con virtualenv
- Activar el entorno virtual
- Instalar las dependencias con pip
- Ejecutar el proyecto

```bash
git clone https://github.com/gaston010/Integrador.git
```

```bash
cd Integrador
```

```bash
mv .env.example .env
```

```bash
virtualenv venv
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

## Uso


Por el momento la API se encuentra en un servidor de pruebas para poder hacer peticiones atraves de la misma(NO WEB).
[API](https://api-2-svwb.onrender.com) donde en el mismo / se listan todos los endpoints disponibles.

## Guia
Dentro del proyecto se encuentra un archivo llamado PeticionesGenerales.http,
el cual contiene las peticiones necesarias para probar el proyecto.
(O en el caso con Pycharm, se puede ejecutar el archivo directamente)
(Se recomienda usar la extensión de VSCode REST Client)

Ejemplo de peticiones para listar los servidor y agregar un servidor:

`GET 127.0.0.1:5000/api/server/list` - Lista todos los servidores (ejemplo de salida)

```JSON
{
  "Servers": [
    {
      "autor_id": 2,
      "descripcion": "Un servidor para testeo",
      "estado": 1,
      "fecha_creacion": "Tue, 26 Sep 2023 01:49:16 GMT",
      "icono": null,
      "id_servidor": 24,
      "nombre_servidor": "Servidor de Prueba",
      "ultima_actualizacion": "Tue, 26 Sep 2023 01:49:16 GMT"
    },
    {
      "autor_id": 1,
      "descripcion": "VideoJuegos",
      "estado": 1,
      "fecha_creacion": "Tue, 26 Sep 2023 02:09:38 GMT",
      "icono": null,
      "id_servidor": 25,
      "nombre_servidor": "Gamer",
      "ultima_actualizacion": "Tue, 26 Sep 2023 02:09:38 GMT"
    }
  ]
}
```

`POST 127.0.0.1:5000/api/server/add` - Agrega un servidor (ejemplo de entrada)

**Content-Type: application/json**

```JSON
{
  "nombre_servidor": "Servidor de Ejemplo",
  "descripcion": "Añadiendo un servidor de ejemplo",
  "autor_id": 2
}
```

La respuesta es un JSON con el nuevo servidor creado y el código de estado 201

```JSON
{
  "Info": [
    {
      "New Server info:": [
        {
          "autor_id": 2,
          "descripcion": "Add user on server auto?",
          "estado": 1,
          "fecha_creacion": "Tue, 26 Sep 2023 16:10:05 GMT",
          "icono": null,
          "id_servidor": 26,
          "nombre_servidor": "Nuevo Servidor",
          "ultima_actualizacion": "Tue, 26 Sep 2023 16:10:05 GMT"
        }
      ],
      "message": "Server created successfully"
    },
    201
  ]
}
```

## Contribución

- [Ana](https://github.com/AnitaGomez2183)
- [Gastón](https://github.com/gaston010)
- [Javier](https://github.com/FSALVA157)
- [Virginia](https://github.com/virginia1612)


¡Agradecemos las contribuciones! Si deseas contribuir a este proyecto, por favor sigue los pasos:

Crea un fork del repositorio.
Trabaja en tus cambios en una rama (branch) separada.
Envía una solicitud de extracción (pull request) con una descripción detallada de tus cambios.


## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para obtener más detalles.
