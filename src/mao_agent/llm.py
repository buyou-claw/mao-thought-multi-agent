# src/mao_agent/llm.py
import os
from langchain_openai import ChatOpenAI

# MiniMax API 配置
MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY", "sk-cp-vDgywsQ2ltIxM6ch249DV7ti28m3OOXSbHxu42TXznLtyo2Zzz0gW78I1Na3saP5coy5MhuuHg554IP4hZ6TGuGin1QsWdNsMZftbW6OhXwrX_QCk0t9eJo")
MINIMAX_BASE_URL = "https://api.minimax.chat/v1"

# 创建 LLM 实例
def get_llm(model: str = "MiniMax-M2.7-highspeed"):
    return ChatOpenAI(
        api_key=MINIMAX_API_KEY,
        base_url=MINIMAX_BASE_URL,
        model=model,
        temperature=0.7
    )
