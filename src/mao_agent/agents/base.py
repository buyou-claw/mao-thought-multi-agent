# src/mao_agent/agents/base.py
from abc import ABC, abstractmethod
from typing import Dict, Any, List
from pydantic import BaseModel

class AgentConfig(BaseModel):
    name: str
    specialty: str
    description: str

class BaseSpecialistAgent(ABC):
    def __init__(self, config: AgentConfig, knowledge_loader=None):
        self.config = config
        self.knowledge_loader = knowledge_loader
        self._knowledge: str = ""

    @abstractmethod
    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        """执行分析，返回分析结果"""
        pass

    @abstractmethod
    def get_system_prompt(self) -> str:
        """获取Agent的系统提示词"""
        pass

    def load_knowledge(self) -> str:
        """加载本Agent的知识库"""
        if self._knowledge:
            return self._knowledge
        if self.knowledge_loader:
            self._knowledge = self.knowledge_loader.get_agent_knowledge(
                self.config.name
            )
        return self._knowledge

    def reload_knowledge(self):
        """重新加载知识库"""
        self._knowledge = ""
        if self.knowledge_loader:
            self.knowledge_loader.reload(self.config.name)
        self.load_knowledge()

    def share_context(self) -> Dict[str, Any]:
        """返回共享给其他Agent的上下文"""
        return {
            "agent": self.config.name,
            "specialty": self.config.specialty,
            "key_insights": self.analyze.__doc__ or ""
        }