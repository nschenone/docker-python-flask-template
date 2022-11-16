# Docker Python Flask Template
Template for creating a Dockerized application using Python, Flask, Docker, and Docker Compose.


## Table of Contents
- [Prerequisites](#prerequisites)
- [Overview](#overview)
- [Sample Application](#sample-application)
- [Getting Started](#getting-started)
- [License](#license)

## Prerequisites
Ensure you have [Docker](https://docs.docker.com/get-docker/), [Docker Compose](https://docs.docker.com/compose/install/), and [Python](https://www.python.org/downloads/) installed.

## Overview
This template allows you to create and deploy a Python application using Flask and Docker. Docker Compose is used to build the Docker image, inject environment variables, and act as a starting point to add additional services to your application.

The template contains the following files and directories:
- `src/`: Directory for source code - will be copied into Docker image
    - `src/app.py`: Sample Flask application
    - `src/hello_world.py`: Sample Python script used in Flask app
- `default.env`: Default environment file for secret management - should be renamed to `.env` and never checked into source control
- `docker-compose.yml`: Default Docker Compose file that injects secrets from `.env` file and builds Docker image specified by `Dockerfile`
- `Dockerfile`: Default Dockerfile that copies source code, installs Python dependencies, and runs Flask server
- `Makefile`: Helper to easily start, stop, and restart app
- `requirements.txt`: Defines list of Python requirements that are used by the application and will be installed into the Docker image

## Sample Application
The sample application is purely a skeleton to build off of. There are two routes defined in the Flask app:
| Endpoint  | Description |
| ------------- | ------------- |
| `/`  | Test connection - will return `Connected` if successful. |
| `/hello/<name>`  | Invokes a function in the Python script using the provided parameter - will return `Hello <name>!` if successful.  |

## Getting Started
1. Clone the repository.
1. Copy the `default.env` file to a new file called `.env` and populate with your desired port and any secrets
    - This should never be commited into source control - this template is setup to ensure the `.env` file is excluded from Git
1. Build your Python application in the `src` directory.
1. Deploy the app by running `make up`.
1. Navigate to `http://<IP_ADDRESS>/<FLASK_PORT>` (e.g. [http://localhost:5050](http://localhost:5050)) in your browser - you should see `Connected` if successful. 
    - `IP_ADDRESS` is the IP address of the machine running Docker.
    - `FLASK_PORT` is the port defined in your `.env` file (default is 5050)
1. Update app with any changes by re-running `make up`
1. Restart app by running `make restart`
1. Stop app by running `make down`

## License
This template is made available under a modified MIT license. See the LICENSE file.