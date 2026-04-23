# src/mao_agent/agents/rural_strategy.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig
from ..llm import get_llm

AGENT_CONFIG = AgentConfig(
    name="rural_strategy",
    specialty="农村包围城市",
    description="专精边缘突破、市场进入策略分析"
)

SYSTEM_PROMPT = """你是一位专精农村包围城市战略的思想者，擅长运用毛泽东《星星之火，可以燎原》的方法分析问题。

你的职责：
1. 识别边缘市场/领域（敌人的薄弱环节）
2. 规划根据地建立路径
3. 设计连点成片的扩展策略
4. 判断包围中心的时机

回复格式：
## 农村包围城市分析
[分析内容]

## 边缘市场识别
[在哪里建立根据地]

## 根据地建立
[如何扎根]

## 连点成片路径
[如何扩展]

## 包围中心时机
[何时发起总攻]
"""

class RuralStrategyAgent(BaseSpecialistAgent):
    def __init__(self, knowledge_loader=None):
        super().__init__(AGENT_CONFIG, knowledge_loader)
        self.llm = get_llm()

    def get_system_prompt(self) -> str:
        knowledge = self.load_knowledge()
        return f"{SYSTEM_PROMPT}\n\n## 知识库\n{knowledge}"

    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        prompt = f"{self.get_system_prompt()}\n\n## 待分析问题\n{task}"
        response = self.llm.invoke(prompt)
        return response.content
