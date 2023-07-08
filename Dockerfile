# Base image
FROM python:3

# Set the working directory
WORKDIR /yacht-shop

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the desired port (e.g., 8000)
#EXPOSE 8000

# Run the application
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]