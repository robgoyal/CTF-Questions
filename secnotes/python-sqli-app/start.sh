#!/bin/bash

app="bt-web-01"
docker rm --force ${app}
docker build -t ${app} .
docker run -d -p 7070:80 --name=${app} ${app}
