# Connects to the database and handles chat-related operations

from app.AI.orchestrator import ITFOrchestrator

orchestrator = ITFOrchestrator() # Orchestrator from the multi-agent system 


def process_message(message: str):
    result = orchestrator.process(message)
    return result["response"]

