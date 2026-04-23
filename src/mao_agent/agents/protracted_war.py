# src/mao_agent/agents/protracted_war.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="protracted_war",
    specialty="持久战略",
    description="专精三阶段战略分析，力量对比评估"
)

SYSTEM_PROMPT = """你是一位专精持久战略的思想者，擅长运用毛泽东《论持久战》的方法分析问题。

你的职责：
1. 评估当前处于哪个战略阶段
2. 分析力量对比
3. 找出相持阶段的转折点
4. 提出积累优势的路径
"""

class ProtractedWarAgent(BaseSpecialistAgent):
    def __init__(self, knowledge_loader=None):
        super().__init__(AGENT_CONFIG, knowledge_loader)

    def get_system_prompt(self) -> str:
        knowledge = self.load_knowledge()
        return f"{SYSTEM_PROMPT}\n\n## 知识库\n{knowledge}"

    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        return f"""## 持久战略分析

针对问题：{task}

### 战略阶段评估
[当前阶段待定]

### 力量对比分析
[力量对比待评估]

### 转折点识别
[关键转折点待识别]

### 优势积累路径
[积累路径待规划]"""