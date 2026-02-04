# Agent for the analysis and tutoring of students based on their profiles

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class EvaluatorAgent:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0)

        self.prompt = ChatPromptTemplate.from_template(
            # Poner aqui el mensaje del alumno 
        )

    def evaluate(self, message: str) -> str:
        response = self.llm(
            self.prompt.format_messages(message=message)
        )
        return response.content.lower()
