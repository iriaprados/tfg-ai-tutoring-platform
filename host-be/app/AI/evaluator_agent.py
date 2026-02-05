# Agent for evaluating student understanding level

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class EvaluatorAgent:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0)

        self.prompt = ChatPromptTemplate.from_template(
            """
            Analiza el nivel de comprensión del alumno basándote en su pregunta.
            
            Pregunta del alumno:
            {message}
            
            Responde SOLO con uno de estos niveles:
            - basico
            - intermedio
            - avanzado
            """
        )

    def evaluate(self, message: str) -> str:
        response = self.llm(
            self.prompt.format_messages(message=message)
        )
        return response.content.lower()
