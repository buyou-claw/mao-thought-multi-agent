# src/mao_agent/agents/united_front.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="united_front",
    specialty="统一战线",
    description="专精利益格局、联盟策略分析"
)

SYSTEM_PROMPT = """你是一位专精统一战线的思想者，擅长运用毛泽东《统一战线》的方法分析问题。

你的职责：
1. 分清敌我友
2. 识别共同利益点
3. 保持相对独立性
4. 根据矛盾变化调整策略
"""

class UnitedFrontAgent(BaseSpecialistAgent):
    def __init__(self, knowledge_loader=None):
        super().__init__(AGENT_CONFIG, knowledge_loader)

    def get_system_prompt(self) -> str:
        knowledge = self.load_knowledge()
        return f"{SYSTEM_PROMPT}\n\n## 知识库\n{knowledge}"

    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        return f"""## 统一战线分析

针对问题：{task}

### 敌我友分析
[各方定位待识别]

### 共同利益点
[利益交汇点待发现]

### 独立性保持
[自主性策略待设计]

### 动态调整预案
[调整策略待规划]"""