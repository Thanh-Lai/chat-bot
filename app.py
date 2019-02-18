from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter


interpreter = RasaNLUInterpreter('models/current/nlu')
messages = ["Hi! you can chat in this window. Type 'stop' to end the conversation."]
agent = Agent.load('models/current/dialogue', interpreter=interpreter)


def respond_to_messages(message):
    responses = agent.handle_message(message)
    for r in responses:
        messages.append(r.get("text"))
    return responses

