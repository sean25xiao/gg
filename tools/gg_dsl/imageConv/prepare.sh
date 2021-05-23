#!/bin/bash -e

cd ./imageConv
gcc -std=gnu99 -static convolution.c -o convolution