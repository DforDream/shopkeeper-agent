from langgraph.runtime import Runtime

from app.agent.context import DataAgentContext
from app.agent.state import DataAgentState


async def recall_column(state: DataAgentState, runtime: Runtime[DataAgentContext]):
    """召回和用户问题语义相关的字段元数据"""

    writer = runtime.stream_writer
    # 先输出节点进度，便于观察 LangGraph 并行分支的执行情况
    writer("召回字段信息")
    import asyncio

    # 当前章节先保留占位逻辑，后续接入 ColumnQdrantRepository 查询
    await asyncio.sleep(0.5)