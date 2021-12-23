

## Part-1
### Run Project with docker:
     #### CMD 
     ```
     docker build --tag python-django .
     ```
     ```
     docker run --publish 8000:8000 python-django

     ```
     #### .dockerignore.
     ```
          */venv
     ```
     #### Dockerfile
     ```
     FROM python:3.8-slim-buster

     WORKDIR /app

     COPY requirements.txt requirements.txt
     RUN pip3 install -r requirements.txt
     COPY . .
     CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
     ```

## Part-2
### Run Project with docker compose :
     #### CMD 

     ```
    docker-compose build
    ```
    ```
    docker-compose run --rm app django-admin startproject core .
    ```
    ```
    docker-compose up
    ```
     #### Dockerfile
     ```
     FROM python:3.8-slim-buster
     ENV PYTHONUNBUFFERED=1

     WORKDIR /django
     COPY requirements.txt requirements.txt
     RUN pip3 install -r requirements.txt
     ```

     #### docker-compose.yml
     ```
     services:
          app:
               build: .
                    # path where docker file exists
               volumes:
                    - .:/django
                    # copy project_dir_to: Dockerfile Working Dir
               ports:
                    - 8000:8000
               image: app:django
               container_name: django_container1
               command: python manage.py runserver 0.0.0.0:8001

     ```
     ###### url: localhost:8000 or 0.0.0.0:8000

 
    #### Stop all running containers: 
    ```
    docker stop $(docker ps -a -q)
    ```
    #### Delete all stopped containers: 
    ```
    docker rm $(docker ps -a -q)
    ```
     #### Delete all Docker images
     ```
     docker rmi $(docker images -q)
     ```


    