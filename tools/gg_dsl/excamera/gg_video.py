import os

# run_gg video <video_name.avi> <start> <end> <batch-size> <cq-level> <num_jobs>

def execute_video_processing(video_name, start, end, batch_size, cq_level, num_jobs, output_path):
    # Clear previous result
    clear_cmd = './excamera/clear.sh'
    os.system(clear_cmd)

    # Prepare the video into .y4m file
    prepare_video = './excamera/prepare.sh {}'
    prepare_video_cmd = prepare_video.format(output_path+video_name)
    os.system(prepare_video_cmd)

    # Create Thunk
    thk_create = 'python3 ./excamera/excam_ex.py {} {} {} {} {}'
    thk_create_cmd = thk_create.format(start, end, batch_size, cq_level, output_path)
    os.system(thk_create_cmd)

    # Push to Lambda
    force_lambda = './excamera/run.sh {}'
    force_lambda_cmd = force_lambda.format(num_jobs)
    os.system(force_lambda_cmd)
