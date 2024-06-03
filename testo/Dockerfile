# Wybierz obraz podstawowy
FROM osgeo/gdal:ubuntu-full-3.3.0

RUN apt-get update && apt-get install -y curl python3-pip  && rm -rf /var/lib/apt/lists/*

WORKDIR /container

COPY requirements.txt /container/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /container/

