# Docker-related Materials

This repository shows useful commands which will help faciliate the development of docker-related projects.


## Sample files


## Docker Commands

### Image-related commands
- List all docker images
    - `docker images -a`
- Remove docker image
    - `docker rmi <image_id>`
- Remove all docker images
    - `docker rmi -f $(docker images -aq)` *(linux)*
    - `for /F %i in ('docker images -a -q') do docker rmi -f %i` *(windows)*

### Container-related commands
- List all docker containers
    - `docker ps -a`
- Stop running container
    - `docker stop <container_id>`
    - `docker stop -f $(docker ps -aq)` *(linux)*
    - `for /F %c in ('docker ps -a -q') do (docker stop %c)` *(windows)*
- Remove docker container
    - `docker rm <container_id>`
- Remove all docker containers (**Note**: You have to stop the container first before removing)
    - `docker rm -f $(docker ps -aq)` *(linux)*
    - `for /F %c in ('docker ps -a -q') do (docker rm %c)` *(windows)*



# Pruning
Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes. [reference](https://docs.docker.com/engine/reference/commandline/system_prune/)

- `docker system prune`
- `docker container prune`
- `docker image prune`
- `docker network prune`
- `docker volume prune`