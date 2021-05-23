#!/bin/bash -e

USAGE="$0 <JOBS-COUNT>"

JOBS_COUNT=${1?$USAGE}
#DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
#cd $DIR/../
cd $GG_DSL_WORK_PATH

gg force --jobs=$JOBS_COUNT --engine=lambda *.out