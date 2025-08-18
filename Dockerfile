FROM python:3.10-slim

# Set working directory
WORKDIR /app

COPY models/ /app/models/
COPY scripts/ /app/scripts/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r scripts/requirements.txt

# Set entrypoint
CMD ["python", "scripts/main.py"]
