# Getting official image from Docker-hub
FROM python:3.11-slim as builder

# Settings work directory 
WORKDIR /usr/src/app

# Creating env variables for python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt
COPY . .

# Getting official image from Docker-hub
FROM python:3.11-slim

# Createing work directory 
RUN mkdir -p /home/app/

# Creating user with permissions
RUN adduser app && usermod -aG sudo app

# Creating env variables for containers
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# Copy project
COPY . $APP_HOME
# Assing permisions for user for whole project
RUN chown -R app:app $APP_HOME

# Changing user
USER app
