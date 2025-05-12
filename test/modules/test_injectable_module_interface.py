from typing import Any

from mu_pipelines_interfaces.config_types.secrets.secret_value_mapping import (
    SecretValueMapping,
)
from mu_pipelines_interfaces.modules.injectable_module_interface import (
    InjectableModuleInterface,
)

# class GetSecretFunc(Protocol):
#     def __call__(self, secret_value_mapping: SecretValueMapping) -> Any: ...


def get_secret(secret_value_mapping: SecretValueMapping) -> Any:
    return f"{secret_value_mapping['secret_name']}"


def test_injectable_base_module() -> None:

    config: dict = {
        "test_1": {"secret_name": "test_secret_1"},
        "test_2": {
            "test_3": {"secret_name": "test_secret_3"},
            "test_4": [{"test_5": {"secret_name": "test_secret_5"}}],
        },
        "test_3": "not_a_secret",
    }

    InjectableModuleInterface(config).inject_secrets({"get_secret": get_secret})

    assert config["test_1"] == "test_secret_1"
    assert config["test_2"]["test_3"] == "test_secret_3"
    assert config["test_2"]["test_4"][0]["test_5"] == "test_secret_5"
