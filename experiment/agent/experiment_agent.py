from abc import ABC, abstractmethod

from aios.hooks.syscall import send_request
from pyopenagi.utils.chat_template import LLMQuery, MemoryQuery, StorageQuery


class ExperimentAgent(ABC):

    @abstractmethod
    def run(self, input_str: str):
        pass


class SimpleLLMAgent(ExperimentAgent):

    def __init__(self, on_aios: bool = True):
        self.agent_name = "gpt"
        self.on_aios = on_aios

    def run(self, input_str: str):
        message = {"content": input_str, "role": "user"}
        query = LLMQuery(messages=[message], tools=None)

        response, _, _, _, _ = send_request(
            agent_name=self.agent_name,
            query=query
        )
        result = response.response_message
        return result
