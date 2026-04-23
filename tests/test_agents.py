# tests/test_agents.py
import pytest
from mao_agent.agents import EditorAgent, AGENT_REGISTRY
from mao_agent.knowledge.loader import KnowledgeLoader

def test_agent_registry():
    assert len(AGENT_REGISTRY) == 7
    assert "contradiction" in AGENT_REGISTRY
    assert "practice" in AGENT_REGISTRY

def test_editor_initialization():
    loader = KnowledgeLoader()
    editor = EditorAgent(loader)
    assert len(editor.agents) == 7

def test_auto_detect_contradiction():
    loader = KnowledgeLoader()
    editor = EditorAgent(loader)
    detected = editor._auto_detect_agents("分析主要矛盾")
    assert "contradiction" in detected

def test_dispatch_task():
    loader = KnowledgeLoader()
    editor = EditorAgent(loader)
    state = editor.dispatch_task("分析市场竞争策略", ["contradiction", "practice"])
    assert state["task"] == "分析市场竞争策略"
    assert "contradiction" in state["agent_outputs"]