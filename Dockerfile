FROM python:3.9

WORKDIR /home/app
RUN apt-get update && apt-get install nginx -y
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log


#If we add the requirements and install dependencies first, docker can use cache if requirements don't change
ADD requirements.txt /home/app
RUN pip install --no-cache-dir -r requirements.txt

ADD . /home/app

# Migrate the database
RUN python manage.py migrate
RUN nginx -g 'daemon off;'

CMD gunicorn webappexample.wsgi:application --bind "0.0.0.0:8080" --daemon

EXPOSE 8080
