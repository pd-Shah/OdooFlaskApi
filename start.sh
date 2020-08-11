#!/bin/bash
sudo docker build -t api .
sudo docker run -p 5000:5000 api