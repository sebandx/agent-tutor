from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

from tools.racket_executor import run_code

class GradingInput(BaseModel):
    """Input schema for the grading agent."""
    code_to_run: str = Field(description="The complete Racket code submitted by the user.")

grading_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="grading_agent",
    description="A specialist agent that runs a piece of Racket code and returns the result.",
    instruction="""You are a simple code execution service.
    You will receive a JSON object containing a user's Racket code.
    Your ONLY job is to take that code and immediately pass it to the `run_code` tool.
    Do not add any conversation. The tool's output is your final output.
    """,
    input_schema=GradingInput,
    tools=[run_code]
)

root_agent = grading_agent