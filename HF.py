from langchain.llms import GooglePalm
from keys import google_palm_key

api_key = google_palm_key

llm = GooglePalm(google_api_key=api_key,temperature=0.7)

name = llm("Names for Indian restaurant.")
print(name)