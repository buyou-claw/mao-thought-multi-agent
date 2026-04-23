# tests/test_knowledge.py
import pytest
from mao_agent.knowledge.loader import KnowledgeLoader

def test_load_single_knowledge():
    loader = KnowledgeLoader()
    content = loader.load("contradiction")
    assert "矛盾分析法" in content
    assert "主要矛盾" in content

def test_load_all_knowledge():
    loader = KnowledgeLoader()
    all_kb = loader.load_all()
    assert len(all_kb) == 7
    assert "contradiction" in all_kb
    assert "practice" in all_kb

def test_get_agent_knowledge():
    loader = KnowledgeLoader()
    kb = loader.get_agent_knowledge("protracted_war")
    assert "持久" in kb
