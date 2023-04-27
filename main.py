from langchain import OpenAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    llm = OpenAI(temperature=0.7)
    chain = ConversationChain(llm=llm)
    while True:
        user_input = input("Human: ")
        user_output = chain.run(input=user_input)
        print(f"AI Bot:{user_output}")
