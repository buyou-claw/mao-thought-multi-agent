# tests/test_integration.py
import pytest
from mao_agent.main import app
from typer.testing import CliRunner

runner = CliRunner()

def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "毛泽东思想" in result.output

def test_cli_agents():
    result = runner.invoke(app, ["agents"])
    assert result.exit_code == 0

def test_analyze_command():
    result = runner.invoke(app, ["analyze", "测试问题"])
    assert result.exit_code == 0