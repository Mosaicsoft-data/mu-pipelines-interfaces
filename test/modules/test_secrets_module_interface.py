from typing import Any, TypedDict, cast

from mu_pipelines_interfaces.config_types.secrets.secrets_config import (
    SecretsConfigItem,
)
from mu_pipelines_interfaces.configuration_provider import ConfigurationProvider
from mu_pipelines_interfaces.modules.secrets_module_interface import (
    SecretsContext,
    SecretsModuleInterface,
)


class AdditionalAttributes(TypedDict):
    hardcoded_value: Any


class MockSecretsModule(SecretsModuleInterface):
    _hardcoded_value: Any

    def __init__(
        self, config: SecretsConfigItem, configuration_provider: ConfigurationProvider
    ):
        super().__init__(config, configuration_provider)
        assert "additional_attributes" in config
        additional_attributes = cast(
            AdditionalAttributes, config["additional_attributes"]
        )

        assert "hardcoded_value" in additional_attributes

        if additional_attributes["hardcoded_value"] is not None:
            self._hardcoded_value = additional_attributes["hardcoded_value"]

    def get_uncached_secret(self, context: SecretsContext) -> Any | None:
        return self._hardcoded_value


def test_SecretsModuleInterface_happy_path() -> None:
    config: SecretsConfigItem = {
        "name": "test_secret_name",
        "provider": "hardcoded",
        "additional_attributes": {"hardcoded_value": "test_hardcoded_value"},
    }
    context: SecretsContext = cast(SecretsContext, {})

    # assumption: configuration_provider is not used by SecretsModuleInterface
    secrets_module: SecretsModuleInterface = MockSecretsModule(
        config, ConfigurationProvider()
    )

    secrets: Any | None = secrets_module.get(context)

    assert secrets == "test_hardcoded_value"

    assert "secrets" in context
    assert config["name"] in context["secrets"]
    assert context["secrets"][config["name"]] == "test_hardcoded_value"


def test_SecretsModuleInterface_uses_cached_value() -> None:
    config: SecretsConfigItem = {
        "name": "test_secret_name",
        "provider": "hardcoded",
        "additional_attributes": {"hardcoded_value": "test_hardcoded_value"},
    }
    context: SecretsContext = cast(
        SecretsContext, {"secrets": {"test_secret_name": "test_cached_value"}}
    )

    # assumption: configuration_provider is not used by SecretsModuleInterface
    secrets_module: SecretsModuleInterface = MockSecretsModule(
        config, ConfigurationProvider()
    )

    secrets: Any | None = secrets_module.get(context)

    assert secrets == "test_cached_value"

    assert "secrets" in context
    assert config["name"] in context["secrets"]
    assert context["secrets"][config["name"]] == "test_cached_value"
