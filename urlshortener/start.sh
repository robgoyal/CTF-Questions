#!/bin/bash

app="urlshortener"
docker rm --force ${app}
docker build -t ${app} .
docker run -d -p 9090:80 --name=${app} ${app}
