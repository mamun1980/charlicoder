#!/bin/bash

CON_PS="docker ps"
CON_START="docker run --rm -d --name charlicoder -p 8000:8050 charlicoder:1.0"

git status