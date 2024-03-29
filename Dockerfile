# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
RUN pip install poetry

WORKDIR /app
COPY . /app

# Install poetry dependencies
RUN POETRY_VIRTUALENVS_CREATE=false poetry install --only main

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

ENTRYPOINT ["./docker-entrypoint.sh"]
