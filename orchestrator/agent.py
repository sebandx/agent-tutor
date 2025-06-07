from google.adk.agents import Agent
from google.adk.agents import LlmAgent
from question_agent.agent import question_agent

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
- After a sub-agent (like `question_agent`) returns structured data (like JSON), your final job is to format that data into a single, friendly, and conversational response for the student. Do not just output the raw JSON.

""",
    sub_agents=[question_agent]
)

# next steps 
# student is give a question by a question agent 
# student can answer question 
# code is given to grading agent 
# grading agent either returns code, or provides code to debugging agent 
# debugging agent then returns coded back to grading agent 
# grading agent then gives student data to learning agent
# grading agent also returns to orchestration agent 