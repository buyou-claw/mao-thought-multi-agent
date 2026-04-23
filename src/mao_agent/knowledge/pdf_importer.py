# src/mao_agent/knowledge/pdf_importer.py
import subprocess
from pathlib import Path
from typing import Optional
from .updater import KnowledgeUpdater

class PDFImporter:
    def __init__(self, knowledge_updater: KnowledgeUpdater = None):
        self.updater = knowledge_updater or KnowledgeUpdater()
        self.markitdown_cmd = "markitdown"

    def convert_pdf_to_markdown(self, pdf_path: str, output_path: str = None) -> str:
        """使用markitdown将PDF转换为Markdown"""
        pdf_file = Path(pdf_path)
        if not pdf_file.exists():
            raise FileNotFoundError(f"PDF文件不存在: {pdf_path}")

        if output_path is None:
            output_path = str(pdf_file.with_suffix(".md"))

        cmd = [self.markitdown_cmd, str(pdf_file), "-o", output_path]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return output_path
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"markitdown转换失败: {e.stderr}")
        except FileNotFoundError:
            raise RuntimeError("markitdown未安装，请先安装: pip install markitdown")

    def import_pdf(
        self,
        pdf_path: str,
        agent_name: str = None,
        auto_detect: bool = True
    ) -> dict:
        """导入PDF到知识库"""
        md_path = self.convert_pdf_to_markdown(pdf_path)

        content = Path(md_path).read_text(encoding="utf-8")

        detected_agent = None
        if auto_detect:
            detected_agent = self._detect_agent_from_content(content)
            agent_name = agent_name or detected_agent

        if agent_name:
            self.updater.update_agent_knowledge(agent_name, content, append=True)

        return {
            "success": True,
            "converted_file": md_path,
            "imported_to": agent_name,
            "detected_agent": detected_agent
        }

    def _detect_agent_from_content(self, content: str) -> Optional[str]:
        """根据内容自动检测应该归属的Agent"""
        content_lower = content.lower()

        if "矛盾" in content_lower:
            return "contradiction"
        elif "实践" in content_lower or "调查" in content_lower:
            return "practice"
        elif "持久" in content_lower or "战略" in content_lower:
            return "protracted_war"
        elif "农村" in content_lower or "根据" in content_lower:
            return "rural_strategy"
        elif "统一" in content_lower or "团结" in content_lower:
            return "united_front"
        elif "群众" in content_lower or "人民" in content_lower:
            return "mass_line"
        elif "纸老虎" in content_lower:
            return "paper_tiger"

        return None