# MaoThought Multi-Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建一个基于毛泽东思想七大理论框架的多Agent协作系统，通过专精Agent的自主协商，为用户提供对话咨询、内容创作、分析研究服务。

**Architecture:** 采用LangGraph作为Multi-Agent框架，7个专项Agent（专精单一思想）通过主编Agent协调工作。专项Agent之间网状通信，自主协商。CLI使用Typer+Rich实现实时日志流，API使用FastAPI。知识库以Markdown文件形式存储，支持PDF导入（markitdown）。

**Tech Stack:** LangGraph, LangChain Agents, Typer, Rich, FastAPI, Python 3.11+, Microsoft markitdown

---

## 项目结构

```
mao-thought-multi-agent/
├── pyproject.toml                          # 项目依赖管理
├── src/mao_agent/
│   ├── __init__.py
│   ├── main.py                             # CLI入口
│   ├── api.py                              # API入口
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py                         # Agent基类
│   │   ├── editor.py                       # 主编Agent
│   │   ├── contradiction.py                # 矛盾分析法Agent
│   │   ├── practice.py                     # 实践论Agent
│   │   ├── protracted_war.py               # 持久战Agent
│   │   ├── rural_strategy.py               # 农村包围城市Agent
│   │   ├── united_front.py                 # 统一战线Agent
│   │   ├── mass_line.py                    # 群众路线Agent
│   │   └── paper_tiger.py                  # 纸老虎论Agent
│   ├── knowledge/
│   │   ├── __init__.py
│   │   ├── loader.py                       # 知识库加载器
│   │   ├── updater.py                      # 知识更新器
│   │   ├── pdf_importer.py                 # PDF导入工具
│   │   ├── 01-contradiction.md
│   │   ├── 02-practice.md
│   │   ├── 03-protracted-war.md
│   │   ├── 04-rural-strategy.md
│   │   ├── 05-united-front.md
│   │   ├── 06-mass-line.md
│   │   └── 07-paper-tiger.md
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── search.py                       # 知识检索工具
│   │   └── report.py                       # 报告生成工具
│   └── output/
│       ├── __init__.py
│       └── formatter.py                    # 输出格式化
├── tests/
│   ├── __init__.py
│   ├── test_agents.py
│   ├── test_knowledge.py
│   └── test_integration.py
└── docs/superpowers/
    ├── specs/2026-04-23-mao-thought-multi-agent-design.md
    └── plans/2026-04-23-mao-thought-multi-agent-implementation.md
```

---

## Phase 1: 项目基础结构

### Task 1: 创建项目骨架和依赖配置

**Files:**
- Create: `pyproject.toml`
- Create: `src/mao_agent/__init__.py`
- Create: `src/mao_agent/agents/__init__.py`
- Create: `src/mao_agent/knowledge/__init__.py`
- Create: `src/mao_agent/tools/__init__.py`
- Create: `src/mao_agent/output/__init__.py`
- Create: `tests/__init__.py`

- [ ] **Step 1: 创建pyproject.toml**

