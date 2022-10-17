from enum import Enum


class GetFileRevisionsType(str, Enum):
    CREATE = "create"
    UPDATE = "update"
    IMPORT = "import"

    def __str__(self) -> str:
        return str(self.value)
