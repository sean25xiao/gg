#!/bin/bash -e

start_time="$(date -u +%s)"

# Clear previous work
cd $GG_DSL_EXCAMERA_PATH
rm -rf *.state *.ivf *.y4m *.txt *.mgc .gg output.avi

# Prepare the video
ffmpeg -i ~/Desktop/ggdsl_excam_test/test_1080p.mp4 -pix_fmt yuv420p input.y4m
ffmpeg -i input.y4m -f segment -segment_time 1 -pix_fmt yuv420p 0000%4d.y4m

# Create Thunk
cd /home/me/5710_gg/gg/tools/gg_dsl/excamera
python3 excam_ex.py 0 16 2 32 $GG_DSL_EXCAMERA_PATH
cd $GG_DSL_EXCAMERA_PATH

# Run
printf "4. Run video processing jobs\n"
gg force --jobs=10 --engine=lambda *.ivf

printf "5. Build output.avi\n"
ls *-vpxenc.ivf | while read each; do echo "file '$each'" >> mylist.txt; done
ffmpeg -f concat -i mylist.txt -codec copy output.avi

printf "6. Result:\n"
file output.avi

end_time="$(date -u +%s)"
elapsed="$(($end_time-$start_time))"
echo "$elapsed"

