#!/bin/bash

app="bt-web-02"
docker rm --force ${app}
docker build -t ${app} .
docker run -d -p 6060:80 --name=${app} ${app}
