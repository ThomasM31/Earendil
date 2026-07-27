# Enables commands from
FROM python:latest

# Add author info
LABEL org.opencontainers.image.authos="thomath@chalmers.se"

# Copy local files into container
COPY backend/ /backend/

# Set working directory (of container)
WORKDIR /backend

# Create venv. in container
RUN python -m venv /env

# Setup virtual env. variables
ENV VIRTUAL_ENV=/env
ENV PATH=/env/bin:$PATH

# Add reqs to container + execute
ADD ../backend/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# What to run when running container from image ["program", "file"]
CMD ["python", "app/main.py"]