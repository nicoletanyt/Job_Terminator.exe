# IMPORTANT: pip3 install openai python-dotenv langchain gradio pandas json

import openai
import os
from dotenv import load_dotenv, find_dotenv
from langchain.evaluation import load_evaluator
from langchain.llms import OpenAI
import gradio as gr

import pandas as pd
import json
import warnings

# don't show warnings 
warnings.filterwarnings("ignore")

# load and read data.json

with open("data.json") as f:
  data = json.load(f)

# print(data)

# load the env.txt that contains the OPENAI key

load_dotenv('env.txt')
openai_api_key = os.getenv('OPENAI_API_KEY')

print(openai_api_key)

llm = OpenAI(
    openai_api_key=openai_api_key,
    model ='gpt-3.5-turbo-instruct'
)

#  evaluator = load_evaluator("trajectory", llm=llm) 

custom_criterion = {
    "grammar": "Does the output follow proper grammar, spelling, and pronunciation rules?",
    "coherence": "Does the output have a coherent flow of ideas?",
    "vocabulary":"Does the output use a robust dictionary of vocabulary?",
    "accuracy":"Does the output fully address the task?"
}

def return_feedback():
  return ""

def predict(message, history):

    output = str(return_feedback(message)).replace("\n", "<br/>")
    return output

demo = gr.ChatInterface(
    predict,
    title = f'Olevel English Essay Grader'
)
