from langgraph.runtime import Runtime

from app.agent.context import DataAgentContext
from app.agent.state import DataAgentState


async def add_extra_context(state: DataAgentState, runtime: Runtime[DataAgentContext]):
    """补齐生成 SQL 所需的上下文信息"""

    writer = runtime.stream_writer
    # 这里是过滤结果汇合点，后续会把结构化上下文写回 state
    writer("添加额外上下文")
    import asyncio

    # 当前章节先保留占位逻辑，后续会组装表字段 指标和取值上下文
    await asyncio.sleep(0.5)