#!/bin/bash -e

# $1 is num_proc, $2 is num_jobs, $3 is path
start_time="$(date -u +%s)"

JOBS_PROC=${1?$USAGE}
JOBS_COUNT=${2?$USAGE}

export GG_MODELPATH=/home/me/5710_gg/gg/src/models/wrappers/
cd /home/me/mosh/
make clean
gg init
gg infer make -j$JOBS_PROC     # creates the thunks
#gg force --jobs $2 --engine lambda src/frontend/mosh-server
gg force --jobs $JOBS_COUNT --engine lambda /home/me/mosh/src/frontend/mosh-server

end_time="$(date -u +%s)"
elapsed="$(($end_time-$start_time))"
echo "$elapsed"