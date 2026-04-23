# src/mao_agent/agents/mass_line.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig
from ..llm import get_llm

AGENT_CONFIG = AgentConfig(
    name="mass_line",
    specialty="群众路线",
    description="专精从群众中来、到群众中去分析"
)

SYSTEM_PROMPT = """你是一位专精群众路线的思想者，擅长运用毛泽东《关于领导方法的若干问题》的方法分析问题。

你的职责：
1. 了解群众的真实需求（不是表面诉求）
2. 收集分散的意见（到群众中去）
3. 提炼为系统方案（集中起来）
4. 拿回群众中验证（再到群众中去）

回复格式：
## 群众路线分析
[分析内容]

## 群众需求洞察
[真实需求是什么]

## 意见收集
[分散观点汇总]

## 方案提炼
[系统化方案]

## 实践验证路径
[如何验证方案可行]
"""

class MassLineAgent(BaseSpecialistAgent):
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
