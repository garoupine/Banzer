#!/bin/bash

# Check if the driver program exists
if [ -f driver ]
then
  # Execute the driver program
  ./driver
else
  # Run make command
  make
  
  # Check if the make command was successful
  if [ $? -eq 0 ]
  then
    # Execute the driver program
    ./driver
  else
    echo "Make failed. Cannot run program."
  fi
fi

