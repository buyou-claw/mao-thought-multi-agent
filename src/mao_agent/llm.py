# src/mao_agent/llm.py
import os
from langchain_openai import ChatOpenAI

# MiniMax API 配置
MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY")  # 必须设置环境变量 MINIMAX_API_KEY
if not MINIMAX_API_KEY:
    raise ValueError("环境变量 MINIMAX_API_KEY 未设置，请先设置再运行")
MINIMAX_BASE_URL = "https://api.minimax.chat/v1"

# 创建 LLM 实例
def get_llm(model: str = "MiniMax-M2.7-highspeed"):
    return ChatOpenAI(
        api_key=MINIMAX_API_KEY,
        base_url=MINIMAX_BASE_URL,
        model=model,
        temperature=0.7
    )
