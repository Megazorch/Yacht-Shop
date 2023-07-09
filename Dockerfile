# version 1.1
FROM docker.io/oz123/pipenv:3.11-v2023-6-26 AS builder

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

# Pipfile contains requests
ADD Pipfile.lock Pipfile /usr/src/

WORKDIR /usr/src

RUN pipenv requirements > requirements.txt

# Base image
FROM python:3.11.4-slim-bullseye AS runtime

# Set the working directory
WORKDIR /yacht-shop

# Copy the requirements file
COPY --from=builder /usr/src/requirements.txt /yacht-shop

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .
