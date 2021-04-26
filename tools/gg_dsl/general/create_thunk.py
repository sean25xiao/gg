#!/usr/bin/env python3

from gg_sdk import GG, GGThunk
import sys
import os

test_prog_bin = 'a'

def main():
    gg = GG()
    all_thunks = []
    next_thunk = GGThunk(exe=test_prog_bin, outname='thunk.out',
             exe_args=[], args_infiles=False)
    next_thunk.add_infile([])
    all_thunks.append(next_thunk)

    gg.create_thunks(all_thunks)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: create_thunk.py <bin-path>")
        sys.exit(1)

    output_path = sys.argv[1]
    os.chdir(output_path)

    main()
