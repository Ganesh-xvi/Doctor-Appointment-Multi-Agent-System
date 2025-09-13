from fastapi import FastAPI
from pydantic import BaseModel
from toolkit.toolkits import *
from utils.llms import LLMModel
from agent import DoctorAppointmentAgent
from langchain_core.messages import AIMessage

from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor

llm_model = LLMModel()
llm       = llm_model.get_model()

availability_agent = create_react_agent(model=llm, tools=[check_availability_by_doctor,check_availability_by_specialization], name ="booking_agent")

booking_agent      = create_react_agent(model=llm, tools=[set_appointment,cancel_appointment,reschedule_appointment], name="availability_agent")

app        = FastAPI()
agent      = DoctorAppointmentAgent(llm, booking_agent, availability_agent)
supervisor = agent.create_supervisor()

class UserQuery(BaseModel):
    messages: str

@app.post("/execute")
def execute_agent(user_input: UserQuery):
    response = supervisor.invoke({"messages": [{"role": "user", "content": user_input.messages}]},config={"recursion_limit": 20})

    ai_messages = [msg for msg in response['messages'] if isinstance(msg, AIMessage) and msg.content.strip() != ""]

    if ai_messages:
        return {"last_message": ai_messages[-1].content}
    else:
        return {"last_message": "No response generated."}
