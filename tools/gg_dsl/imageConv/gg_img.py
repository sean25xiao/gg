import os

# run_gg video <video_name.avi> <start> <end> <batch-size> <cq-level> <num_jobs>

def execute_image_convolution(num_image, num_jobs, output_path):
    # Clear previous result
    clear_cmd = './imageConv/clear.sh'
    os.system(clear_cmd)

    # Compile Convolutoin.c
    prepare_cmd = './imageConv/prepare.sh'
    os.system(prepare_cmd)

    # Create Thunk
    thk_create = 'python3 ./imageConv/create_thunk.py {} {}'
    thk_create_cmd = thk_create.format(output_path, num_image)
    os.system(thk_create_cmd)

    # Push to Lambda
    force_lambda = './imageConv/run.sh {}'
    force_lambda_cmd = force_lambda.format(num_jobs)
    os.system(force_lambda_cmd)
