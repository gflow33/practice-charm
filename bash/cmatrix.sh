#!/bin/bash

#Get the last command that was run
last_command=$(tail -n 1 ~/.bash_history)

# Extract the process ID (PID) from the last command
pid=$(pidof cmatrix)
#echo "$last command" | awk '{print $1}')

#terminate the process if it is runnning
if [ -n "$pid" ]; then
	echo "Terminating process with PID: $pid"
	kill "$pid"
else 
	echo "No process found to terminate."
fi
