# Load Testing the cborg Chatbot Portal

This repository contains scripts to load test the cborg chatbot portal by submitting queries to the `lbl/command-r-plus` model simultaneously every 10 minutes. The testing setup uses a Python script to send parallel requests and a Bash script to manage the job submission to a cluster.

## Prerequisites

- Access to the LRC cluster.
- The necessary environment variables set up in `~/.bashrc`:
  - `CBORG_API_KEY`: API key for accessing the cborg chatbot.
  - `SBATCH_ACCOUNT`: Your SLURM account name.
  - `SBATCH_PARTITION`: The SLURM partition to use.
- Conda environment with the required dependencies installed (e.g., OpenAI library).

## Files

- `parallel_chatbot_queries.py`: Python script to send parallel queries to the chatbot.
- `run_parallel_chatbot.sh`: Bash script to submit the job to the cluster.

## Instructions

### 1. Setup Environment Variables

Ensure that the `CBORG_API_KEY`, `SBATCH_ACCOUNT`, and `SBATCH_PARTITION` environment variables are set in your `~/.bashrc` file:

```bash
export CBORG_API_KEY=your_api_key
export SBATCH_ACCOUNT=your_account
export SBATCH_PARTITION=your_partition
```

Reload your `~/.bashrc` to apply the changes:

```bash
source ~/.bashrc
```

### 2. Create and Activate Conda Environment

Create a Conda environment and install the required dependencies:

```bash
conda create -n cborg python=3.8
conda activate cborg
pip install openai
```

### 3. Submit the Job to the Cluster

Use the `sbatch` command to submit the job script to the cluster:

```bash
sbatch run_parallel_chatbot.sh
```

This command will:
- Submit 200 queries to the "lbl/command-r-plus" model simultaneously.
- Run the script 100 times with a 10-minute interval between each run.

### 4. Monitoring Job Output

The output and error logs will be stored in the `./output` directory with filenames in the format `chatbot_queries_<job_id>.out` and `chatbot_queries_<job_id>.err`.

## Script Details

### `parallel_chatbot_queries.py`

This Python script initializes the OpenAI client using the API key from the environment variable and sends a list of predefined questions to the `lbl/command-r-plus` model. The responses are printed to the console.

### `run_parallel_chatbot.sh`

This Bash script sets up the SLURM job parameters and runs the Python script on each node in the cluster. It repeats the execution every 10 minutes for a total of 100 times.

## Notes
- Adjust the SLURM parameters in `run_parallel_chatbot.sh` as needed based on your cluster's configuration and resource availability.
