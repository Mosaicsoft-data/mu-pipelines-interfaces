from abc import ABC
from typing import Any

from mu_pipelines_interfaces.config_types.destination_config import DestinationConfig
from mu_pipelines_interfaces.configuration_provider import ConfigurationProvider


class DestinationModuleInterface(ABC):
    _config: DestinationConfig
    _configuration_provider: ConfigurationProvider

    def __init__(
        self, config: DestinationConfig, configuration_provider: ConfigurationProvider
    ):
        self._config = config
        self._configuration_provider = configuration_provider

    def save(self, df: Any, context: Any) -> None:

        raise NotImplementedError()
