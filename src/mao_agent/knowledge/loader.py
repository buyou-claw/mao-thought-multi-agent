# src/mao_agent/knowledge/loader.py
from pathlib import Path
from typing import Dict

class KnowledgeLoader:
    def __init__(self, knowledge_dir: str = None):
        if knowledge_dir is None:
            base = Path(__file__).parent
            knowledge_dir = base
        self.knowledge_dir = Path(knowledge_dir)
        self._cache: Dict[str, str] = {}
        self._agent_mapping = {
            "contradiction": "01-contradiction.md",
            "practice": "02-practice.md",
            "protracted_war": "03-protracted-war.md",
            "rural_strategy": "04-rural-strategy.md",
            "united_front": "05-united-front.md",
            "mass_line": "06-mass-line.md",
            "paper_tiger": "07-paper-tiger.md",
        }

    def load(self, agent_name: str) -> str:
        if agent_name in self._cache:
            return self._cache[agent_name]
        filename = self._agent_mapping.get(agent_name)
        if not filename:
            raise ValueError(f"Unknown agent: {agent_name}")
        file_path = self.knowledge_dir / filename
        content = file_path.read_text(encoding="utf-8")
        self._cache[agent_name] = content
        return content

    def load_all(self) -> Dict[str, str]:
        return {name: self.load(name) for name in self._agent_mapping.keys()}

    def get_agent_knowledge(self, agent_name: str) -> str:
        return self.load(agent_name)

    def reload(self, agent_name: str = None):
        if agent_name:
            self._cache.pop(agent_name, None)
        else:
            self._cache.clear()
