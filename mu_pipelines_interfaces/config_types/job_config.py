from typing import TypedDict

from dev_kit_interfaces.config_types.destination_config import DestinationConfig
from dev_kit_interfaces.config_types.execute_config import ExecuteConfig


class JobConfigItem(TypedDict):
    execution: list[ExecuteConfig]
    destination: list[DestinationConfig]
