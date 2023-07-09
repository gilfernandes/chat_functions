from typing import Optional
from langchain.callbacks.base import BaseCallbackHandler
from typing import Optional, Any
from uuid import UUID

from langchain.schema import (
    AgentAction,
    AgentFinish
)

import logging

def setup_log(module_name: str):
    logging.basicConfig(
        level='INFO', 
        format='%(asctime)s %(message)s', 
        datefmt='%m/%d/%Y %I:%M:%S %p',
        handlers=[
            logging.FileHandler("agent.log"),
            # logging.StreamHandler()
        ]
    )
    return logging.getLogger(module_name)

logger = setup_log("agent-logger")

class AgentCallbackHandler(BaseCallbackHandler):

    def on_agent_action(
        self,
        action: AgentAction,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        """Run on agent action."""
        logger.info(f"on_agent_action tool: {action.tool}")
        logger.info(f"on_agent_action tool input: {action.tool_input}")
        logger.info(f"on_agent_action tool log: {action.log}")

    def on_agent_finish(
        self,
        finish: AgentFinish,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        """Run on agent end."""
        logger.info(f"on_agent_finish re: {finish.return_values}")
        logger.info(f"on_agent_finish too logl: {finish.log}")