FROM python:3.9

WORKDIR /home/app
RUN apt-get update && apt-get install nginx -y
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

#If we add the requirements and install dependencies first, docker can use cache if requirements don't change
ADD requirements.txt /home/app
RUN pip install --no-cache-dir -r requirements.txt

ADD . /home/app

EXPOSE 8080

RUN chmod +x /home/app/entrypoint.sh
CMD /home/app/entrypoint.sh