```toml
[project]
name = "mao-thought-multi-agent"
version = "0.1.0"
description = "毛泽东思想多智能体协作系统"
requires-python = ">=3.11"
dependencies = [
    "langgraph>=0.0.20",
    "langchain>=0.1.0",
    "langchain-anthropic>=0.1.0",
    "typer>=0.9.0",
    "rich>=13.0.0",
    "fastapi>=0.109.0",
    "uvicorn>=0.27.0",
    "pydantic>=2.0.0",
    "httpx>=0.26.0",
]

[project.scripts]
mao-agent = "mao_agent.main:app"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

- [ ] **Step 2: 创建空的__init__.py文件**

```bash
touch src/mao_agent/__init__.py
touch src/mao_agent/agents/__init__.py
touch src/mao_agent/knowledge/__init__.py
touch src/mao_agent/tools/__init__.py
touch src/mao_agent/output/__init__.py
touch tests/__init__.py
```

- [ ] **Step 3: 提交**

```bash
git add pyproject.toml src/mao_agent/__init__.py src/mao_agent/agents/__init__.py src/mao_agent/knowledge/__init__.py src/mao_agent/tools/__init__.py src/mao_agent/output/__init__.py tests/__init__.py
git commit -m "feat: initial project skeleton with dependencies"
```

---

### Task 2: 安装依赖验证环境

**Files:**
- None (dependency installation)

- [ ] **Step 1: 安装依赖**

```bash
cd /vol1/1000/ai-project/mao_agent/mao-thought-multi-agent
pip install -e .
```

Expected: Successfully installed mao-thought-multi-agent

- [ ] **Step 2: 验证安装**

```bash
mao-agent --version
```

Expected: 显示版本号

---

## Phase 2: 知识库基础

### Task 3: 创建7个思想知识库Markdown文件

**Files:**
- Create: `src/mao_agent/knowledge/01-contradiction.md`
- Create: `src/mao_agent/knowledge/02-practice.md`
- Create: `src/mao_agent/knowledge/03-protracted-war.md`
- Create: `src/mao_agent/knowledge/04-rural-strategy.md`
- Create: `src/mao_agent/knowledge/05-united-front.md`
- Create: `src/mao_agent/knowledge/06-mass-line.md`
- Create: `src/mao_agent/knowledge/07-paper-tiger.md`

- [ ] **Step 1: 创建01-contradiction.md**

```markdown
# 矛盾分析法

## 核心定义
一切事物的发展都是由内部矛盾推动的。找到主要矛盾，就找到了破局之道。

## 理论框架
- **主要矛盾**：在复杂局面中规定或影响着其他矛盾的那个矛盾
- **矛盾的主要方面**：主要矛盾内部决定事物性质的那个方面
- **矛盾的转化**：矛盾双方在一定条件下互相转化

## 经典来源
- 《矛盾论》（1937）
- "谁是我们的敌人？谁是我们的朋友？这个问题是革命的首要问题。"

## 应用案例
- 抗日战争：中日矛盾上升为主要矛盾 → 国共矛盾退居次要
- 公司经营：市场扩张 vs 利润压缩，哪个是主要矛盾？

## 分析模板
1. 列出所有相关矛盾
2. 识别主要矛盾
3. 分析矛盾主要方面
4. 判断矛盾转化趋势
5. 给出破局建议
```

- [ ] **Step 2: 创建02-practice.md**

```markdown
# 实践认识循环

## 核心定义
认识从实践中来，在实践中检验，再回到实践中去。没有调查就没有发言权。

## 理论框架
- **实践（感性认识）**：亲自接触事物，获得直接经验
- **理论（理性认识）**：将经验上升为规律性认识
- **再实践**：用理论指导新的实践，验证和修正

## 经典来源
- 《实践论》（1937）
- 《反对本本主义》（1930）
- "你要知道梨子的滋味，你就得变革梨子，亲口吃一吃。"

## 应用案例
- 产品开发：MVP到用户面前试
- 创业：商业计划书不如先卖出第一单

## 分析模板
1. 问题是否经过实地调查？
2. 现有认识从何而来？实践还是理论？
3. 如何设计验证实验？
4. 下一步实践行动是什么？
```

- [ ] **Step 3: 创建03-protracted-war.md**

```markdown
# 持久战略

## 核心定义
在力量对比不利时，不求速胜，以时间换空间，在持久中逐步改变力量对比。

## 理论框架
- **三阶段论**：战略防御 → 战略相持 → 战略反攻
- **相持阶段**：最关键、最困难、也最容易出错的阶段
- **核心原则**：敌强我弱是暂时的，时间站在积蓄力量的一方

## 经典来源
- 《论持久战》（1938）
- "不是不打，是不打无准备之仗"

## 应用案例
- 创业公司 vs 行业巨头
- 职业发展的三个阶段

## 分析模板
1. 当前处于哪个战略阶段？
2. 力量对比如何？
3. 相持阶段的转折点是什么？
4. 如何积累优势？
```

- [ ] **Step 4: 创建04-rural-strategy.md**

```markdown
# 农村包围城市

