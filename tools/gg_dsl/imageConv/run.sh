#!/bin/bash -e

USAGE="$0 <JOBS-COUNT>"

JOBS_COUNT=${1?$USAGE}
#DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
#cd $DIR/../
cd $GG_DSL_WORK_PATH

start_time="$(date -u +%s)"
gg force --jobs=$JOBS_COUNT --engine=lambda *.out

end_time="$(date -u +%s)"
elapsed="$(($end_time-$start_time))"
echo "$elapsed"