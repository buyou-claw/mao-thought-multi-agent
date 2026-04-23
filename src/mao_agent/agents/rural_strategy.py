# src/mao_agent/agents/rural_strategy.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="rural_strategy",
    specialty="农村包围城市",
    description="专精边缘突破、市场进入策略分析"
)

SYSTEM_PROMPT = """你是一位专精农村包围城市战略的思想者，擅长运用毛泽东《星星之火，可以燎原》的方法分析问题。

你的职责：
1. 识别边缘市场/领域
2. 规划根据地建立路径
3. 设计连点成片的策略
4. 判断包围中心的时机
"""

class RuralStrategyAgent(BaseSpecialistAgent):
    def __init__(self, knowledge_loader=None):
        super().__init__(AGENT_CONFIG, knowledge_loader)

    def get_system_prompt(self) -> str:
        knowledge = self.load_knowledge()
        return f"{SYSTEM_PROMPT}\n\n## 知识库\n{knowledge}"

    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        return f"""## 农村包围城市分析

针对问题：{task}

### 边缘市场识别
[边缘领域待识别]

### 根据地建立
[稳固立足点待规划]

### 连点成片路径
[扩展路径待设计]

### 包围中心时机
[关键时机待判断]"""