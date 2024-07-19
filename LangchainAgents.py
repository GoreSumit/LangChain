from langchain.agents import AgentType, initialize_agent, load_tools
from keys import google_palm_key
from langchain.llms import GooglePalm

api_key = google_palm_key
llm = GooglePalm(google_api_key=api_key, temperature=0.7)

# Load tools using load_tools function
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True #discloses the thinking chain on llm
)

response = agent.run("When was Elon Musk born and what is his age now in 2024?")
print(response)
