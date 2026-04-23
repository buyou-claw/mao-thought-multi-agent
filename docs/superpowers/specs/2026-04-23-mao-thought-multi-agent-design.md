# 毛泽东思想多智能体系统设计

## 1. 项目概述

**项目名称：** MaoThought Multi-Agent

**一句话描述：** 基于毛泽东思想七大理论框架的多Agent协作系统，通过专精Agent的自主协商，为用户提供对话咨询、内容创作、分析研究服务。

**核心价值：** 将毛泽东思想的方法论（矛盾分析、实践论、持久战、农村包围城市、统一战线、群众路线、战略藐视）工具化，形成可协作的智能体网络。

---

## 2. 系统架构

### 2.1 整体架构

```
┌─────────────────────────────────────────────────────────────┐
│                      用户交互层                              │
│  ┌─────────────────┐          ┌─────────────────────────┐  │
│  │   CLI (Typer)   │          │   API (FastAPI + SSE)   │  │
│  │  实时日志流输出   │          │    纯文本结构化输出      │  │
│  └────────┬────────┘          └──────────┬──────────────┘  │
└───────────┼──────────────────────────────┼─────────────────┘
            │                              │
            ▼                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    主编Agent (EditorAgent)                    │
│  - 任务分发 (dispatch)                                       │
│  - 结果整合 (integrate)                                      │
│  - 综合分析撰写 (synthesis)                                  │
│  - 知识更新协调 (knowledge_update)                           │
└─────────────────────────────────────────────────────────────┘
            │
            │ 自主协商 (网状通信)
            ▼
┌─────────────────────────────────────────────────────────────┐
│                    专项Agent × 7                             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │矛盾分析 │ │ 实践论  │ │ 持久战  │ │农村包围 │           │
│  │  Agent  │ │  Agent  │  │  Agent  │ │ 城市Agent│           │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘           │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐                        │
│  │统一战线 │ │群众路线 │ │纸老虎论 │                        │
│  │  Agent  │ │  Agent  │ │  Agent  │                        │
│  └─────────┘ └─────────┘ └─────────┘                        │
└─────────────────────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────────────┐
│                    知识库层 (Knowledge Base)                  │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │  /knowledge                                              │ │
│  │   ├── 01-contradiction.md    (矛盾分析法)               │ │
│  │   ├── 02-practice.md          (实践认识循环)             │ │
│  │   ├── 03-protracted-war.md    (持久战略)                 │ │
│  │   ├── 04-rural-strategy.md    (农村包围城市)             │ │
│  │   ├── 05-united-front.md      (统一战线)                 │ │
│  │   ├── 06-mass-line.md         (群众路线)                 │ │
│  │   └── 07-paper-tiger.md        (纸老虎论)                 │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Agent通信拓扑

**星型 + 网状混合：**
- 主编Agent与各专项Agent之间：星型（主编作为中枢分发任务）
- 专项Agent之间：网状（自主协商，共享分析中间结论）
- 通信协议：LangGraph内置的图状态机机制

---

## 3. 核心组件

### 3.1 主编Agent (EditorAgent)

**职责：**
1. 接收用户任务，判断需要哪些专项Agent参与
2. 将任务分发给相关专项Agent
3. 协调专项Agent之间的协商
4. 收集各Agent的分析结果，进行综合撰写
5. 提供知识更新接口，协调知识库更新

**状态定义：**
```python
class EditorState(TypedDict):
    task: str                          # 用户任务描述
    relevant_agents: List[str]         # 相关的专项Agent列表
    agent_inputs: Dict[str, str]       # 分发给各Agent的输入
    agent_outputs: Dict[str, str]      # 各Agent的原始输出
    synthesis: str                      # 综合分析报告
    knowledge_updates: List[dict]      # 待确认的知识更新
```

### 3.2 专项Agent × 7

| Agent | 专精思想 | 核心能力 |
|-------|---------|---------|
| ContradictionAgent | 矛盾分析法 | 识别主要矛盾/次要矛盾，分析矛盾转化 |
| PracticeAgent | 实践认识循环 | "没有调查就没有发言权"分析框架 |
| ProtractedWarAgent | 持久战略 | 三阶段战略分析，力量对比评估 |
| RuralStrategyAgent | 农村包围城市 | 边缘突破、市场进入策略分析 |
| UnitedFrontAgent | 统一战线 | 利益格局、联盟策略分析 |
| MassLineAgent | 群众路线 | 从群众中来、到群众中去分析 |
| PaperTigerAgent | 纸老虎论 | 战略藐视+战术重视分析框架 |

**专项Agent状态定义：**
```python
class SpecialistState(TypedDict):
    task: str                          # 接收的任务
    analysis: str                       # 本Agent的分析结果
    shared_context: Dict[str, Any]     # 共享给其他Agent的中间结论
    requests_to_other_agents: List[dict]  # 向其他Agent请求的信息
