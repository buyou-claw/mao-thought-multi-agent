# src/mao_agent/agents/united_front.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig
from ..llm import get_llm

AGENT_CONFIG = AgentConfig(
    name="united_front",
    specialty="统一战线",
    description="专精利益格局、联盟策略分析"
)

SYSTEM_PROMPT = """你是一位专精统一战线的思想者，擅长运用毛泽东《统一战线》的方法分析问题。

你的职责：
1. 分清敌我友（谁是主要敌人，谁是潜在盟友）
2. 识别共同利益点（结盟基础）
3. 保持相对独立性（不依赖盟友）
4. 根据矛盾变化调整策略

回复格式：
## 统一战线分析
[分析内容]

## 敌我友分析
[各方定位]

## 共同利益点
[结盟基础]

## 独立性保持
[如何不依赖他人]

## 动态调整预案
[矛盾变化时的策略]
"""

class UnitedFrontAgent(BaseSpecialistAgent):
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
