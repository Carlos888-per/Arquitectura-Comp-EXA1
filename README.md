# Analizador de representación de datos

Aplicación educativa con Python 3.12 y Django para convertir enteros entre bases 2, 8, 10 y 16, y explorar la codificación Unicode/UTF-8 carácter por carácter.

## Funcionalidades

- Valida enteros entre 0 y 65 535 y muestra sus representaciones decimal, binaria, octal y hexadecimal.
- Completa el binario con ceros a la izquierda hasta un número entero de bytes e informa bits significativos y bytes mínimos.
- Acepta textos de hasta 20 caracteres y presenta carácter, decimal, punto de código U+, hexadecimal y bytes UTF-8.
- Incluye mensajes de validación en español y pruebas automatizadas.

## Ejecutar con Docker

Requiere Docker Engine y Docker Compose. Desde la carpeta del proyecto:

```bash
docker compose up --build
```

Compose limita el servicio a 256 MB de RAM y 1 CPU. Abre <http://localhost:8000>. Para detenerlo, pulsa `Ctrl+C` y ejecuta `docker compose down`.

Para revisar el consumo y guardar evidencia de `docker stats`:

```bash
docker compose up --build -d
docker compose ps
docker stats --no-stream analizador-web-1
docker compose down
```

El nombre del contenedor puede variar; usa el que aparezca en `docker compose ps`. Para conservar la evidencia en un archivo, redirige la salida:

```bash
docker stats --no-stream NOMBRE_DEL_CONTENEDOR > docker-stats.txt
```

## Ejecutar localmente

Requiere Python 3.12:

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Abre <http://127.0.0.1:8000>.

## Pruebas

```bash
python manage.py test
```

## Arquitectura y contenedores

La aplicación usa la CPU para ejecutar Python y Django, la memoria RAM para mantener el proceso y sus datos temporales, y el almacenamiento para leer el código y los archivos del proyecto. La conversión numérica y la codificación UTF-8 se realizan en la CPU sobre datos guardados temporalmente en memoria.

Docker aísla el proceso y el sistema de archivos de la aplicación, pero los contenedores Linux comparten el kernel del sistema operativo host. No incluyen un kernel propio: Docker utiliza mecanismos de aislamiento del kernel anfitrión, lo que hace al contenedor más ligero que una máquina virtual.

## Publicación

El código fuente está en [Arquitectura-Comp-EXA1](https://github.com/Carlos888-per/Arquitectura-Comp-EXA1). Para publicar cambios en GitHub, ejecuta:

```bash
git add .
git commit -m "Describe los cambios"
git push
```