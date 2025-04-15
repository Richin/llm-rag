from langchain_community.chat_models import ChatOllama
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0.3)

def ask_deepseek(prompt):
    messages = [
        SystemMessage(content="You are a knowledgeable clinical assistant."),
        HumanMessage(content=prompt)
    ]
    return llm(messages).content