```

### 3.3 知识库 (Knowledge Base)

**目录结构：**
```
/knowledge/
├── 01-contradiction.md       # 矛盾分析法完整知识库
├── 02-practice.md            # 实践认识循环完整知识库
├── 03-protracted-war.md       # 持久战略完整知识库
├── 04-rural-strategy.md       # 农村包围城市完整知识库
├── 05-united-front.md         # 统一战线完整知识库
├── 06-mass-line.md            # 群众路线完整知识库
├── 07-paper-tiger.md          # 纸老虎论完整知识库
├── index.md                   # 知识库索引
└── source/
    └── *.pdf                  # 原始PDF文献（《毛选》补充材料等）
```

**PDF转Markdown工具：**

集成 [Microsoft/markitdown](https://github.com/microsoft/markitdown)，实现PDF文献的自动转换和知识入库：

```bash
# 工具调用示例
markitdown input.pdf -o output.md
```

**PDF处理流程：**
```
用户上传PDF（如《毛选》第五卷新增章节）
     ↓
markitdown 转换为 Markdown
     ↓
主编Agent 解析内容，识别所属思想类别
     ↓
更新对应 Markdown 知识库文件
     ↓
通知相关专项Agent重新加载
```

**CLI命令扩展：**
```bash
mao-agent pdf-import <file.pdf> --category contradiction
mao-agent pdf-import <file.pdf> --auto-detect  # 自动识别类别
```

**知识文档结构（每个.md）：**
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
- 针对问题的标准化分析步骤
- prompt提示词模板

## 常见问答
- Q: ...
- A: ...
```

---

## 4. 用户交互层

### 4.1 CLI (Typer + Rich)

**命令结构：**
```bash
mao-agent <command> [options]

Commands:
  analyze   <question>    分析问题
  create    <topic>        创作内容
  research  <topic>        研究分析
  chat                      交互式对话
  update    <agent>        更新知识库
  config                    显示配置
```

**实时日志流输出：**
```
[Editor] 接收到任务：分析某公司市场竞争策略
[Editor] 调度Agent: contradiction, protracted_war, rural_strategy
[Contradiction] 分析主要矛盾...
[Contradiction] 主要矛盾识别完成: 市场份额 vs 用户心智
[ProtractedWar] 开始三阶段战略分析...
[RuralStrategy] 农村包围城市路径规划...
[Editor] 综合分析中...
[Editor] 输出结构化报告
```

**Verbose模式选项：**
- `--verbose` / `-v`: 显示完整协作过程
- `--quiet` / `-q`: 只显示最终结果

### 4.2 API (FastAPI)

**Endpoints：**
```python
POST /api/v1/analyze     # 结构化分析
POST /api/v1/create      # 内容创作
POST /api/v1/chat       # 对话咨询
POST /api/v1/update      # 知识更新

GET  /api/v1/health      # 健康检查
GET  /api/v1/agents      # 查看所有Agent状态
```

**请求/响应示例（POST /api/v1/analyze）：**
```json
// Request
{
  "task": "分析某创业公司面对行业巨头的竞争策略",
  "mode": "full"  // full: 报告+可视化+时间线, text_only: 仅报告
}

// Response (200 OK)
{
  "report": "...",
  "visualization": "base64 encoded image or url",
  "timeline": [...]
}
```

---

## 5. 输出格式

### 5.1 分析报告结构

```markdown
# 《{问题标题}》战略分析报告

## 一、矛盾分析
### 1.1 主要矛盾
### 1.2 矛盾的主要方面
### 1.3 矛盾转化趋势

## 二、力量对比评估
### 2.1 我方优势
### 2.2 敌方劣势
### 2.3 力量对比走势

## 三、战略路径
### 3.1 战略阶段划分（如适用）
### 3.2 农村包围城市路径（如适用）
### 3.3 统一战线策略

## 四、行动建议
### 4.1 近期行动（1-3个月）
### 4.2 中期行动（3-12个月）
### 4.3 长期行动（1年以上）

## 五、风险提示
### 5.1 主要风险
### 5.2 应对预案

## 六、可视化附录
[嵌入可视化图表]

## 七、战略时间线
[如持久战三阶段时间线]
```

