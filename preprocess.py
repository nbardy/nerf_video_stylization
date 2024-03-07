import os
import subprocess
import wandb
import modal

# Initialize W&B
wandb.init(project="video_preprocessing", job_type="preprocess")

# Define the Docker image and preprocessing script path
DOCKER_IMAGE = "neuman"
VIDEO_FOLDER_ON_HOST = "/path/to/data_folder"  # Adjust this path
SMPLX_FOLDER_ON_HOST = "/path/to/smplx"  # Adjust this path
PREPROCESS_SCRIPT_PATH = "/neuman/preprocess/gen_run.py"


# Function to run the Docker container and preprocess the video
def preprocess_video(video_url):
    # Download the video to the VIDEO_FOLDER_ON_HOST
    video_path = os.path.join(VIDEO_FOLDER_ON_HOST, "my_video.mov")
    os.system(f"wget {video_url} -O {video_path}")

    # Run Docker container with mounted volumes and preprocess the video
    docker_run_cmd = f"docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=all -ti -v {VIDEO_FOLDER_ON_HOST}:/data -v {SMPLX_FOLDER_ON_HOST}:/neuman/data/smplx --entrypoint bash {DOCKER_IMAGE}"
    preprocess_cmd = f"cd /neuman/preprocess; python {PREPROCESS_SCRIPT_PATH} --video /data/my_video.mov; bash -i ./run.sh"
    final_cmd = f'{docker_run_cmd} -c "{preprocess_cmd}"'
    subprocess.run(final_cmd, shell=True, check=True)

    # Output path
    output_path = os.path.join(video_path, "output")

    # Log the output to W&B
    wandb.log({"preprocessed_video": wandb.Video(output_path)})


# [Change] Added function to log the output directory as an artifact to W&B
# Function to log the output directory as an artifact to W&B
def log_directory_as_artifact(directory_path, artifact_name):
    # Create a new artifact
    artifact = wandb.Artifact(artifact_name, type="preprocessed_data")
    # Add the directory to the artifact
    artifact.add_dir(directory_path)
    # Log the artifact to W&B
    wandb.log_artifact(artifact)


# Define a Modal stub
stub = modal.Stub("gpu_preprocessing")

# Define the image for Modal
gpu_image = modal.Image.git_repo(
    "ml-neuman/preprocess", python_version="3.10"
).pip_install("wandb==0.16.4")


@stub.function(image=gpu_image, gpu=1)
def preprocess_and_log(video_url):
    preprocess_video(video_url)
    # [Change] Updated to log the output directory as an artifact to W&B
    output_path = os.path.join(VIDEO_FOLDER_ON_HOST, "my_video/output")
    # Log the output directory to W&B
    log_directory_as_artifact(output_path, "preprocessed_video_output")


# Example usage
if __name__ == "__main__":
    video_url = "http://example.com/my_video.mov"
    preprocess_and_log(video_url)
