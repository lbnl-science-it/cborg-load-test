import openai
import os
import concurrent.futures

# Initialize OpenAI client
client = openai.OpenAI(
    api_key=os.environ.get('CBORG_API_KEY'),
    base_url="https://api.cborg.lbl.gov"
)


# List of questions
questions = [
    "Simulate the N-body problem for a system of 100 celestial bodies. Calculate their positions and velocities over time considering gravitational interactions. Present the results with detailed visualizations and explanations of the methods used.",
    "Train a deep neural network to classify images from the CIFAR-10 dataset. Compare the performance of different architectures (e.g., CNN, ResNet, EfficientNet) and provide a detailed evaluation report, including model architectures, training processes, and performance metrics.",
    "Implement and train a transformer-based language model (e.g., BERT, GPT) on a large text corpus. Evaluate its performance on a specific NLP task such as text classification or summarization, and provide detailed training logs, evaluation metrics, and example outputs.",
    "Develop a reinforcement learning agent to play and master the game of Go. Describe the training process, computational resources used, and the agent's performance against human players, including detailed training logs and performance evaluations.",
    "Analyze a large dataset (e.g., terabytes of web traffic logs) to identify patterns and trends. Use distributed computing frameworks like Apache Spark or Hadoop. Provide detailed visualizations and insights, along with the code and methodology used for the analysis.",
    "Conduct a genome-wide association study (GWAS) to identify genetic variants associated with a specific disease. Use a large dataset of genomic sequences and phenotype data. Report the significant findings, including detailed statistical analyses and biological interpretations.",
    "Develop a high-resolution climate model to simulate the impact of various factors (e.g., greenhouse gas emissions, deforestation) on global temperature changes over the next century. Provide detailed visualizations and analysis, along with the model's assumptions and limitations.",
    "Simulate the spread of a contagious disease in a large population using agent-based modeling. Evaluate the effects of different intervention strategies on the spread and provide recommendations, including detailed simulation results and policy implications.",
    "Create a detailed simulation of a stock market using historical data. Implement various trading algorithms and evaluate their performance under different market conditions. Present a comprehensive report on the findings, including detailed backtesting results and risk assessments.",
    "Develop an image segmentation algorithm using deep learning. Train and evaluate the model on a large image dataset, and provide detailed results, including segmentation accuracy, visualizations of segmented images, and performance metrics.",
    "Implement a speech recognition system using deep learning. Train the model on a large audio dataset and evaluate its performance on different types of speech. Provide detailed results, including transcriptions, accuracy metrics, and error analysis.",
    "Develop a recommendation system using collaborative filtering and content-based filtering techniques. Train and evaluate the system on a large dataset, and provide detailed results, including recommendation accuracy, user satisfaction metrics, and examples of recommendations.",
    "Solve a complex optimization problem using genetic algorithms. Describe the problem, implement the algorithm, and provide detailed results, including the solution process, convergence analysis, and performance metrics.",
    "Develop a robotic path planning algorithm using reinforcement learning. Train the robot to navigate through complex environments and avoid obstacles. Provide detailed results, including training logs, path visualizations, and performance evaluations.",
    "Simulate a quantum algorithm (e.g., Shor's algorithm for integer factorization) using a quantum computing framework. Provide detailed results, including the implementation process, simulation results, and performance analysis.",
    "Analyze a large social network graph to identify key influencers and community structures. Use graph algorithms and machine learning techniques, and provide detailed results, including visualizations, metrics, and interpretations.",
    "Develop an object detection model using deep learning. Train and evaluate the model on a large image dataset, and provide detailed results, including detection accuracy, visualizations of detected objects, and performance metrics.",
    "Develop a text generation model using a transformer architecture. Train the model on a large text corpus and evaluate its ability to generate coherent and contextually relevant text. Provide detailed results, including generated text samples, evaluation metrics, and error analysis.",
    "Analyze a large RNA sequencing dataset to identify differentially expressed genes. Use statistical and machine learning methods, and provide detailed results, including the analysis process, identified genes, and biological interpretations."
]

# send a question to the chatbot and get the response
def get_response(question):
    response = client.chat.completions.create(
        model="lbl/command-r-plus",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.0
    )
    return response

# send requests in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=len(questions)) as executor:
    future_to_question = {executor.submit(get_response, q): q for q in questions}
    for future in concurrent.futures.as_completed(future_to_question):
        question = future_to_question[future]
        try:
            data = future.result()
            print(f"Question: {question}\nResponse: {data}\n")
        except Exception as exc:
            print(f"Question: {question} generated an exception: {exc}")
