#!/bin/bash -e

USAGE="$0 <JOBS-COUNT>"

JOBS_COUNT=${1?$USAGE}
#DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
#cd $DIR/../
cd $GG_DSL_GENERAL_PATH


printf "1. Run the General C++ jobs\n"
gg force --jobs=$JOBS_COUNT --engine=lambda *.out

printf "2. Result:\n"
cat *.out
