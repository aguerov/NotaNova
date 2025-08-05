# NotaNova

NotaNova es un backend construido con [FastAPI](https://fastapi.tiangolo.com/) y [SQLModel](https://sqlmodel.tiangolo.com/) para crear notas por voz, agendar recordatorios y organizar rutinas personalizadas.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución local

```bash
uvicorn app.main:app --reload
```

## Despliegue en Render

1. Crea un nuevo servicio **Web Service** en [Render](https://render.com) conectado a este repositorio.
2. Configura los comandos:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
3. Realiza el deploy.
