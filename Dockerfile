FROM python:3.12-slim

# Evita que Python bufferice stdout/stderr y no genera archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Crear usuario sin privilegios root
RUN adduser --disabled-password --gecos "" appuser

# Copiar configuración e instalar dependencias
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copiar el código fuente
COPY app/ ./app

# Asignar permisos al usuario no root
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]