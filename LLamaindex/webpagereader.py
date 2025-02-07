from llama_index.readers import SimpleWebPageReader
from llama_index import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv


load_dotenv()

def main(url: str)-> None:
    document=SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index=VectorStoreIndex.from_documents(documents=document)
    query_engine=index.as_query_engine()
    response=query_engine.query("What is the history of the generative ai?")
    print(response)

if __name__=="__main__":
    main(url="https://medium.com/technology-nineleaps/what-is-generative-ai-a-comprehensive-guide-96485365bd20#:~:text=Generative%20AI%20refers%20to%20a,text%2C%20music%2C%20and%20more.")
