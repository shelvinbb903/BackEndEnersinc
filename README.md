## Detalles del proyecto
- Python
- Django
- PostgreSQL
- pgAdmin
- DBeaver

## Instrucciones de Despliegue Local

Para realizar la verificación de los puntos de la prueba técnica se deben seguir los siguientes pasos:

- Clonar el proyecto, ya sea con el comando git clone https://github.com/shelvinbb903/PruebaTecnicaEnersinc.git o usando una herramienta grafica GitHub

- Después de clonar el repositorio, acceder a la carpeta descargada con el comando cd en la terminal, ya que en ella se ejecutarán varios comandos.

- Activar enviroment de python con los comandos: 
```
python -m venv env
source env/Scripts/activate
```

- Instalar las dependencias necesarias y usadas para la prueba con el comando: ```pip install -r requirements.txt```

- Crear la base de datos en el administrador de su preferencia. Por ejemplo, puede usar pgAdmin para crear la base de datos y DBeaver para realizar la conexión a la base de datos y ver la estructura de las tablas. Para la prueba, el nombre que se uso fue prueba, pero puede usar otro nombre.

- Cambiar la conexión a la base de datos archivo PruebaTecnica/settings.py del proyecto. En este archivo se modifican el diccionario u objeto DATABASES, el cual tiene los atributos para la conexión establecida por defecto. Se modifican los atributos USER y PASSWORD, los cuales tienen su configuración establecida durante la instalación de PostgreSQL en su equipo y NAME que corresponde al nombre de la base de datos que generó en el paso anterior.

- Ejecutar las migraciones para generar la estructura de las tablas en la base de datos creada. Se realiza con el comando: ```python manage.py migrate```

- En este punto, el proyecto está listo para realizar prueba. Se realiza la ejecución con el comando: ```python manage.py runserver```

## Nota Adicional

- Se agregó el archivo postman_collections con todas las API rest desarrolladas.
