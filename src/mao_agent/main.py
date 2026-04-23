# src/mao_agent/main.py
import typer
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from typing import Optional
from mao_agent.agents import EditorAgent, AGENT_REGISTRY
from mao_agent.knowledge.loader import KnowledgeLoader

app = typer.Typer(help="毛泽东思想多智能体协作系统")
console = Console()

@app.command()
def analyze(
    question: str = typer.Argument(..., help="要分析的问题"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="显示完整协作过程"),
):
    """分析问题"""
    console.print(f"[bold green]收到任务：[/bold green]{question}")

    loader = KnowledgeLoader()
    editor = EditorAgent(loader)

    # 自动检测相关Agent
    relevant = editor._auto_detect_agents(question)
    console.print(f"[bold blue]调度Agent：[/bold blue]{', '.join(relevant)}")

    with Live(console=console, refresh_per_second=10) as live:
        # 分发任务
        state = editor.dispatch_task(question, relevant)
        live.update(Panel("任务分发完成，开始分析..."))

        # 收集结果
        for agent_name in relevant:
            output = state["agent_outputs"].get(agent_name, "")
            live.update(Panel(f"[{agent_name}] 分析完成"))

        # 综合报告
        synthesis = editor.synthesize(state)
        live.update(Panel(synthesis, title="分析报告"))

    console.print(synthesis)

@app.command()
def chat():
    """交互式对话"""
    console.print(Panel("[bold]毛泽东思想多智能体系统[/bold]\n输入问题进行分析，输入 'quit' 退出"))
    loader = KnowledgeLoader()
    editor = EditorAgent(loader)

    while True:
        question = console.input("\n[bold green]>[/bold green] ")
        if question.lower() in ["quit", "exit", "q"]:
            break
        if not question.strip():
            continue

        relevant = editor._auto_detect_agents(question)
        state = editor.dispatch_task(question, relevant)
        synthesis = editor.synthesize(state)
        console.print(synthesis)

@app.command()
def agents():
    """显示所有可用的专项Agent"""
    console.print("[bold]专项Agent列表：[/bold]\n")
    for name, agent_class in AGENT_REGISTRY.items():
        console.print(f"  • {name}")

@app.command()
def version():
    """显示版本信息"""
    console.print("mao-thought-multi-agent v0.1.0")

if __name__ == "__main__":
    app()