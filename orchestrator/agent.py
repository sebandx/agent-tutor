from google.adk.agents import Agent
from google.adk.agents import LlmAgent
def get_weather(city: str) -> str:
    city_weather = {"toronto": "rainy", "waterloo": "sunny", "quebec city": "snowy"}
    return city_weather.get(city.lower(), f"Sorry, I don't know the weather of {city}.")


def get_time(city: str) -> str:
    city_time = {"toronto": "1 PM", "waterloo": "2 PM", "quebec city": "3 PM"}
    return city_time.get(city.lower(), f"Sorry, I don't know the time of {city}.")

root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="orchestrator_agent",
    description="Assigns tasks to other AI Agents",
    instruction="""You are an agent that provide information about a city. 
    When a user asks for information about a city:
    1. Use the 'get_weather' tool to find find the weather.
    2. Use the 'get_time' tool to find the 
    3. Respond clearly to the user, stating the weather and time. 
    Example Query: "Give me information about Toronto?"
    Example Response: "The weather in Toronto is rainy, the time in Toronto is 1 PM."
""",
    tools=[get_time,get_weather]
)


