#!/usr/bin/env python3

from gg_sdk import GG, GGThunk

test_prog_bin = 'hw_cpp'

def main():
    gg = GG()
    all_thunks = []
    next_thunk = GGThunk(exe=test_prog_bin, outname='thunk.out',
             exe_args=[], args_infiles=False)
    next_thunk.add_infile([])
    all_thunks.append(next_thunk)

    gg.create_thunks(all_thunks)

if __name__ == '__main__':
    main()
