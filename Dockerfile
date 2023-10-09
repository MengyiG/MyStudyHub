FROM python:3.11-slim-buster

# sets the current working directory for subsequent instructions in the Dockerfile
WORKDIR /app

# copy the requirements.txt file to the working directory
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy the current directory contents into the container at /app
COPY . .

# run the command to start uWSGI
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]