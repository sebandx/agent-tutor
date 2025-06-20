import json
from typing import Literal

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

from question_agent.agent import question_agent, questionInput


async def question_tool(question_type: str, question_difficulty: Literal["easy","medium","hard"]) -> dict:
    """
    Use this tool when a student asks for a CS practice problem. 
    It calls a specialist agent to generate a structured question and returns a python dictionary. 
    """
    question_agent_runner = Runner(agent=question_agent, session_service=InMemorySessionService(), app_name = "agent_tutor_app")

    input = questionInput(type=question_type, difficulty=question_difficulty).model_dump_json()

    user_content = Content(role='user', parts=[Part(text=input)])

    session_id = "question_generator_session"
    user_id = "internal_tool_user"

    await question_agent_runner.session_service.create_session(
        app_name=question_agent_runner.app_name,
        user_id=user_id,
        session_id=session_id
    )

    async for event in question_agent_runner.run_async(user_id=user_id, session_id=session_id, new_message=user_content):
        if event.is_final_response() and event.content and event.content.parts:
            return json.loads(event.content.parts[0].text)
        
    return {"error": "The question agent did not return a valid response."}


