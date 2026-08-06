# Enables commands from
FROM python:latest

# Add author info
LABEL org.opencontainers.image.authos="thomath@chalmers.se"

# Set working directory (of container)
WORKDIR /app

# Copy local files into container
COPY app/ /app/

# Create venv. in container
RUN python -m venv /env

# Setup virtual env. variables
ENV VIRTUAL_ENV=/env
ENV PATH=/env/bin:$PATH

# Add reqs to container + execute
ADD ../requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# What to run when running container from image ["program", "file"] (Path in WORKDIR)
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]