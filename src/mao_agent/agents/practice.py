# src/mao_agent/agents/practice.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

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
"""

class PracticeAgent(BaseSpecialistAgent):
    def __init__(self, knowledge_loader=None):
        super().__init__(AGENT_CONFIG, knowledge_loader)

    def get_system_prompt(self) -> str:
        knowledge = self.load_knowledge()
        return f"{SYSTEM_PROMPT}\n\n## 知识库\n{knowledge}"

    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        return f"""## 实践认识分析

针对问题：{task}

### 现状判断
- 调查程度：[待分析]
- 认识来源：[待分析]

### 验证方案设计
[待设计]

### 下一步实践行动
[待提出]"""