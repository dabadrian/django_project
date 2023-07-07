
# Proyecto Django

Este es el proyecto utilizando el framework Django


## Authors

- [@dabadrian](https://github.com/dabadrian/)


## Setup

Crear una carpeta para clonar el proyecto e instalar venv.

```bash
py -m venv venv

```
## Despliegue

Clonar el proyecto. Ejecutar venv:
```bash
.\venv\Scripts\activate
pip install django
```

En la raiz del proyecto:

```bash
  python manage.py runserver
```


## Cuentas

Las cuentas que existen en el proyecto son (nombre de usuario, contraseña):

```bash
superuser: dblanco, dblanco
usuario tipo alumno: alumno, pass2023
usuario tipo docente: docente, pass2023

```


## API Reference

### CRUD Estudiantes (cualquier usuario autenticado)

```http
  GET POST DELETE /notas/estudiantes 
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

Restricciones: CI sólo números, mail en formato correcto

### CRUD Asignaturas (usuario admin autenticado)

```http
  GET POST DELETE /notas/asignaturas 
```

| Parameter | Type     | Description                |
| :-------- | :------- | :--------------------------|
| `api_key` | `string` | **Required**. Your API key |

### CRUD Semestres (usuario admin autenticado)

```http
  GET POST DELETE /notas/semestres
```

| Parameter | Type     | Description                |
| :-------- | :------- | :--------------------------|
| `api_key` | `string` | **Required**. Your API key |

### Crear notas (usuario docente autenticado)


```http
  POST /notas/nota
```
Json a enviar:
```json
{
  "nota": "100.00",
  "estudiante": 1,
  "asignatura": 1,
  "semestre": 1
}
```

Restricciones: Nota entre los valores 0.00 a 100.00



