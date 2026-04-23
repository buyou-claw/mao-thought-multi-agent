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