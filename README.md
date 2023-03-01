# django-todo

- Clone the project
- Go to project folder `cd django-todo`
- Run `docker build -t django-todo -f ./docker/Dockerfile .`
- Run `docker run -p 8000:8000 django-todo docker/start_django.sh`
- Go to `http://localhost:8000/api-docs/swagger/` to view SwaggerUI
- Go to `http://localhost:8000/admin/` to view DjangoAdmin

#### Django Admin account
Username: admin\
Password: admin
