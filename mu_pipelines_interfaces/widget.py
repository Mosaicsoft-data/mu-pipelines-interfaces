from abc import ABC, abstractmethod


class WidgetInterface(ABC):
    @abstractmethod
    def do(self) -> None:
        pass
