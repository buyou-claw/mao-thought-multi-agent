# src/mao_agent/knowledge/updater.py
from pathlib import Path
from typing import Optional
from .loader import KnowledgeLoader

class KnowledgeUpdater:
    def __init__(self, knowledge_dir: str = None):
        self.loader = KnowledgeLoader(knowledge_dir)
        self.knowledge_dir = Path(knowledge_dir) if knowledge_dir else self.loader.knowledge_dir

    def update_agent_knowledge(self, agent_name: str, new_content: str, append: bool = True) -> bool:
        """更新指定Agent的知识库"""
        filename = self.loader._agent_mapping.get(agent_name)
        if not filename:
            return False

        file_path = self.knowledge_dir / filename

        if append:
            existing = file_path.read_text(encoding="utf-8")
            updated = f"{existing}\n\n---\n\n## 补充内容\n\n{new_content}"
        else:
            updated = new_content

        file_path.write_text(updated, encoding="utf-8")
        self.loader.reload(agent_name)
        return True

    def update_from_user_input(self, agent_name: str, user_content: str) -> dict:
        """从用户对话中解析更新内容并更新知识库"""
        success = self.update_agent_knowledge(agent_name, user_content, append=True)
        return {
            "success": success,
            "agent": agent_name,
            "message": "知识库更新成功" if success else "更新失败"
        }