# Analizador

Proyecto base con Django, Docker y Docker Compose, preparado para trabajar desde Visual Studio Code y ejecutarse en Linux.

## Requisitos

- Docker Engine y el complemento Docker Compose
- Visual Studio Code (opcional) con las extensiones Python, Pylance y Docker

## Ejecutar con Docker

Desde la carpeta del proyecto:

```bash
docker compose up --build
```

Abre <http://localhost:8000>. Para detenerlo, pulsa `Ctrl+C` y luego ejecuta `docker compose down`.

## Ejecutar localmente en Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abre <http://127.0.0.1:8000>.

## Empezar a trabajar

- La configuración del proyecto está en `config/`.
- La aplicación inicial está en `core/`.
- La página principal usa `templates/core/home.html`.
- Crea nuevas aplicaciones con `python manage.py startapp nombre`.

## Publicar en GitHub

Crea un repositorio vacío en GitHub y luego ejecuta, reemplazando la URL por la de tu repositorio:

```bash
git init
git add .
git commit -m "Inicializa proyecto Django con Docker"
git branch -M main
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin main
```

No subas secretos ni archivos `.env` al repositorio. La clave incluida en la configuración es solo para desarrollo local.
