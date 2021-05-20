import os

def compiling(num_proc, num_jobs, work_path):
    force_lambda =  './general/compiling/run_compiling.sh {} {}'
    force_lambda_cmd = force_lambda.format(num_proc, num_jobs)
    os.system(force_lambda_cmd)
    os.system('pwd')