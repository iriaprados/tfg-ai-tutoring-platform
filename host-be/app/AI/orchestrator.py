# Unified the agents on a multi-agent system 

from app.AI.evaluator_agent import EvaluatorAgent
from app.AI.planner_agent import PlannerAgent
from app.AI.tutor_agent import TutorAgent

class ITFOrchestrator:
    def __init__(self):
        self.evaluator = EvaluatorAgent()
        self.planner = PlannerAgent()
        self.tutor = TutorAgent()

    def process(self, message: str):
        level = self.evaluator.evaluate(message)
        strategy = self.planner.plan(level)
        response = self.tutor.explain(message, strategy)

        return {
            "level": level,
            "strategy": strategy,
            "response": response
        }
