from google.adk.agents import Agent
from google.adk.agents import LlmAgent
from question_agent.agent import question_agent, questionInput
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from tools.question import question_tool

import json
from typing import Literal 


root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="orchestrator_agent",
    description="Directly interacts with the user and delegates tasks to specialist agents like a question generator.",
    instruction="""You are a friendly and encouraging CS 135 tutor orchestrator.
Your main job is to understand a student's request and delegate the task to the correct sub-agent from your team.
**DELEGATION RULES:**
1.  Read the user's request.
2.  Review the `description` of each of your available `sub_agents`.
3.  If the user's request matches the capability of a sub-agent, you MUST delegate the task to that agent.
    - If the user asks for a **new question**, wants to **practice**, or wants to **study a topic**, delegate to the `question_agent`.

**RESPONSE FORMATTING:**
- After a sub-agent (like `question_agent`) returns structured data (in JSON), your job is to format that data into a single, FRIENDLY, and CONVERSATIONAL response for the student. Do NOT just output the raw JSON.
""",
    tools=[question_tool]
)
