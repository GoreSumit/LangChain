from langchain.chains import SequentialChain
from keys import google_palm_key
from langchain.llms import GooglePalm
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


api_key = google_palm_key


llm = GooglePalm(google_api_key=api_key,temperature=0.7)




prompt_template_name = PromptTemplate(
input_variables =  ['cuisine'],
template = "I want to open a restaurant for {cuisine} food. suggest some fancy names for it."
)
name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")



prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template="suggest some menu items for {restaurant_name}."
    
)

food_items_chain = LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")


chain = SequentialChain(
    chains=[name_chain, food_items_chain],
    input_variables=['cuisine'],
    output_variables=['restaurant_name','menu_items'],
    verbose=True
)
response = chain({'cuisine' : 'Indian'})
