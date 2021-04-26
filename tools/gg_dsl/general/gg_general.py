import os

def execute_general_program(file_name, num_jobs, output_path):
    clear_cmd = './general/clear.sh'
    os.system(clear_cmd)

    compiling = './general/compile_cmd.sh {}'
    compiling_cmd = compiling.format(file_name)
    os.system(compiling_cmd)
    
    thk_create = 'python3 ./general/create_thunk.py {}'
    thk_create_cmd = thk_create.format(output_path)
    os.system(thk_create_cmd)

    # Push to Lambda
    force_lambda = './general/run.sh {}'
    force_lambda_cmd = force_lambda.format(num_jobs)
    os.system(force_lambda_cmd)