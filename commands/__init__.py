from abc import ABC, abstractmethod
from discord import Message


class Command(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    async def execute(self, message: Message):
        pass
