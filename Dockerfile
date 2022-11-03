FROM python:3.9.15-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install nginx
RUN apt-get update && apt-get install nginx -y --no-install-recommends

COPY nginx.default /etc/nginx/sites-available/default

RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log


RUN mkdir -p /opt/app && \
    chown -R www-data:www-data /opt/app

WORKDIR /opt/app


COPY requirements.txt entrypoint.sh /opt/app
RUN pip install --upgrade pip && \
	pip install -r requirements.txt


COPY . .

# start server
EXPOSE 80


# gunicorn core.wsgi --user www-data --bind 0.0.0.0:8050
# gunicorn core.asgi:application -k uvicorn.workers.UvicornWorker

RUN chmod +x entrypoint.sh


#ENTRYPOINT ["/opt/app/entrypoint.sh"]
ENTRYPOINT ["sh", "-c", "/opt/app/entrypoint.sh"]
