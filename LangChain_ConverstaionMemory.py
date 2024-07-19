from langchain.agents import AgentType, initialize_agent, load_tools
from keys import google_palm_key
from langchain.llms import GooglePalm
from langchain.memory import ConversationBufferMemory,ConversationBufferWindowMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


api_key = google_palm_key
llm = GooglePalm(google_api_key=api_key, temperature=0.7)

prompt_template_name = PromptTemplate(
input_variables =  ['cuisine'],
template = "I want to open a restaurant for {cuisine} food. suggest some fancy names for it."
)


memory = ConversationBufferMemory()

chain = LLMChain(llm=llm,prompt=prompt_template_name,memory=memory)

# name = chain.run("Lebanese")
# print(name)

# name = chain.run("Indian")
# print(name)

#print(chain.memory.buffer) #will remain all previous history and give all result sets charging tokens for each result set


#limit the history to last 5 results or conversations

from langchain.chains import ConversationChain
# convo = ConversationChain(llm=llm)
# convo.run("whats 5+5?")
# convo.run("who is the president of india?")
# convo.run("what is the distance between earth and mars?")
# convo.run("how many kilometer is that?")
# print(convo.memory.buffer)


# start limit the history to last 5 results or conversations
memory = ConversationBufferWindowMemory(k=1)

convo = ConversationChain(
    llm = llm,
    memory = memory
)
convo.run("whats 5+5?")
convo.run("who is the president of india?")
convo.run("what is the distance between earth and mars?")
convo.run("how many kilometer is that?")
print(convo.memory.buffer)