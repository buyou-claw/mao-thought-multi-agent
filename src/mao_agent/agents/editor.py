# src/mao_agent/agents/editor.py
from typing import Dict, List, Any, TypedDict
from .base import AgentConfig
from .contradiction import ContradictionAgent
from .practice import PracticeAgent
from .protracted_war import ProtractedWarAgent
from .rural_strategy import RuralStrategyAgent
from .united_front import UnitedFrontAgent
from .mass_line import MassLineAgent
from .paper_tiger import PaperTigerAgent

class EditorState(TypedDict):
    task: str
    relevant_agents: List[str]
    agent_inputs: Dict[str, str]
    agent_outputs: Dict[str, str]
    synthesis: str
    knowledge_updates: List[dict]

AGENT_REGISTRY = {
    "contradiction": ContradictionAgent,
    "practice": PracticeAgent,
    "protracted_war": ProtractedWarAgent,
    "rural_strategy": RuralStrategyAgent,
    "united_front": UnitedFrontAgent,
    "mass_line": MassLineAgent,
    "paper_tiger": PaperTigerAgent,
}

class EditorAgent:
    def __init__(self, knowledge_loader=None):
        self.knowledge_loader = knowledge_loader
        self.agents: Dict[str, Any] = {}
        self._initialize_agents()

    def _initialize_agents(self):
        for name, agent_class in AGENT_REGISTRY.items():
            self.agents[name] = agent_class(self.knowledge_loader)

    def dispatch_task(self, task: str, relevant_agents: List[str] = None) -> EditorState:
        if relevant_agents is None:
            relevant_agents = self._auto_detect_agents(task)

        state = EditorState(
            task=task,
            relevant_agents=relevant_agents,
            agent_inputs={},
            agent_outputs={},
            synthesis="",
            knowledge_updates=[]
        )

        # 分发任务给各Agent
        for agent_name in relevant_agents:
            state["agent_inputs"][agent_name] = task
            agent = self.agents.get(agent_name)
            if agent:
                output = agent.analyze(task)
                state["agent_outputs"][agent_name] = output

        return state

    def _auto_detect_agents(self, task: str) -> List[str]:
        """根据任务内容自动检测需要调用的Agent"""
        detected = []
        task_lower = task.lower()

        if any(k in task_lower for k in ["矛盾", "主要矛盾", "次要矛盾", "问题", "冲突"]):
            detected.append("contradiction")
        if any(k in task_lower for k in ["实践", "调查", "认识", "验证"]):
            detected.append("practice")
        if any(k in task_lower for k in ["持久", "阶段", "长期", "战略"]):
            detected.append("protracted_war")
        if any(k in task_lower for k in ["农村", "边缘", "包围", "突破", "市场"]):
            detected.append("rural_strategy")
        if any(k in task_lower for k in ["统一战线", "联盟", "团结", "朋友", "敌人"]):
            detected.append("united_front")
        if any(k in task_lower for k in ["群众", "人民", "员工", "用户", "基层"]):
            detected.append("mass_line")
        if any(k in task_lower for k in ["纸老虎", "藐视", "强大", "对手", "竞争"]):
            detected.append("paper_tiger")

        # 至少返回2个Agent
        if len(detected) < 2:
            detected = ["contradiction", "practice"]
        return detected[:4]  # 最多4个

    def synthesize(self, state: EditorState) -> str:
        """综合各Agent的分析结果"""
        outputs = state["agent_outputs"]
        task = state["task"]

        synthesis = f"""# 《{task}》战略分析报告

## 一、综合分析

"""

        for agent_name, output in outputs.items():
            agent = self.agents.get(agent_name)
            if agent:
                synthesis += f"### 【{agent.config.specialty}】\n{output}\n\n"

        synthesis += f"""## 二、核心结论

基于以上分析，针对"{task}"的核心结论如下：

1. 抓住主要矛盾
2. 尊重实践验证
3. 做好战略持久准备
4. 建立统一战线

## 三、行动建议

### 近期行动（1-3个月）
- 深入调查研究
- 明确主要矛盾

### 中期行动（3-12个月）
- 建立边缘根据地
- 团结一切可以团结的力量

### 长期行动（1年以上）
- 持久积累优势
- 等待战略反攻时机
"""

        return synthesis

    def update_knowledge(self, agent_name: str, content: str) -> bool:
        """更新指定Agent的知识库"""
        if agent_name in self.agents:
            self.agents[agent_name].reload_knowledge()
            return True
        return False
