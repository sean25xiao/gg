import os
import sys
sys.path.insert(0, './excamera')
sys.path.insert(0, './general')
from read_args import read_args, get_module
from gg_video import execute_video_processing
from gg_general import execute_general_program


# run_gg video <video_name.avi> 0 4 2 32

def run_gg():
    parts = read_args()
   # mod = get_module(parts[0])
   
    if parts[0] != 'run_gg':
       print('Please use run_gg at the beginning')
       sys.exit(1)
    elif parts[1] == 'video':
        EXCAM_PATH = os.getenv('GG_DSL_EXCAMERA_PATH', default=0) # Get path to excam-static-bin
        if EXCAM_PATH == 0:
            print("Please set up <path-to-excamera-output-file> to 'GG_DSL_EXCAMERA_PATH' ")
            sys.exit(1)
        print(EXCAM_PATH)
        execute_video_processing(parts[2], int(parts[3]), int(parts[4]), int(parts[5]), int(parts[6]), int(parts[7]), EXCAM_PATH)
    elif parts[1] == "general":
        GENERAL_PATH = os.getenv('GG_DSL_GENERAL_PATH', default=0)
        if GENERAL_PATH == 0:
            print("Please set up <path-to-general-app-output-file> to 'GG_DSL_GENERAL_PATH' ")
            sys.exit(1)
        print(GENERAL_PATH)
        execute_general_program(parts[2], parts[3], GENERAL_PATH)



if __name__ == '__main__':
    run_gg()
