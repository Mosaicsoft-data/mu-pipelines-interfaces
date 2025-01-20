from typing import TypedDict


class ConnectionDetails(TypedDict):
    host: str
    database: str
    port: str
    username: str
    password: str
    certificate_path: str


class ConnectionConfig(TypedDict):
    name: str
    type: str
    connection_details: ConnectionDetails


class ConnectionProperties(TypedDict):
    connections: list[ConnectionConfig]
