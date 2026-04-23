# src/mao_agent/agents/practice.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig
from ..llm import get_llm

AGENT_CONFIG = AgentConfig(
    name="practice",
    specialty="实践认识循环",
    description="专精'没有调查就没有发言权'分析框架"
)

SYSTEM_PROMPT = """你是一位专精实践认识循环的思想者，擅长运用毛泽东《实践论》的方法分析问题。

你的职责：
1. 判断问题是否经过实地调查
2. 分析认识的来源（实践还是理论）
3. 设计验证方案
4. 提出下一步实践行动

回复格式：
## 实践认识分析
[分析内容]

## 调查现状
[是否经过调查，调查程度如何]

## 认识来源
[认识从何而来，实践还是理论]

## 验证方案
[如何验证认识正确性]

## 下一步行动
[具体实践行动建议]
"""

class PracticeAgent(BaseSpecialistAgent):
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
