from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Form
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from langchain import OpenAI
from langchain.chains import ConversationChain

load_dotenv()

app = FastAPI()
origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.websocket("/api/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    llm = OpenAI(temperature=0.7)
    chain = ConversationChain(llm=llm, verbose=True)
    while (True):
        try:
            msg = await websocket.receive_text()
            reply = chain.run(input=msg)
            await websocket.send_text(reply)
        except WebSocketDisconnect:
            break

@app.get('/')
async def get():
    return "Hello World!"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=9000, reload=True)
