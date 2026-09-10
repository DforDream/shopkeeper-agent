from langgraph.runtime import Runtime

from app.agent.context import DataAgentContext
from app.agent.state import DataAgentState


async def generate_sql(state: DataAgentState, runtime: Runtime[DataAgentContext]):
    """基于已检索和过滤的上下文生成 SQL"""

    writer = runtime.stream_writer
    # 后续真实实现会调用 llm，把 SQL 写回 DataAgentState
    writer("生成SQL")
    import asyncio

    # 当前章节先保留占位逻辑，后续替换为 LLM 生成 SQL
    await asyncio.sleep(0.5)