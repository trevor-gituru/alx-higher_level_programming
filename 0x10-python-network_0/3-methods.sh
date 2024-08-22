#!/bin/bash
# Task 3
curl -sI "$1" | grep "Allow:" | cut -d' ' -f2- 
