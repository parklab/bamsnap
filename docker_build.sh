
#!/bin/bash

# Define version variable
VERSION="1.0.0"

docker build -f docker/Dockerfile -t aveit/bamsnap:${VERSION} .
docker tag aveit/bamsnap:${VERSION} aveit/bamsnap:latest

# # Log in to Docker Hub
# docker login

# # Push the tagged image to Docker Hub
# docker push aveit/bamsnap:${VERSION}