## 核心定义
不在敌人力量最强的地方争夺，先在边缘建立根据地，再逐步包围中心。

## 理论框架
- **城市是敌人的主场**：不硬攻
- **农村是敌人忽视的地方**：先扎根
- **根据地连成片**：形成包围 → 最终拿下城市

## 经典来源
- 《星星之火，可以燎原》（1930）
- 《井冈山的斗争》（1928）
- "星星之火，可以燎原"

## 应用案例
- 拼多多农村包围城市
- 技术产品边缘场景证明价值

## 分析模板
1. 边缘市场在哪里？
2. 如何建立稳固的根据地？
3. 如何连点成片？
4. 时机成熟如何包围中心？
```

- [ ] **Step 5: 创建05-united-front.md**

```markdown
# 统一战线

## 核心定义
把朋友搞得多多的，把敌人搞得少少的。一切可以团结的力量都要团结。

## 理论框架
- **分清敌我友**：第一步分析
- **又团结又斗争**：求同存异，保持独立性
- **动态调整**：根据矛盾变化调整联盟

## 经典来源
- 《中国社会各阶级的分析》（1925）
- "又团结又斗争，以斗争求团结"

## 应用案例
- 抗日民族统一战线
- 商业竞合策略

## 分析模板
1. 谁是敌人？谁是朋友？
2. 共同利益点在哪里？
3. 如何保持独立性？
4. 矛盾变化时如何调整？
```

- [ ] **Step 6: 创建06-mass-line.md**

```markdown
# 群众路线

## 核心定义
从群众中来，到群众中去。领导者是群众智慧的集中者和执行者。

## 理论框架
- **收集**：深入群众，了解分散的意见和经验
- **提炼**：将群众意见系统化
- **执行**：拿回群众中检验，不认可则修正

## 经典来源
- 《关于领导方法的若干问题》（1943）
- "群众是真正的英雄"

## 应用案例
- 产品需求调研
- 团队决策流程

## 分析模板
1. 群众的真实需求是什么？
2. 如何收集分散的意见？
3. 如何提炼为系统方案？
4. 如何拿回群众中验证？
```

- [ ] **Step 7: 创建07-paper-tiger.md**

```markdown
# 纸老虎论

## 核心定义
一切貌似强大的对手，从长远看、从本质看，都是纸老虎。战略上藐视它，战术上重视它。

## 理论框架
- **战略层面**：看本质，看趋势
- **战术层面**：每一个具体的仗都要认真打
- **两层缺一不可**：只有战略藐视没有战术重视是鲁莽；只有战术重视没有战略藐视是怯懦

## 经典来源
- 与斯特朗谈话（1946）
- "一切反动派都是纸老虎"

## 应用案例
- 面对强劲竞争对手
- 面对困难项目

