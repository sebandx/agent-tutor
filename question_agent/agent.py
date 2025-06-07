import json
from google.adk.agents import Agent
from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field
from typing import Literal 

APP_NAME = "agent_comparison_app"
MODEL_NAME = "gemini-2.0-flash"

class questionInput(BaseModel):
    difficulty: Literal["easy", "medium", "hard"] = Field(description = "The difficulty of the question.")
    type: str = Field(description = "The type of question. Some examples of question types are recursion, graph theory, and dynamic programming.")

class questionOutput(BaseModel): 
    question_text: str = Field(description = "An explaination about the programming problem.")
    question_example_input: str = Field(description = "An expample for the input of the question.")
    question_example_output: str = Field(description = "An example for the expected output for the provided input above.")
    question_example_explaination: str = Field(description = "An explaination for why the program provides that output for that given input.")

# rename to question_agent, only name it to root_agent to use when testing in adk web
root_agent = LlmAgent(
    model = MODEL_NAME,
    name = "question_agent",
    description = "generates a CS 135 question as a JSON object",
    instruction=f"""
    You are a Computer Science course assistant for an introductory Racket course.
    Your task is to generate a single, complete programming problem based on the user's request.

    The user will provide the topic and difficulty in a JSON object.
    
    You MUST respond with ONLY a valid JSON object that conforms to the following schema.
    Do not include any other text, conversation, or markdown formatting like ```json.
    
    The schema to follow is:
    {json.dumps(questionOutput.model_json_schema(), indent=2)}
    """,
    input_schema = questionInput,
    output_schema = questionOutput,
    tools = [],
    output_key="structured_question_json"
)