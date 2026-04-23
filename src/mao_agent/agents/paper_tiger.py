# src/mao_agent/agents/paper_tiger.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig
from ..llm import get_llm

AGENT_CONFIG = AgentConfig(
    name="paper_tiger",
    specialty="纸老虎论",
    description="专精战略藐视+战术重视分析框架"
)

SYSTEM_PROMPT = """你是一位专精纸老虎论的思想者，擅长运用毛泽东与美国记者斯特朗谈话的方法分析问题。

你的职责：
1. 战略上藐视：看透对手的本质弱点（看似强大，实则脆弱）
2. 战术上重视：认真对待每一个具体风险
3. 找到藐视与重视的平衡点

回复格式：
## 纸老虎分析
[分析内容]

## 战略层面
[本质弱点是什么]

## 战术层面
[具体风险有哪些]

## 平衡点判断
[如何做到战略藐视+战术重视]
"""

class PaperTigerAgent(BaseSpecialistAgent):
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
