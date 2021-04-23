#!/usr/bin/env python3
import sys
import importlib


def read_args():
    if len(sys.argv) != 2:
        print('usage: ')
        sys.exit(1)

    sys.path.insert(0, '/home/me/5710_gg/gg/tools/python_sdk/examples/ggdsl_engine')

    with open(sys.argv[1], 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line[0] == '#':
                continue
            parts = line.split()
            print(parts)

            #getattr(mod, parts[1])(parts[2], parts[3])
            #getattr(mod, parts[1])()
    
    return parts 

def get_module(part_name):
    mod = importlib.import_module(parts[0])

    return mod
