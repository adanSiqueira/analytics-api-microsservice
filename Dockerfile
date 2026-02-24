# Base image
FROM python:3.13.2-slim-bookworm

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN pip install --upgrade pip

# Python environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /code

# Copy requirements first (better layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy entire src directory (KEEP STRUCTURE)
COPY ./src ./src

# Copy boot script
COPY ./boot/docker-run.sh /opt/run.sh
RUN chmod +x /opt/run.sh

# Run app
CMD ["/opt/run.sh"]