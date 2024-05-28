# Wybierz obraz podstawowy
FROM python:3.12.0-slim

# Ustaw zmienną środowiskową
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Skopiuj plik gunicorn.exe do katalogu /usr/local/bin wewnątrz kontenera
COPY gunicorn.exe /usr/local/bin/

# Zainstaluj Gunicorn
RUN pip install gunicorn

# Utwórz katalog roboczy
WORKDIR /container

# Skopiuj plik requirements.txt
COPY requirements.txt /container/

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę kodu aplikacji
COPY . /container/

# Dodaj bieżący katalog do zmiennej PATH
ENV PATH="/testo:${PATH}"

# Otwórz port
EXPOSE 8000

# Ustaw domyślną komendę startową
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "testo.wsgi:application"]
