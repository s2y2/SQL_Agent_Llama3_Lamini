# SQL Agent using Llama 3 and Lamini

## Objective

Creation of SQL Agent using prompt engineering and fine tuning (Meta-Llama-3-8B-Instruct and Lamini). 

## Potential Use Cases + Advantages of using a SQL Agent

- Allows a team to create SQL using natural language, saving time on SQL creation from scratch
- Fewer questions from team re SQL creation -> frees up Data team's time
- Could set-up pipeline to run SQL against database to allow user's natural language queries to bring back the data itself
- Potential to fine-tune towards a specific team's usage eg board level questions, marketing team's questions 

## Model

Meta-Llama-3-8B-Instruct 

Pretrained and instruction tuned generative text model (LLM). The Llama 3 instruction tuned models are optimized for dialogue use cases. They have undergone supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align with human preferences for helpfulness and safety.

## Platform

The Lamini Platform is enterprise-focused and is for building and deploying custom Large Language Models (LLMs). It integrates model refinement, deployment and inference (https://www.lamini.ai/product)

## Usage

- Create SQLite database using data of choice (see *Raw data* for this project's data)
- Create user-generated questions and SQL answers (see test-set.jsonl)
- Set-up Lamini API Key (https://docs.lamini.ai/authenticate/) and add to .env file
- Install required packages: see Text_to_SQL_Agent.ipynb (1st 2 cells)
- Create/update .py files in util directory and modify as required

## Raw data

SQLite database SpotifyData.db created from Top100MostStreamed.csv. CSV download from [Kaggle](https://www.kaggle.com/datasets/pavan9065/top-100-most-streamed-songs-on-spotify).

## Method

- Evaluation of LLM-generated SQL against user-generated SQL. Iteration to improve metrics after prompt-engineering and chain of thought (CoT) prompting
- Creation of training data ie increased volume of SQL and question pairs (for LLM fine-tuning), using LLM 
- LLM fine-tuning with larger dataset using Lamini Memory Tuning (a fine-tuning method that optimises for zero error on specific facts by tuning millions of LoRA adapters and selecting them at inference time) https://www.lamini.ai/blog/lamini-memory-tuning 
- Evaluation of fine-tuned model

## Results of iterations

<br>
<table>
  <tr>
    <th>Iteration</th>
    <th>Valid SQL Syntax (%)</th> 
    <th>Correct SQL Query (%)</th> 
  </tr>
  <tr>
    <td>Original results with basic schema</td>
    <td>50.0</td> 
    <td>33.3 </td> 
  </tr>
  <tr>
    <td>Prompt engineering: additions to schema</td>
    <td>83.3</td> 
    <td>50.0</td> 
  </tr>
  <tr>
    <td>Prompt engineering: additions to system prompt</td>
    <td>83.3</td> 
    <td>66.7</td> 
  </tr>
    <tr>
    <td>After fine tuning with (LLM-created) larger dataset</td>
    <td>100.0</td> 
    <td>100.0</td> 
  </tr>
  </tr>
</table>
<br>


## References and tools

- https://www.kaggle.com/datasets/pavan9065/top-100-most-streamed-songs-on-spotify
- https://www.lamini.ai/blog/meta-lamini-llama3-sql
- https://learn.deeplearning.ai/courses/improving-accuracy-of-llm-applications/lesson/1/introduction
- https://www.llama.com/docs/model-cards-and-prompt-formats/meta-llama-3/#meta-llama-3-instruct
- https://www.geeksforgeeks.org/import-a-csv-file-into-an-sqlite-table/?ref=header_outind
- https://github.com/lamini-ai/lamini-examples/tree/main
- https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
- https://markdownlivepreview.com/
- https://www.lamini.ai/blog/lamini-memory-tuning


## Next steps

- Increase evaluation set size by including more difficult SQL queries and a greater range of SQL queries
- Focus on the specific use cases: which team(/s) is likely to be using the service and what are examples of questions that they would be asking
- Increase size of generated questions and SQL answers (filtering out any poor results). Further fine tuning based on the larger set of data
- Reflection prompting (feeding back to the LLM: the incorrect SQL and associated error). Attempt (before fine-tuning) during this project saw no improvement in output
