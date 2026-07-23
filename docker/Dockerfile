# Enables commands from
FROM python:latest

# Add author info
LABEL org.opencontainers.image.authos="thomath@chalmers.se"

# Copy local files into container
COPY /backend/ /backend/

# Set working directory (of container)
WORKDIR /backend

# Execute commands (in container)
RUN pip install -r requirements.txt

# What to run when running container from image ["program", "file"]
CMD ["python", "app/main.py"]
