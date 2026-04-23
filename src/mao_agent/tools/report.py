# src/mao_agent/tools/report.py
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class ReportGenerator:
    REPORTS_DIR = Path("reports")

    @classmethod
    def ensure_reports_dir(cls):
        """确保报告目录存在"""
        cls.REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def generate_filename(cls, content: str, task: str) -> str:
        """根据内容生成唯一文件名"""
        prefix = task[:20].strip().replace(" ", "_").replace("/", "_").replace("\\", "_")
        prefix = "".join(c for c in prefix if c.isalnum() or c in "_-")
        if not prefix:
            prefix = "report"
        content_hash = hashlib.md5(content.encode()[:200]).hexdigest()[:8]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{prefix}_{timestamp}_{content_hash}.md"

    @classmethod
    def save_report(cls, report: str, task: str) -> Path:
        """保存报告到本地markdown文件"""
        cls.ensure_reports_dir()
        filename = cls.generate_filename(report, task)
        filepath = cls.REPORTS_DIR / filename
        filepath.write_text(report, encoding="utf-8")
        return filepath

    @staticmethod
    def generate_analysis_report(task: str, agent_outputs: Dict[str, str]) -> str:
        """生成结构化分析报告"""
        report = f"# 《{task}》战略分析报告\n\n"
        report += "## 一、综合分析\n\n"

        for agent_name, output in agent_outputs.items():
            report += f"### 【{agent_name}】\n{output}\n\n"

        report += "## 二、核心结论\n\n"
        report += "## 三、行动建议\n\n"

        return report

    @staticmethod
    def generate_timeline(stages: List[str]) -> List[Dict[str, Any]]:
        """生成战略时间线"""
        timeline = []
        for i, stage in enumerate(stages):
            timeline.append({
                "phase": i + 1,
                "name": stage,
                "description": f"第{i+1}阶段: {stage}"
            })
        return timeline