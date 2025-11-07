# ${{ values.appName }}

${{ values.description }}

## Overview

This is a Python web application built with Flask that displays sample data from public APIs. The application fetches posts and user information from JSONPlaceholder API and presents them in a modern, responsive web interface.

## Features

- **Web Dashboard**: Beautiful, responsive web interface displaying sample data
- **Public API Integration**: Fetches data from JSONPlaceholder (no authentication required)
- **Modern UI**: Clean, gradient-based design with card layouts
- **Health Endpoint**: `/health` endpoint for monitoring
- **OpenShift DevSpaces Ready**: Includes devfile.yaml for instant cloud development environment

## Prerequisites

- Python 3.11+
- Docker (for containerization)

## Local Development

### Running the application

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:8080`

### Using Docker

Build the image:
```bash
docker build -t ${{ values.appName }}:latest .
```

Run the container:
```bash
docker run --rm -p 8080:8080 ${{ values.appName }}:latest
```

The application will be available at `http://localhost:8080`

## API Endpoints

- `GET /` - Main dashboard displaying posts and users
- `GET /health` - Health check endpoint

## OpenShift DevSpaces

This project includes a `devfile.yaml` that configures an OpenShift DevSpaces workspace for cloud-based development. 

### Opening in DevSpaces

1. Click the "Open in DevSpaces" link in Backstage after scaffolding
2. Or manually open: `https://<devspaces-url>#https://github.com/${{ values.githubOrg }}/${{ values.appName }}`

The devfile.yaml configures:
- Python 3.11 development environment
- Automatic dependency installation
- Flask development server with hot reload
- Port 8080 exposed for web access

### DevSpaces Workspace Features

- **Pre-configured Environment**: Python 3.11 with Flask ready to use
- **Auto-install**: Dependencies are automatically installed when workspace opens
- **Hot Reload**: Code changes are automatically reflected in the running application
- **Port Forwarding**: Application accessible via DevSpaces port forwarding

## Data Source

This application uses the [JSONPlaceholder API](https://jsonplaceholder.typicode.com) to fetch sample posts and user data. No authentication is required.

## CI/CD

This project includes a GitHub Actions workflow that automatically builds and pushes Docker images to Quay.io when changes are pushed to the main branch.

### Required Secrets

Configure the following secrets in your GitHub repository:

- `QUAY_USERNAME`: Your Quay.io username
- `QUAY_PASSWORD`: Your Quay.io password or token

### Image Location

Images are pushed to: `${{ values.quayRepo }}`

## Repository

This repository is part of the `${{ values.githubOrg }}` GitHub organization.

