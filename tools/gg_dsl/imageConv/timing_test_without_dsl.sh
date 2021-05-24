#!/bin/bash -e

start_time="$(date -u +%s)"

cd $GG_DSL_WORK_PATH

rm -rf *.out .gg

cd /home/me/final/gg/tools/gg_dsl

python3 ./imageConv/create_thunk.py $GG_DSL_WORK_PATH 5

cd $GG_DSL_WORK_PATH

gg force --jobs=100 --engine=lambda *.out

end_time="$(date -u +%s)"
elapsed="$(($end_time-$start_time))"
echo "$elapsed"