# Serverless AI Endpoint

This repository contains the structure for deploying a serverless AI endpoint using Docker and RunPod.

## Folder Structure

- `models/`: Place your model files here (e.g., .pt, .safetensors).
- `scripts/`: Python scripts for inference and endpoint logic.
- `Dockerfile`: Builds the container with all dependencies.
- `README.md`: Setup instructions.

## Setup Instructions

1. Clone this repository:
   git clone https://github.com/MasterNathobi/serverlessAiEndpoint.git

2. Navigate to the project directory:
   cd serverlessAiEndpoint

3. Build the Docker image:
   docker build -t serverless-ai-endpoint .

4. Run the container:
   docker run --rm -it serverless-ai-endpoint
