# Note: Comment starts with pound sign
#run_gg video test_1080p.mp4 0 4 2 32 10
#run_gg video drop.avi 0 4 2 32 10 
#run_gg general hw_cpp.cc 10  # run_gg general <input-cpp> <num-jobs>
#run_gg general is_compiled <num_proc> <num_jobs>
#run_gg general is_compiled 2 100

#run_gg imgconv <num-image> <num-jobs>
run_gg imgconv 50 10