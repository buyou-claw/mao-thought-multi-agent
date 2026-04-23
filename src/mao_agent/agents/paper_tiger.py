# src/mao_agent/agents/paper_tiger.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="paper_tiger",
    specialty="纸老虎论",
    description="专精战略藐视+战术重视分析框架"
)

SYSTEM_PROMPT = """你是一位专精纸老虎论的思想者，擅长运用毛泽东与美国记者斯特朗谈话的方法分析问题。

你的职责：
1. 战略上藐视：看透对手本质弱点
2. 战术上重视：认真对待每一个具体风险
3. 找到藐视与重视的平衡点
"""

class PaperTigerAgent(BaseSpecialistAgent):
    def __init__(self, knowledge_loader=None):
        super().__init__(AGENT_CONFIG, knowledge_loader)

    def get_system_prompt(self) -> str:
        knowledge = self.load_knowledge()
        return f"{SYSTEM_PROMPT}\n\n## 知识库\n{knowledge}"

    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        return f"""## 纸老虎分析

针对问题：{task}

### 战略层面分析
[本质弱点待看透]

### 战术层面分析
[具体风险待识别]

### 平衡点判断
[藐视与重视平衡策略待制定]"""