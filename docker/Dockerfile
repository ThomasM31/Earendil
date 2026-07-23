# Definition -> build image -> run container 
# NOTE: run with docker build -f path/to/Dockerfile -t name-of-image:version
# Enables commands from: 
FROM python:latest

# Copy local files into container
COPY /backend/ /backend/

# Set working directory (of container)
WORKDIR /backend

# Execute commands (in container)
RUN pip install -r requirements.txt

# What to run when running container from image
CMD ["python", "/app/main.py"]
