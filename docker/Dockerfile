# ------------------------------------------------------ Backend ------------------------------------------------------
# Enables commands from
FROM python:latest

# Add author info
LABEL org.opencontainers.image.authos="thomath@chalmers.se"

# Copy local files into container
COPY backend/ /app/

# Set working directory (of container)
WORKDIR /app

# Execute commands (in container)
RUN pip install -r requirements.txt

# What to run when running container from image ["program", "file"]
CMD ["python", "app/main.py"]

# ------------------------------------------------------ Database ------------------------------------------------------

