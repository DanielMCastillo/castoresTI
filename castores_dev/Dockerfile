FROM debian:bullseye-slim

RUN apt-get update
RUN apt-get install apache2 python3 python3-pip libmariadb-dev aptitude \
    libapache2-mod-wsgi-py3 python3-dev openssh-client nano -y

RUN aptitude install gdal-bin libgdal-dev -y

RUN aptitude install python3-gdal -y

RUN aptitude install binutils libproj-dev -y

# Configure timezone
ENV TZ=America/Mexico_City
RUN ln -snf  /etc/l/usr/share/zoneinfo/$TZocaltime && echo $TZ > /etc/timezone

# Application environment
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
