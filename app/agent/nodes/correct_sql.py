from langgraph.runtime import Runtime

from app.agent.context import DataAgentContext
from app.agent.state import DataAgentState


async def correct_sql(state: DataAgentState, runtime: Runtime[DataAgentContext]):
    """根据校验错误修正 SQL"""

    writer = runtime.stream_writer
    # 后续真实实现会读取 state["error"] 和原 SQL，再调用 LLM 生成修正版 SQL
    writer("校正SQL")
    import asyncio

    # 当前章节先保留占位逻辑，后续接入 SQL 修正提示词
    await asyncio.sleep(0.5)