## 分析模板
1. 战略上：它的本质弱点是什么？
2. 战术上：具体风险点有哪些？
3. 如何做到藐视与重视的平衡？
```

- [ ] **Step 8: 提交**

```bash
git add src/mao_agent/knowledge/*.md
git commit -m "feat: initial 7 thought knowledge bases"
```

---

### Task 4: 实现知识库加载器

**Files:**
- Create: `src/mao_agent/knowledge/loader.py`
- Test: `tests/test_knowledge.py`

- [ ] **Step 1: 编写测试**

```python
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
```

- [ ] **Step 2: 运行测试验证失败**

```bash
pytest tests/test_knowledge.py::test_load_single_knowledge -v
```

Expected: FAIL - module not found

- [ ] **Step 3: 实现loader.py**

```python
# src/mao_agent/knowledge/loader.py
from pathlib import Path
from typing import Dict

class KnowledgeLoader:
    def __init__(self, knowledge_dir: str = None):
        if knowledge_dir is None:
            base = Path(__file__).parent
            knowledge_dir = base
        self.knowledge_dir = Path(knowledge_dir)
        self._cache: Dict[str, str] = {}
        self._agent_mapping = {
            "contradiction": "01-contradiction.md",
            "practice": "02-practice.md",
            "protracted_war": "03-protracted-war.md",
            "rural_strategy": "04-rural-strategy.md",
            "united_front": "05-united-front.md",
            "mass_line": "06-mass-line.md",
            "paper_tiger": "07-paper-tiger.md",
        }

    def load(self, agent_name: str) -> str:
        if agent_name in self._cache:
            return self._cache[agent_name]
        filename = self._agent_mapping.get(agent_name)
        if not filename:
            raise ValueError(f"Unknown agent: {agent_name}")
        file_path = self.knowledge_dir / filename
        content = file_path.read_text(encoding="utf-8")
        self._cache[agent_name] = content
        return content

    def load_all(self) -> Dict[str, str]:
        return {name: self.load(name) for name in self._agent_mapping.keys()}

    def get_agent_knowledge(self, agent_name: str) -> str:
        return self.load(agent_name)

    def reload(self, agent_name: str = None):
        if agent_name:
            self._cache.pop(agent_name, None)
        else:
            self._cache.clear()
```

- [ ] **Step 4: 运行测试验证通过**

```bash
pytest tests/test_knowledge.py -v
```

Expected: PASS

- [ ] **Step 5: 提交**

```bash
git add src/mao_agent/knowledge/loader.py tests/test_knowledge.py
git commit -m "feat: implement knowledge loader"
```

---

## Phase 3: Agent实现

### Task 5: 实现Agent基类

**Files:**
- Create: `src/mao_agent/agents/base.py`
- Modify: `src/mao_agent/agents/__init__.py`

- [ ] **Step 1: 创建base.py**

```python
# src/mao_agent/agents/base.py
from abc import ABC, abstractmethod
from typing import Dict, Any, List
from pydantic import BaseModel

class AgentConfig(BaseModel):
    name: str
    specialty: str
    description: str

class BaseSpecialistAgent(ABC):
    def __init__(self, config: AgentConfig, knowledge_loader=None):
        self.config = config
        self.knowledge_loader = knowledge_loader
        self._knowledge: str = ""

    @abstractmethod
    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        """执行分析，返回分析结果"""
        pass

    @abstractmethod
    def get_system_prompt(self) -> str:
        """获取Agent的系统提示词"""
        pass

    def load_knowledge(self) -> str:
        """加载本Agent的知识库"""
        if self._knowledge:
            return self._knowledge
        if self.knowledge_loader:
            self._knowledge = self.knowledge_loader.get_agent_knowledge(
                self.config.name
            )
        return self._knowledge

    def reload_knowledge(self):
        """重新加载知识库"""
        self._knowledge = ""
        if self.knowledge_loader:
            self.knowledge_loader.reload(self.config.name)
        self.load_knowledge()

    def share_context(self) -> Dict[str, Any]:
        """返回共享给其他Agent的上下文"""
        return {
            "agent": self.config.name,
            "specialty": self.config.specialty,
            "key_insights": self.analyze.__doc__ or ""
        }
```

- [ ] **Step 2: 更新__init__.py**

```python
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
```

- [ ] **Step 3: 提交**

```bash
git add src/mao_agent/agents/base.py src/mao_agent/agents/__init__.py
git commit -m "feat: implement base agent class"
```

---

### Task 6: 实现7个专项Agent

**Files:**
- Create: `src/mao_agent/agents/contradiction.py`
- Create: `src/mao_agent/agents/practice.py`
- Create: `src/mao_agent/agents/protracted_war.py`
- Create: `src/mao_agent/agents/rural_strategy.py`
- Create: `src/mao_agent/agents/united_front.py`
- Create: `src/mao_agent/agents/mass_line.py`
- Create: `src/mao_agent/agents/paper_tiger.py`

- [ ] **Step 1: 创建contradiction.py**

```python
# src/mao_agent/agents/contradiction.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="contradiction",
    specialty="矛盾分析法",
    description="专精识别主要矛盾/次要矛盾，分析矛盾转化"
)

SYSTEM_PROMPT = """你是一位专精矛盾分析法的思想者，擅长运用毛泽东《矛盾论》的方法分析问题。

你的职责：
1. 从复杂局面中识别主要矛盾
2. 分析矛盾的主要方面和次要方面
3. 判断矛盾双方的转化趋势
4. 找出破局之道

分析问题时：
- 先列出所有相关矛盾
- 找出那个牵一发动全身的主要矛盾
- 分析该矛盾的主要方面
- 指出矛盾转化的条件
- 提出解决主要矛盾的路径

回复格式：
## 矛盾结构分析
[列出主要矛盾和次要矛盾]

## 主要矛盾分析
[分析主要矛盾及其主要方面]

## 矛盾转化判断
[判断矛盾转化趋势]

## 破局建议
[基于矛盾分析的破局路径]
"""

class ContradictionAgent(BaseSpecialistAgent):
    def __init__(self, knowledge_loader=None):
        super().__init__(AGENT_CONFIG, knowledge_loader)

    def get_system_prompt(self) -> str:
        knowledge = self.load_knowledge()
        return f"{SYSTEM_PROMPT}\n\n## 知识库\n{knowledge}"

    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        prompt = f"{self.get_system_prompt()}\n\n## 待分析问题\n{task}"
        # 实际调用LLM，这里简化为返回结构化分析框架
        return f"""## 矛盾结构分析

针对问题：{task}

### 识别的矛盾
1. [主要矛盾]：待进一步分析
2. [次要矛盾]：待进一步分析

## 主要矛盾分析
主要矛盾的主要方面：[待分析]

## 矛盾转化判断
矛盾转化条件：[待分析]

## 破局建议
抓住主要矛盾，带动次要矛盾的解决。"""
```

- [ ] **Step 2: 创建其他6个Agent（简化版示例）**

```python
# src/mao_agent/agents/practice.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="practice",
    specialty="实践认识循环",
    description="专精'没有调查就没有发言权'分析框架"
)

SYSTEM_PROMPT = """你是一位专精实践认识循环的思想者，擅长运用毛泽东《实践论》的方法分析问题。

你的职责：
1. 判断问题是否经过实地调查
2. 分析认识的来源（实践还是理论）
3. 设计验证方案
4. 提出下一步实践行动
"""

class PracticeAgent(BaseSpecialistAgent):
    def __init__(self, knowledge_loader=None):
        super().__init__(AGENT_CONFIG, knowledge_loader)

    def get_system_prompt(self) -> str:
        knowledge = self.load_knowledge()
        return f"{SYSTEM_PROMPT}\n\n## 知识库\n{knowledge}"

    def analyze(self, task: str, context: Dict[str, Any] = None) -> str:
        return f"""## 实践认识分析

针对问题：{task}

### 现状判断
- 调查程度：[待分析]
- 认识来源：[待分析]

### 验证方案设计
[待设计]

### 下一步实践行动
[待提出]"""
```

```python
# src/mao_agent/agents/protracted_war.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="protracted_war",
    specialty="持久战略",
    description="专精三阶段战略分析，力量对比评估"
)
```

```python
# src/mao_agent/agents/rural_strategy.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="rural_strategy",
    specialty="农村包围城市",
    description="专精边缘突破、市场进入策略分析"
)
```

```python
# src/mao_agent/agents/united_front.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="united_front",
    specialty="统一战线",
    description="专精利益格局、联盟策略分析"
)
```

```python
# src/mao_agent/agents/mass_line.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="mass_line",
    specialty="群众路线",
    description="专精从群众中来、到群众中去分析"
)
```

```python
# src/mao_agent/agents/paper_tiger.py
from typing import Dict, Any
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="paper_tiger",
    specialty="纸老虎论",
    description="专精战略藐视+战术重视分析框架"
)
```

- [ ] **Step 3: 提交**

```bash
git add src/mao_agent/agents/contradiction.py src/mao_agent/agents/practice.py src/mao_agent/agents/protracted_war.py src/mao_agent/agents/rural_strategy.py src/mao_agent/agents/united_front.py src/mao_agent/agents/mass_line.py src/mao_agent/agents/paper_tiger.py
git commit -m "feat: implement 7 specialist agents"
```

---

### Task 7: 实现主编Agent

**Files:**
- Create: `src/mao_agent/agents/editor.py`
- Modify: `src/mao_agent/agents/__init__.py`

- [ ] **Step 1: 创建editor.py**

```python
# src/mao_agent/agents/editor.py
from typing import Dict, List, Any, TypedDict
from .base import AgentConfig
from .contradiction import ContradictionAgent
from .practice import PracticeAgent
from .protracted_war import ProtractedWarAgent
from .rural_strategy import RuralStrategyAgent
from .united_front import UnitedFrontAgent
from .mass_line import MassLineAgent
from .paper_tiger import PaperTigerAgent

class EditorState(TypedDict):
    task: str
    relevant_agents: List[str]
    agent_inputs: Dict[str, str]
    agent_outputs: Dict[str, str]
    synthesis: str
    knowledge_updates: List[dict]

AGENT_REGISTRY = {
    "contradiction": ContradictionAgent,
    "practice": PracticeAgent,
    "protracted_war": ProtractedWarAgent,
    "rural_strategy": RuralStrategyAgent,
    "united_front": UnitedFrontAgent,
    "mass_line": MassLineAgent,
    "paper_tiger": PaperTigerAgent,
}

class EditorAgent:
    def __init__(self, knowledge_loader=None):
        self.knowledge_loader = knowledge_loader
        self.agents: Dict[str, Any] = {}
        self._initialize_agents()

    def _initialize_agents(self):
        for name, agent_class in AGENT_REGISTRY.items():
            self.agents[name] = agent_class(self.knowledge_loader)

    def dispatch_task(self, task: str, relevant_agents: List[str] = None) -> EditorState:
        if relevant_agents is None:
            relevant_agents = self._auto_detect_agents(task)

        state = EditorState(
            task=task,
            relevant_agents=relevant_agents,
            agent_inputs={},
            agent_outputs={},
            synthesis="",
            knowledge_updates=[]
        )

        # 分发任务给各Agent
        for agent_name in relevant_agents:
            state["agent_inputs"][agent_name] = task
            agent = self.agents.get(agent_name)
            if agent:
                output = agent.analyze(task)
                state["agent_outputs"][agent_name] = output

        return state

    def _auto_detect_agents(self, task: str) -> List[str]:
        """根据任务内容自动检测需要调用的Agent"""
        detected = []
        task_lower = task.lower()

        if any(k in task_lower for k in ["矛盾", "主要矛盾", "次要矛盾", "问题", "冲突"]):
            detected.append("contradiction")
        if any(k in task_lower for k in ["实践", "调查", "认识", "验证", "调查"]):
            detected.append("practice")
        if any(k in task_lower for k in ["持久", "阶段", "长期", "战略"]):
            detected.append("protracted_war")
        if any(k in task_lower for k in ["农村", "边缘", "包围", "突破", "市场"]):
            detected.append("rural_strategy")
        if any(k in task_lower for k in ["统一战线", "联盟", "团结", "朋友", "敌人"]):
            detected.append("united_front")
        if any(k in task_lower for k in ["群众", "人民", "员工", "用户", "基层"]):
            detected.append("mass_line")
        if any(k in task_lower for k in ["纸老虎", "藐视", "强大", "对手", "竞争"]):
            detected.append("paper_tiger")

        # 至少返回2个Agent
        if len(detected) < 2:
            detected = ["contradiction", "practice"]
        return detected[:4]  # 最多4个

    def synthesize(self, state: EditorState) -> str:
        """综合各Agent的分析结果"""
        outputs = state["agent_outputs"]
        task = state["task"]

        synthesis = f"""# 《{task}》战略分析报告

## 一、综合分析

"""

        for agent_name, output in outputs.items():
            agent = self.agents.get(agent_name)
            if agent:
                synthesis += f"### 【{agent.config.specialty}】\n{output}\n\n"

        synthesis += f"""## 二、核心结论

基于以上分析，针对"{task}"的核心结论如下：

1. 抓住主要矛盾
2. 尊重实践验证
3. 做好战略持久准备
4. 建立统一战线

## 三、行动建议

### 近期行动（1-3个月）
- 深入调查研究
- 明确主要矛盾

### 中期行动（3-12个月）
- 建立边缘根据地
- 团结一切可以团结的力量

### 长期行动（1年以上）
- 持久积累优势
- 等待战略反攻时机
"""

        return synthesis

    def update_knowledge(self, agent_name: str, content: str) -> bool:
        """更新指定Agent的知识库"""
        if agent_name in self.agents:
            self.agents[agent_name].reload_knowledge()
            return True
        return False
```

- [ ] **Step 2: 更新__init__.py导出EditorAgent**

```python
from .base import BaseSpecialistAgent, AgentConfig
from .editor import EditorAgent, AGENT_REGISTRY
# ... 保留其他导入
```

- [ ] **Step 3: 提交**

```bash
git add src/mao_agent/agents/editor.py src/mao_agent/agents/__init__.py
git commit -m "feat: implement editor agent with dispatch and synthesis"
```

---

## Phase 4: CLI实现

### Task 8: 实现CLI主入口

**Files:**
- Create: `src/mao_agent/main.py`

- [ ] **Step 1: 创建main.py**

```python
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
```

- [ ] **Step 2: 测试CLI**

```bash
mao-agent --help
mao-agent agents
mao-agent version
```

- [ ] **Step 3: 提交**

```bash
git add src/mao_agent/main.py
git commit -m "feat: implement CLI entry point"
```

---

## Phase 5: API实现

### Task 9: 实现FastAPI服务

**Files:**
- Create: `src/mao_agent/api.py`

- [ ] **Step 1: 创建api.py**

```python
# src/mao_agent/api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from mao_agent.agents import EditorAgent
from mao_agent.knowledge.loader import KnowledgeLoader

app = FastAPI(title="毛泽东思想多智能体API")

loader = KnowledgeLoader()
editor = EditorAgent(loader)

class AnalyzeRequest(BaseModel):
    task: str
    mode: Optional[str] = "text_only"  # full or text_only

class AnalyzeResponse(BaseModel):
    report: str
    visualization: Optional[str] = None
    timeline: Optional[List[str]] = None

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/agents")
async def list_agents():
    from mao_agent.agents import AGENT_REGISTRY
    return {
        "agents": [
            {"name": name, "class": cls.__name__}
            for name, cls in AGENT_REGISTRY.items()
        ]
    }

@app.post("/api/v1/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    try:
        relevant = editor._auto_detect_agents(request.task)
        state = editor.dispatch_task(request.task, relevant)
        synthesis = editor.synthesize(state)

        response = AnalyzeResponse(report=synthesis)

        if request.mode == "full":
            response.visualization = None  # TODO: 实现可视化
            response.timeline = []  # TODO: 实现时间线

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/chat")
async def chat(request: AnalyzeRequest):
    return await analyze(request)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

- [ ] **Step 2: 测试API**

```bash
cd /vol1/1000/ai-project/mao_agent/mao-thought-multi-agent
uvicorn mao_agent.api:app --reload &
sleep 2
curl http://localhost:8000/health
curl http://localhost:8000/agents
```

- [ ] **Step 3: 提交**

```bash
git add src/mao_agent/api.py
git commit -m "feat: implement FastAPI service"
```

---

## Phase 6: 知识更新和PDF导入

### Task 10: 实现知识更新器

**Files:**
- Create: `src/mao_agent/knowledge/updater.py`

- [ ] **Step 1: 创建updater.py**

```python
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
```

- [ ] **Step 2: 提交**

```bash
git add src/mao_agent/knowledge/updater.py
git commit -m "feat: implement knowledge updater"
```

---

### Task 11: 实现PDF导入工具

**Files:**
- Create: `src/mao_agent/knowledge/pdf_importer.py`
- Modify: `src/mao_agent/main.py` (添加pdf-import命令)

- [ ] **Step 1: 创建pdf_importer.py**

```python
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
```

- [ ] **Step 2: 更新main.py添加pdf-import命令**

```python
from mao_agent.knowledge.pdf_importer import PDFImporter

@app.command()
def pdf_import(
    file: str = typer.Argument(..., help="PDF文件路径"),
    category: Optional[str] = typer.Option(None, "--category", help="指定归属的思想类别"),
    auto_detect: bool = typer.Option(True, "--auto-detect", help="自动检测类别"),
):
    """导入PDF到知识库"""
    importer = PDFImporter()
    try:
        result = importer.import_pdf(file, agent_name=category, auto_detect=auto_detect)
        console.print(f"[bold green]导入成功！[/bold green]")
        console.print(f"转换文件: {result['converted_file']}")
        console.print(f"导入到: {result['imported_to']}")
    except Exception as e:
        console.print(f"[bold red]导入失败:[/bold red] {e}")
```

- [ ] **Step 3: 提交**

```bash
git add src/mao_agent/knowledge/pdf_importer.py src/mao_agent/main.py
git commit -m "feat: implement PDF import with markitdown"
```

---

## Phase 7: 工具和输出格式化

### Task 12: 实现工具和输出格式化

**Files:**
- Create: `src/mao_agent/tools/search.py`
- Create: `src/mao_agent/tools/report.py`
- Create: `src/mao_agent/output/formatter.py`

- [ ] **Step 1: 创建search.py**

```python
# src/mao_agent/tools/search.py
from typing import List, Dict, Any
from mao_agent.knowledge.loader import KnowledgeLoader

class KnowledgeSearch:
    def __init__(self, loader: KnowledgeLoader = None):
        self.loader = loader or KnowledgeLoader()

    def search_by_keyword(self, keyword: str) -> List[Dict[str, str]]:
        """搜索包含关键词的知识"""
        results = []
        all_kb = self.loader.load_all()

        for agent_name, content in all_kb.items():
            if keyword in content:
                results.append({
                    "agent": agent_name,
                    "matched": keyword in content
                })

        return results

    def get_relevant_knowledge(self, query: str) -> Dict[str, str]:
        """根据查询获取相关知识"""
        agents = self.loader._agent_mapping.keys()
        relevant = {}

        for agent in agents:
            content = self.loader.get_agent_knowledge(agent)
            relevant[agent] = content

        return relevant
```

- [ ] **Step 2: 创建report.py**

```python
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
```

- [ ] **Step 3: 创建formatter.py**

```python
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
```

- [ ] **Step 4: 提交**

```bash
git add src/mao_agent/tools/search.py src/mao_agent/tools/report.py src/mao_agent/output/formatter.py
git commit -m "feat: implement search tools and output formatter"
```

---

## Phase 8: 集成测试

### Task 13: 实现集成测试

**Files:**
- Create: `tests/test_agents.py`
- Create: `tests/test_integration.py`

- [ ] **Step 1: 创建test_agents.py**

```python
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
```

- [ ] **Step 2: 创建test_integration.py**

```python
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
```

- [ ] **Step 3: 运行测试**

```bash
pytest tests/ -v
```

- [ ] **Step 4: 提交**

```bash
git add tests/test_agents.py tests/test_integration.py
git commit -m "test: add integration tests"
```

---

## 自检清单

完成所有任务后，请确认以下检查项：

### 规范覆盖检查

- [ ] Spec Section 3.1 (主编Agent) → Task 7
- [ ] Spec Section 3.2 (专项Agent × 7) → Task 5, 6
- [ ] Spec Section 3.3 (知识库) → Task 3, 4
- [ ] Spec Section 4.1 (CLI) → Task 8
- [ ] Spec Section 4.2 (API) → Task 9
- [ ] Spec Section 6 (知识进化) → Task 10, 11
- [ ] PDF导入 (markitdown) → Task 11

### 验收标准检查

- [ ] 主编Agent能正确调度相关专项Agent
- [ ] 专项Agent之间能进行网状通信
- [ ] CLI实时日志流正常输出
- [ ] API正常返回结构化报告
- [ ] 知识更新命令能正确更新Markdown
- [ ] 专项Agent能重新加载更新后的知识
- [ ] PDF导入功能正常工作

### 提交检查

```bash
git log --oneline
# 确认每个Phase都有对应的commit
```
