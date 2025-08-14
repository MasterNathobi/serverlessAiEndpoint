FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy scripts and models
COPY scripts/ /app/scripts/
COPY models/ /app/models/

# Install dependencies
RUN pip install --no-cache-dir -r scripts/requirements.txt

# Set entrypoint
CMD ["python", "scripts/app.py"]
