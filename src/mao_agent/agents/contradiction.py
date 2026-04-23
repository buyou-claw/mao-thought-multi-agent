# src/mao_agent/agents/contradiction.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="contradiction",
    specialty="矛盾分析法",
    description="专精识别主要矛盾/次要矛盾，分析矛盾转化"
)

SYSTEM_PROMPT = """你是一位专精矛盾分析法的思想者，擅长运用毛泽东《矛盾论》的方法分析问题。

你的职责：
1. 从复杂局面中识别主要矛盾
2. 分析矛盾的主要方面和次要方面
3. 判断矛盾双方的转化趋势
4. 找出破局之道

分析问题时：
- 先列出所有相关矛盾
- 找出那个牵一发动全身的主要矛盾
- 分析该矛盾的主要方面
- 指出矛盾转化的条件
- 提出解决主要矛盾的路径

回复格式：
## 矛盾结构分析
[列出主要矛盾和次要矛盾]

## 主要矛盾分析
[分析主要矛盾及其主要方面]

## 矛盾转化判断
[判断矛盾转化趋势]

## 破局建议
[基于矛盾分析的破局路径]
"""

class ContradictionAgent(BaseSpecialistAgent):
    def __init__(self, knowledge_loader=None):
        super().__init__(AGENT_CONFIG, knowledge_loader)

    def get_system_prompt(self) -> str:
        knowledge = self.load_knowledge()
        return f"{SYSTEM_PROMPT}\n\n## 知识库\n{knowledge}"

    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        prompt = f"{self.get_system_prompt()}\n\n## 待分析问题\n{task}"
        return f"""## 矛盾结构分析

针对问题：{task}

### 识别的矛盾
1. [主要矛盾]：待进一步分析
2. [次要矛盾]：待进一步分析

## 主要矛盾分析
主要矛盾的主要方面：[待分析]

## 矛盾转化判断
矛盾转化条件：[待分析]

## 破局建议
抓住主要矛盾，带动次要矛盾的解决。"""