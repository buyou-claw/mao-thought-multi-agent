# src/mao_agent/tools/search.py
from typing import List, Dict, Any
from mao_agent.knowledge.loader import KnowledgeLoader

class KnowledgeSearch:
    def __init__(self, loader: KnowledgeLoader = None):
        self.loader = loader or KnowledgeLoader()

    def search_by_keyword(self, keyword: str) -> List[Dict[str, str]]:
        """搜索包含关键词的知识"""
        results = []
        all_kb = self.loader.load_all()

        for agent_name, content in all_kb.items():
            results.append({
                "agent": agent_name,
                "matched": keyword in content
            })

        return results

    def get_relevant_knowledge(self, query: str) -> Dict[str, str]:
        """根据查询获取相关知识"""
        agents = self.loader._agent_mapping.keys()
        relevant = {}

        for agent in agents:
            content = self.loader.get_agent_knowledge(agent)
            relevant[agent] = content

        return relevant