#!/bin/bash

greeting="h to your name"

if ! $greeting ; then
    echo $greeting
else
    echo "Empty greeting"
fi