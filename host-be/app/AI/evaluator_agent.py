# Agent for tutoring students based on a given strategy

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class TutorAgent:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.7)

        self.prompt = ChatPromptTemplate.from_template(
            """
            Actúa como un tutor paciente y claro.
            Estrategia: {strategy}

            Pregunta del alumno:
            {message}
            """
        )

    def explain(self, message: str, strategy: str) -> str:
        response = self.llm(
            self.prompt.format_messages(
                message=message,
                strategy=strategy
            )
        )
        return response.content
