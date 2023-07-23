# version 1.7 | 22/07/2023
FROM docker.io/oz123/pipenv:3.11-v2023-6-26 AS builder

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

# Pipfile contains requests
ADD Pipfile.lock Pipfile /usr/src/

WORKDIR /usr/src

# Install dependencie
RUN pipenv requirements > requirements.txt

# Copy the application code
COPY . .

# Base image
FROM python:3.11.4-slim-bullseye AS runtime

# Set the working directory
WORKDIR /yacht-shop

# Copy the application code from the 'builder' stage
COPY --from=builder /usr/src /yacht-shop

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "yacht_shop.wsgi:application"]

