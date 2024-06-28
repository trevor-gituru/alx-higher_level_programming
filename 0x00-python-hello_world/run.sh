#!/bin/bash

# Check if the source file arguent is provided
if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <task-number>"
	exit 1
fi

# Assign source file to a variable
SOURCE_FILE=$1

#Compile source file with specified flags & output as '<task-number>.out'
gcc -Wall -Werror -pedantic -Wextra -std=gnu89 "$1"* -o "_$1.out" 

# Check if compilation was successf
if [ $? -eq 0 ]; then
	echo "Compilation was succesful, Executable file _$1 created"
	./"_$1".out
else
	echo "Compilaton failed."
fi
