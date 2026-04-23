# src/mao_agent/agents/__init__.py
from .base import BaseSpecialistAgent, AgentConfig
from .contradiction import ContradictionAgent
from .practice import PracticeAgent
from .protracted_war import ProtractedWarAgent
from .rural_strategy import RuralStrategyAgent
from .united_front import UnitedFrontAgent
from .mass_line import MassLineAgent
from .paper_tiger import PaperTigerAgent

__all__ = [
    "BaseSpecialistAgent",
    "AgentConfig",
    "ContradictionAgent",
    "PracticeAgent",
    "ProtractedWarAgent",
    "RuralStrategyAgent",
    "UnitedFrontAgent",
    "MassLineAgent",
    "PaperTigerAgent",
]