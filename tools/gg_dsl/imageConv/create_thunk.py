#!/usr/bin/env python3

from gg_sdk import GG, GGThunk
import sys
import math
import os

CONV = 'convolution $GG_DSL_WORK_PATH {input_file} {output_file}'

def bname(i):
    return "image{}".format(i)

def make_command(cmd):
    return "\t{}".format(cmd)

def main(num_image):
    gg = GG()
    all_thunks = []

    for i in range(0, num_image):
        name = bname(i)

        conv = make_command(CONV.format(input_file="%s.txt" % name, output_file="%s.out" % name))
        conv_split = conv.split()
        next_thunk = GGThunk(exe=conv_split[0], outname="%s.out" % name,
                        exe_args=conv_split[1:], args_infiles=False)
        next_thunk.add_infile(name + '.txt')
        all_thunks.append(next_thunk)

    gg.create_thunks(all_thunks)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: create_thunk.py <path-to-work-directory> <num-image>")
        sys.exit(1)

    output_path = sys.argv[1]
    num_image = int(sys.argv[2])

    copy_bin = 'cp ./imageConv/convolution {}'
    copy_bin_cmd = copy_bin.format(output_path)
    #print(copy_bin_cmd)
    os.system(copy_bin_cmd)

    
    os.chdir(output_path)

    main(num_image)