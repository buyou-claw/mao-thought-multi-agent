# 毛泽东思想多智能体协作系统

> 基于毛泽东思想七大理论框架的多Agent协作系统，通过专精Agent的自主协商，为用户提供对话咨询、内容创作、分析研究服务。

## 核心特性

- **七大专项Agent**：矛盾分析法、实践论、持久战、农村包围城市、统一战线、群众路线、纸老虎论
- **主编Agent协调**：智能调度专项Agent，自主协商，综合分析
- **多入口支持**：CLI实时日志流 + REST API
- **知识可进化**：Markdown知识库 + PDF导入 + 对话式更新
- **结构化输出**：分析报告 + 可视化 + 战略时间线

## 思想框架

| Agent | 专精思想 | 核心方法论 |
|-------|---------|-----------|
| ContradictionAgent | 矛盾分析法 | 找主要矛盾，破局之道 |
| PracticeAgent | 实践认识循环 | 没有调查就没有发言权 |
| ProtractedWarAgent | 持久战略 | 三阶段战略：防御→相持→反攻 |
| RuralStrategyAgent | 农村包围城市 | 边缘突破，根据地连片 |
| UnitedFrontAgent | 统一战线 | 团结一切可以团结的力量 |
| MassLineAgent | 群众路线 | 从群众中来，到群众中去 |
| PaperTigerAgent | 纸老虎论 | 战略上藐视，战术上重视 |

## 快速开始

### 安装

```bash
cd mao-thought-multi-agent
pip install -e .
```

### CLI使用

```bash
# 分析问题
mao-agent analyze "分析某创业公司面对行业巨头的竞争策略"

# 交互式对话
mao-agent chat

# 查看所有Agent
mao-agent agents

# 导入PDF到知识库
mao-agent pdf-import ./source/毛选补充.pdf --auto-detect
mao-agent pdf-import ./source/矛盾论新解.pdf --category contradiction
```

### API服务

```bash
# 启动服务
uvicorn mao_agent.api:app --reload --host 0.0.0.0 --port 8000

# 健康检查
curl http://localhost:8000/health

# 分析接口
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{"task": "分析某创业公司面对行业巨头的竞争策略"}'

# 查看所有Agent
curl http://localhost:8000/agents
```

## 项目结构

```
mao-thought-multi-agent/
├── src/mao_agent/
│   ├── main.py                 # CLI入口
│   ├── api.py                  # FastAPI服务
│   ├── agents/
│   │   ├── base.py            # Agent基类
│   │   ├── editor.py           # 主编Agent（调度+综合）
│   │   ├── contradiction.py     # 矛盾分析法Agent
│   │   ├── practice.py          # 实践论Agent
│   │   ├── protracted_war.py    # 持久战Agent
│   │   ├── rural_strategy.py    # 农村包围城市Agent
│   │   ├── united_front.py      # 统一战线Agent
│   │   ├── mass_line.py         # 群众路线Agent
│   │   └── paper_tiger.py       # 纸老虎论Agent
│   ├── knowledge/              # 知识库
│   │   ├── loader.py           # 知识加载器
│   │   ├── updater.py          # 知识更新器
│   │   ├── pdf_importer.py      # PDF导入工具
│   │   └── 01-07-*.md          # 7大思想知识库
│   ├── tools/
│   │   ├── search.py           # 知识检索工具
│   │   └── report.py          # 报告生成工具
│   └── output/
│       └── formatter.py        # 输出格式化
├── tests/                      # 测试
└── docs/                       # 文档
```

## 使用场景

### 1. 战略分析

```bash
mao-agent analyze "分析某公司面对行业巨头的竞争策略"
```

输出结构化分析报告：
- 矛盾结构分析
- 力量对比评估
- 战略阶段判断
- 行动建议（近期/中期/长期）

### 2. 内容创作

```python
# API调用
import requests

response = requests.post("http://localhost:8000/api/v1/analyze", json={
    "task": "写一篇关于农村包围城市战略的演讲稿",
    "mode": "full"
})
print(response.json()["report"])
```

### 3. 知识进化

```bash
# 添加新的案例到知识库
mao-agent pdf-import ./新增文献.pdf --category rural_strategy

# 或者直接编辑Markdown文件
vim src/mao_agent/knowledge/04-rural-strategy.md
```

## 知识库结构

每个思想的知识库Markdown包含：

```markdown
# {思想名称}

## 核心定义
一句话概括

## 理论框架
- 关键概念
- 原理说明

## 经典来源
- 原始著作引用
- 原文摘要

## 应用案例
- 历史案例
- 现代应用示例

## 分析模板
- 标准化分析步骤
- prompt提示词模板
```

## 配置

### 环境变量

```bash
# 可选：设置API密钥等
export ANTHROPIC_API_KEY="your-api-key"
```

### 知识库路径

知识库默认位于 `src/mao_agent/knowledge/`，可在初始化时指定自定义路径：

```python
from mao_agent.knowledge.loader import KnowledgeLoader

loader = KnowledgeLoader("/path/to/knowledge")
```

## 开发

### 运行测试

```bash
pytest tests/ -v
```

### 添加新的专项Agent

1. 在 `src/mao_agent/agents/` 创建新Agent文件（如 `new_agent.py`）
2. 继承 `BaseSpecialistAgent`
3. 实现 `analyze()` 和 `get_system_prompt()` 方法
4. 在 `editor.py` 的 `AGENT_REGISTRY` 中注册
5. 创建对应的知识库文件 `knowledge/xx-new.md`

```python
# new_agent.py
from .base import BaseSpecialistAgent, AgentConfig

AGENT_CONFIG = AgentConfig(
    name="new_agent",
    specialty="新思想",
    description="描述"
)

class NewAgent(BaseSpecialistAgent):
    def __init__(self, knowledge_loader=None):
        super().__init__(AGENT_CONFIG, knowledge_loader)

    def get_system_prompt(self) -> str:
        return "你的系统提示词"

    def analyze(self, task: str, context=None) -> str:
        return "分析结果"
```

## 架构说明

### Agent通信拓扑

```
用户请求
     ↓
主编Agent（EditorAgent）
  ├── 任务分发（星型）
  ├── 结果整合
  └── 自主协商（网状）
     ↓
专项Agent × 7
     ↓
知识库（Markdown）
```

### 工作流程

1. 用户输入问题
2. 主编Agent分析问题，自动检测相关专项Agent
3. 任务分发给相关专项Agent（可并行）
4. 专项Agent加载自身知识库，进行分析
5. 专项Agent之间可自主协商（网状通信）
6. 主编Agent收集结果，综合撰写
7. 输出结构化报告

## 技术栈

- **Multi-Agent框架**: LangGraph
- **CLI**: Typer + Rich
- **API**: FastAPI + Uvicorn
- **PDF处理**: Microsoft markitdown
- **Python**: 3.11+

## 许可

MIT License

## 参考

- 《毛泽东选集》一至五卷
- 《矛盾论》《实践论》《论持久战》
- 《星星之火，可以燎原》
- 《关于正确处理人民内部矛盾的问题》
