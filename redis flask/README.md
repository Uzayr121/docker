## Deploying redis flask app using Docker compose

## Overview

This project showcases a lightweight microservices setup where a Flask-powered web app tracks and displays visitor counts using Redis as the backing store. Docker Compose ties everything together, running the app, Redis, and an Nginx load balancer as isolated, collaborative containers. It's a practical dive into container orchestration, state persistence, and scalable web service design.


## File structure
<pre> redis-flask/ ├── images/ │ ├── about.png │ ├── count.gif │ └── main.png ├── templates/ │ ├── about.html │ ├── count.html │ └── index.html ├── app.py ├── docker-compose.yml ├── Dockerfile ├── nginx.conf └── README.md </pre>
## Tools used

- **Python (Flask)** — Backend web framework  
- **Redis** — In-memory key-value store for fast data access  
- **HTML** — Frontend for user interaction  
- **Docker** — Containerisation of services  
- **Docker Compose** — Orchestration of multi-container app  
- **Nginx** — Reverse proxy and load balancer  


## Local Set-up

1. **First clone the repo**
    open the terminal and run this command
    `` git clone https://github.com/Uzayr121/docker``

2. **CD into project folder**
    do this
    ``cd "redis app"``

3. **Start the containers**
    Make sure to have docker engine running
    ``docker-compose up``

4. **Test locally**
    access on the internet using http://localhost:5001



## Dockerfile

``FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install flask redis
EXPOSE 5001
CMD ["python", "app.py"]``

- simple Dockerfile used to create a flask app using redis
- `FROM` specifies our base image
- `WORKDIR` we set our directory in our container 
- `COPY` we copy everything in the host to the container inside the `WORKDIR`
- `RUN` installs our dependencies
- `EXPOSE` tells docker what port to listen on, doesn't actually expose it 
- `CMD` tells docker to run these commands when the container is running


## Docker-compose

``services:
  
  web: 
    build: .
    expose:
      - "5001"
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
  redis: 
    image: "redis:latest"
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data  # This is the volume that will be created
      # /data is where data is stored in the redis image
      # in the redis service, we are mounting the volume redis-data to /data  
  nginx:
    image: "nginx:latest"
    ports: 
    - "5001:5001"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web



volumes:
  redis-data: # This is the volume that will be created
``

- Docker-compose.yml file to run multiple containers
- **web service** is for our app, specifies what port to expose and adds service dependency, so it only starts after the redis db has started. Use of environment variables so it can connect to the redis database
- **redis**, uses the latest image and exposes the default redis ports, named volume is added for persistent storage 
- **nginx**, used for load balancing for higher availability. Uses latest image, listens and receives traffic from port 5001 same as the app. has service dependency so will only start after the app is created
- **volumes** this is where we specify the volume created


## Results

![main](/redis%20flask/images/main.png)
![about](/redis%20flask/images/about.png)
![count](/redis%20flask/images/count.gif)