# Goal
Simple containerized flask api with two endpoints

# Run locally
1. Setup and enter virtual env (optional): `python3 -m venv venv && source ./env/bin/activate`
2. Install required packages `pip install requirements.txt`
3. Run app `flask run -p 3030`

# Run in container
1. Install docker
2. Run it (for systemd devices: `sudo systmectl start docker`)
3. Build `docker build -t simple_api .`
4. Run `docker run -it --rm --network=host -e PORT=8080 simple_api`

Note: `simple_api` can be changed to any name you want

# Run with docker-compose
1. Install docker-compose
2. Build `docker-compose build`
3. Run `docker-compose up`

# Usage:
On get request on path `/healthcheck` program sends json with 2 fields: current time in Kyiv, server status and status code 200. Json has next structure: `{ date: string, status: string }`

Also on request to just `/` will say "Check my health!"

# Hosted link
https://backend-1-ejet.onrender.com

# Student info
Дячок Максим Андрійович. ІМ-21