### 5.2 内容创作输出

根据创作类型（演讲稿/文章/其他）生成对应格式的完整文档。

### 5.3 对话咨询输出

简洁、直接的问答形式，辅以辩证分析。

---

## 6. 知识进化机制

### 6.1 对话式更新流程

```
用户: "更新一下农村包围城市的案例，添加拼多多案例"
     ↓
EditorAgent 解析更新指令
     ↓
EditorAgent 更新对应 Markdown 文件
     ↓
通知相关专项Agent重新加载知识库
     ↓
确认更新完成
```

### 6.2 更新命令

```bash
mao-agent update rural-strategy --add-case "拼多多农村包围城市案例"
mao-agent update contradiction --add-question "如何识别主要矛盾？"
mao-agent update --interactive  # 交互式更新
```

---

## 7. 技术栈

| 组件 | 技术选型 | 版本 |
|------|---------|------|
| Multi-Agent框架 | LangGraph | latest |
| Agent实现 | LangChain Agents | latest |
| CLI框架 | Typer | latest |
| CLI美化 | Rich | latest |
| Web框架 | FastAPI | latest |
| Python版本 | Python 3.11+ | - |
| 知识向量化 | LangChain + FAISS | 可选 |
| PDF转换 | Microsoft markitdown | latest |

---

## 8. 项目结构

```
mao-thought-multi-agent/
├── README.md
├── pyproject.toml
├── requirements.txt
├── src/
│   └── mao_agent/
│       ├── __init__.py
│       ├── main.py              # CLI入口
│       ├── api.py               # API入口
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── editor.py        # 主编Agent
│       │   ├── contradiction.py
│       │   ├── practice.py
│       │   ├── protracted_war.py
│       │   ├── rural_strategy.py
│       │   ├── united_front.py
│       │   ├── mass_line.py
│       │   └── paper_tiger.py
│       ├── knowledge/
│       │   ├── __init__.py
│       │   ├── loader.py        # 知识库加载器
│       │   ├── updater.py       # 知识更新器
│       │   ├── pdf_importer.py  # PDF导入工具（集成markitdown）
│       │   ├── 01-contradiction.md
│       │   ├── 02-practice.md
│       │   ├── 03-protracted-war.md
│       │   ├── 04-rural-strategy.md
│       │   ├── 05-united-front.md
│       │   ├── 06-mass-line.md
│       │   └── 07-paper-tiger.md
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── search.py        # 知识检索工具
│       │   └── report.py        # 报告生成工具
│       └── output/
│           ├── __init__.py
│           └── formatter.py     # 输出格式化
├── tests/
│   ├── __init__.py
│   ├── test_agents.py
│   ├── test_knowledge.py
│   └── test_integration.py
└── docs/
    └── superpowers/
        └── specs/
            └── 2026-04-23-mao-thought-multi-agent-design.md
```

---

## 9. 验收标准

### 9.1 功能验收

- [ ] 主编Agent能正确调度相关专项Agent
- [ ] 专项Agent之间能进行网状通信
- [ ] CLI实时日志流正常输出
- [ ] API正常返回结构化报告
- [ ] 知识更新命令能正确更新Markdown
- [ ] 专项Agent能重新加载更新后的知识
- [ ] PDF导入功能正常工作（markitdown集成）

### 9.2 输出质量验收

- [ ] 分析报告包含矛盾分析、战略路径、行动建议
- [ ] 内容创作体现教员风格
- [ ] 对话咨询体现辩证思维

### 9.3 技术验收

- [ ] 多Agent协作流程无死锁
- [ ] 知识库并发读取安全
- [ ] CLI日志流不卡顿

---

## 10. 后续步骤

1. 创建项目基础结构（poetry/pyproject、目录）
2. 实现7个专项Agent的提示词模板
3. 实现主编Agent的调度逻辑
4. 实现知识库加载和更新机制
5. 实现CLI界面
6. 实现API接口
7. 集成测试
