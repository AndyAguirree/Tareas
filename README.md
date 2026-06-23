# TAREAS (Django) - Administrador de Tareas (To-Do)

## Requisitos
- Python 3.x
- PostgreSQL

## Configuración
Crea/ajusta el archivo `.env` con las variables de base de datos.
Este proyecto ya incluye un `.env` dentro de `TAREAS/`.

## Instalación
```bash
cd TAREAS
python -m venv entorno
# Windows:
entorno\Scripts\activate
# Luego:
pip install -r requirements.txt
```

## Migraciones y ejecución
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Abre: http://127.0.0.1:8000

## Roles (seguridad)
- Anónimo: solo puede ver el listado.
- Usuario registrado: puede crear y editar.
- Admin (`is_staff` o superusuario): puede además eliminar.
```

