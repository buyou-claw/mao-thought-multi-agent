# src/mao_agent/agents/mass_line.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="mass_line",
    specialty="群众路线",
    description="专精从群众中来、到群众中去分析"
)

SYSTEM_PROMPT = """你是一位专精群众路线的思想者，擅长运用毛泽东《关于领导方法的若干问题》的方法分析问题。

你的职责：
1. 了解群众的真实需求
2. 收集分散的意见
3. 提炼为系统方案
4. 拿回群众中验证
"""

class MassLineAgent(BaseSpecialistAgent):
    def __init__(self, knowledge_loader=None):
        super().__init__(AGENT_CONFIG, knowledge_loader)

    def get_system_prompt(self) -> str:
        knowledge = self.load_knowledge()
        return f"{SYSTEM_PROMPT}\n\n## 知识库\n{knowledge}"

    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        return f"""## 群众路线分析

针对问题：{task}

### 群众需求洞察
[真实需求待发现]

### 意见收集
[分散观点待汇总]

### 方案提炼
[系统方案待形成]

### 实践验证
[验证路径待设计]"""