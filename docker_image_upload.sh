#!/bin/bash

# Docker Hub username
DOCKER_USERNAME=shaqdevops

# Image names
BACKEND_IMAGE="slide_backend"
FRONTEND_IMAGE="slide_frontend"

# Version tag (optional)
VERSION="latest"

# Build backend image
echo "Building backend image..."
docker build -t $BACKEND_IMAGE ./slide_backend

# Tag backend image
echo "Tagging backend image..."
docker tag $BACKEND_IMAGE:latest $DOCKER_USERNAME/$BACKEND_IMAGE:$VERSION

# Push backend image
echo "Pushing backend image to Docker Hub..."
docker push $DOCKER_USERNAME/$BACKEND_IMAGE:$VERSION

# Build frontend image
echo "Building frontend image..."
docker build -t $FRONTEND_IMAGE ./slide_frontend

# Tag frontend image
echo "Tagging frontend image..."
docker tag $FRONTEND_IMAGE:latest $DOCKER_USERNAME/$FRONTEND_IMAGE:$VERSION

# Push frontend image
echo "Pushing frontend image to Docker Hub..."
docker push $DOCKER_USERNAME/$FRONTEND_IMAGE:$VERSION

# Confirm the push is complete
echo "All images have been pushed to Docker Hub."
