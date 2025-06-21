# flask-app

A containerized Python Flask application.

## Overview

This repository contains a simple Flask web application. The application is built and published automatically to GitHub Container Registry (GHCR) via GitHub Actions.

## Getting Started

### Local Development

1. **Clone the repo:**
    ```
    git clone https://github.com/AlexeyPetroff/flask-app.git
    cd flask-app/app
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Run locally:**
    ```
    FLASK_ENV=development python main.py
    ```

4. **Test healthcheck:**
    ```
    curl http://localhost:8080/healthcheck
    ```

