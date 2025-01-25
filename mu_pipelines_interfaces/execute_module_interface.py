from abc import ABC
from typing import Any

from mu_pipelines_interfaces.config_types.execute_config import ExecuteConfig
from mu_pipelines_interfaces.configuration_provider import ConfigurationProvider


class ExecuteModuleInterface(ABC):
    _config: ExecuteConfig
    _configuration_provider: ConfigurationProvider

    def __init__(
        self, config: ExecuteConfig, configuration_provider: ConfigurationProvider
    ):
        self._config = config
        self._configuration_provider = configuration_provider

    def execute(self, context: Any) -> Any | None:

        raise NotImplementedError()
