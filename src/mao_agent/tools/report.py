# src/mao_agent/tools/report.py
from typing import Dict, List, Any

class ReportGenerator:
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