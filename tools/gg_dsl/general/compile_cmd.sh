#!/bin/bash -e

USAGE="$0 <CPP-PROGRAM-PATH>"

cd $GG_DSL_GENERAL_PATH

if [ -z $1 ]
then
    echo "Please input C++ Program"
    exit -1
else
    cd $GG_DSL_GENERAL_PATH
    pwd
    g++ --static $1 -o a
fi