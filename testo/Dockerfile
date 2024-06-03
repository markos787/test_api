# Wybierz obraz podstawowy
FROM osgeo/gdal:ubuntu-full-3.3.0

RUN apt-get update && apt-get install -y curl python3-pip  && rm -rf /var/lib/apt/lists/*

# # Ustaw zmienną środowiskową
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Zainstaluj Gunicorn
# RUN pip install gunicorn

# # Skopiuj plik gunicorn.exe do katalogu /usr/local/bin wewnątrz kontenera
# COPY gunicorn.exe /usr/local/bin/

# RUN pip install django

# Utwórz katalog roboczy
WORKDIR /container

# Skopiuj plik requirements.txt
COPY requirements.txt /container/

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install django

# Skopiuj resztę kodu aplikacji
COPY . /container/

# # Dodaj bieżący katalog do zmiennej PATH
# ENV PATH="/testo:${PATH}"

# # Otwórz port
# EXPOSE 8000

# # Ustaw domyślną komendę startową
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "testo.wsgi:application"]
