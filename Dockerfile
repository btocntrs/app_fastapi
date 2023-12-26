# Usa una imagen base de Python
FROM python:slim

# Establece el directorio de trabajo en /app
WORKDIR /API

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del directorio actual al contenedor en /app
COPY ./app /API/app

# Expone el puerto 8000 (o el que utilice tu aplicación FastAPI)
EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]