from langgraph.runtime import Runtime

from app.agent.context import DataAgentContext
from app.agent.state import DataAgentState


async def recall_value(state: DataAgentState, runtime: Runtime[DataAgentContext]):
    """召回和用户问题相关的字段取值"""

    writer = runtime.stream_writer
    # 通过流式事件标记当前已经进入字段取值检索分支
    writer("召回字段取值")
    import asyncio

    # 当前章节先保留占位逻辑，后续接入 Elasticsearch 检索
    await asyncio.sleep(0.5)