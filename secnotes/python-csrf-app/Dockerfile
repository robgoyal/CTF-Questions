FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN apt update
RUN apt install bash vim sqlite3 -y
ENV STATIC_URL /static
ENV STATIC_PATH /app/app/static
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app
RUN sed -i "s/<REPLACE_SECRET_KEY>/$(echo $RANDOM | md5sum | head -c 20)/g" /app/app/__init__.py
RUN sed -i "s/<REPLACE_KATE_PASSWORD>/$(echo $RANDOM | md5sum | head -c 10)/g" /app/app/__init__.py
RUN sed -i "s/<REPLACE_JESS_PASSWORD>/$(echo $RANDOM | md5sum | head -c 10)/g" /app/app/__init__.py
RUN sed -i "s/<REPLACE_ADAM_PASSWORD>/$(echo $RANDOM | md5sum | head -c 10)/g" /app/app/__init__.py
