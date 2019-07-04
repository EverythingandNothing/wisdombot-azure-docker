#!/bin/bash

PORT=80

docker container stop wisdom-app > /dev/null
docker container rm wisdom-app > /dev/null

docker build -t twap:latest .
docker run -d -p"${PORT}:${PORT}" \
           --name wisdom-app \
           --mount type=bind,source="$(pwd)"/truisms.csv,target=/truisms.csv \
           twap:latest
