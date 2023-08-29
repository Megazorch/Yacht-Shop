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

ENV YACHT_SHOP=/home/app/yacht_shop
ENV APP_USER=megazorch
RUN addgroup --system $APP_USER && adduser --system $APP_USER --ingroup $APP_USER


# Set the working directory
RUN mkdir -p $YACHT_SHOP && \
    mkdir -p $YACHT_SHOP/static && \
    mkdir -p $YACHT_SHOP/media
WORKDIR $YACHT_SHOP

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Giving the script an executable permissions
RUN chmod +x /home/app/yacht_shop/entrypoint.sh

# Set ownership and permissions for the media directory
RUN chown -R megazorch:megazorch /home/app/yacht_shop/media

# Copy the application code from the 'builder' stage
COPY --from=builder /usr/src $YACHT_SHOP

# Execute script
ENTRYPOINT ["/home/app/yacht_shop/entrypoint.sh"]

