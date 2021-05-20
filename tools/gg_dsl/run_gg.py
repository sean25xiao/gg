import os
import sys
import time 
sys.path.insert(0, './excamera')
sys.path.insert(0, './general')
sys.path.insert(0, './general/compiling')
from read_args import read_args, get_module
from gg_video import execute_video_processing
from gg_general import execute_general_program
from gg_compiling import compiling


# run_gg video <video_name.avi> 0 4 2 32

def run_gg():
    parts = read_args()
   # mod = get_module(parts[0])
    PATH = os.getenv('GG_DSL_WORK_PATH', default=0)
    if parts[0] != 'run_gg':
       print('Please use run_gg at the beginning')
       sys.exit(1)
    elif parts[1] == 'video':
        #EXCAM_PATH = os.getenv('GG_DSL_EXCAMERA_PATH', default=0) # Get path to excam-static-bin
        if PATH == 0:
            print("Please set up <path-to-excamera-output-file> to 'GG_DSL_WORK_PATH' ")
            sys.exit(1)
        print(PATH)
        execute_video_processing(parts[2], int(parts[3]), int(parts[4]), int(parts[5]), int(parts[6]), int(parts[7]), PATH)
    elif parts[1] == "general":
        if parts[2] == "is_compiled":
            if PATH == 0:
                print("Please set up <the directory for compiling> to 'GG_DSL_WORK_PATH' ")
                sys.exit(1)
            print(PATH)
            compiling(parts[3], parts[4], PATH)

        else: 
            #GENERAL_PATH = os.getenv('GG_DSL_GENERAL_PATH', default=0)
            if PATH == 0:
                print("Please set up <path-to-general-app-output-file> to 'GG_DSL_WORK_PATH' ")
                sys.exit(1)
            print(PATH)
            execute_general_program(parts[2], parts[3], PATH)



if __name__ == '__main__':
    start_time = time.time()
    run_gg()
    print(time.time() - start_time)