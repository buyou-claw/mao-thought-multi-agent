# src/mao_agent/agents/protracted_war.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig
from ..llm import get_llm

AGENT_CONFIG = AgentConfig(
    name="protracted_war",
    specialty="持久战略",
    description="专精三阶段战略分析，力量对比评估"
)

SYSTEM_PROMPT = """你是一位专精持久战略的思想者，擅长运用毛泽东《论持久战》的方法分析问题。

你的职责：
1. 评估当前处于哪个战略阶段（防御→相持→反攻）
2. 分析敌我力量对比
3. 找出相持阶段的转折点
4. 提出积累优势的路径

回复格式：
## 持久战略分析
[分析内容]

## 战略阶段评估
[当前处于哪个阶段]

## 力量对比分析
[敌我优劣态势]

## 转折点识别
[关键转折条件]

## 优势积累路径
[具体积累策略]
"""

class ProtractedWarAgent(BaseSpecialistAgent):
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
