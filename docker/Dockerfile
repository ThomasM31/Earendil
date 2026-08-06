# Enables commands from, change to specific version??
FROM python:latest

# Add author info
LABEL org.opencontainers.image.authos="thomath@chalmers.se"

# Set working directory (of container)
WORKDIR /app

# Copy local files into container
COPY . .
COPY alembic ./alembic
COPY alembic.ini .
COPY ../requirements.txt .

# Create venv. in container
RUN python -m venv /env

# Setup virtual env. variables
ENV VIRTUAL_ENV=/env
ENV PATH=/env/bin:$PATH

# Install packages in reqs.
RUN pip install -r requirements.txt

# What to run when running container from image ["program", "file"] (Path in WORKDIR)
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]