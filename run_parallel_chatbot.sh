#!/bin/bash
#SBATCH --job-name=parallel_chatbot_queries
# Account:
#SBATCH --account=$SBATCH_ACCOUNT
# Partition:
#SBATCH --partition=$SBATCH_PARTITION
#SBATCH --nodes=10
#SBATCH --ntasks-per-node=1
#SBATCH --time=10:00:00
#SBATCH --output=./output/chatbot_queries_%j.out
#SBATCH --error=./output/chatbot_queries_%j.err

# Ensure the CBORG_API_KEY environment variable is set in ~/.bashrc

source ~/.bashrc
conda activate cborg

run_script() {
    python ./parallel_chatbot_queries.py
}
export -f run_script

# Loop to run the script 100 times with a 10-minute sleep between each run
echo "# Run the script on each node"
echo $(date)
for i in {1..100}
do
    srun --nodes=10 --ntasks=10 bash -c 'run_script'
    if [ $i -ne 100 ]; then
        sleep 600  # 10 minutes
    fi
done
echo $(date)
echo "# Done!"
