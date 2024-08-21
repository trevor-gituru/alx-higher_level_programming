#!/bin/bash
# Task 0
curl -sI "$1" | grep -E "^Content-Length" | cut -d' '  -f2
