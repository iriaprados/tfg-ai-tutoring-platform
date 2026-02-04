# Agent for planning the tutoring strategy based on student level determinated by EvaluatorAgent

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class PlannerAgent:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0)

        self.prompt = ChatPromptTemplate.from_template(
            """
            El alumno tiene nivel {level}.
            Decide la estrategia pedagógica a seguir.

            Responde SOLO con una de estas opciones:
            - explicacion_basica
            - explicacion_detallada
            - ejemplo_practico
            """
        )

    def plan(self, level: str) -> str:
        response = self.llm(
            self.prompt.format_messages(level=level)
        )
        return response.content.lower()
