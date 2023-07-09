from typing import Optional
from langchain.callbacks.base import BaseCallbackHandler
from typing import Optional, Any
from uuid import UUID

from langchain.schema import (
    AgentAction,
    AgentFinish
)


class StreamlitCallbackHandler(BaseCallbackHandler):

    def __init__(self, st) -> None:
        super().__init__()
        self.st = st

    def on_agent_action(
        self,
        action: AgentAction,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        """Run on agent action."""
        self.st.write(f"Tool: {action.tool}")
        self.st.write(f"Input: {action.tool_input['query']}")

    def on_agent_finish(
        self,
        finish: AgentFinish,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        """Run on agent end."""
        pass