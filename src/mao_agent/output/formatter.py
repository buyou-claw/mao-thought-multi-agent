# src/mao_agent/output/formatter.py
from typing import Dict, Any
from rich.console import Console
from rich.markdown import Markdown

class OutputFormatter:
    def __init__(self):
        self.console = Console()

    def format_report(self, report: str):
        """格式化报告输出"""
        self.console.print(Markdown(report))

    def format_agent_output(self, agent_name: str, output: str):
        """格式化Agent输出"""
        self.console.print(f"\n[bold cyan]=== {agent_name} ===[/bold cyan]")
        self.console.print(output)

    def format_error(self, error: str):
        """格式化错误信息"""
        self.console.print(f"[bold red]错误:[/bold red] {error}")