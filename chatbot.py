from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from prompts import ice_cream_assistant_prompt_template

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct',
             temperature=0.7)

llm_chain = ice_cream_assistant_prompt_template | llm

def query_llm(question):
    print(llm_chain.invoke({'question': question}))

while(1):
    ques = input("Enter Your Question :")
    query_llm(ques)




