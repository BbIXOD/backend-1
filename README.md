# Goal
Simple containerized flask api with one endpoint

# Run locally
1. setup and enter virtual env (optional): `python3 -m venv venv && source ./env/bin/activate`
2. install required packages `pip install requirements.txt`
3. run app `flask run -p 3030`

# Run in container
1. install docker
2. run it (for systemd devices: `sudo systmectl start docker`)
3. build `docker build -t simple_api .`
4. run `docker run -it --rm --network=host -e PORT=8080 simple_api`
Note: `simple_api` can be changed to any name you want

# Run with docker-compose
1. install docker-compose
2. build `docker-compose build`
3. run `docker-compose up`

# Usage:
on get request program sends current time in Kyiv and status code 200.

# Hosted link
https://backend-1-ejet.onrender.com

# Student info
Дячок Максим Андрійович. ІМ-21
