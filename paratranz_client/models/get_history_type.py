from enum import Enum


class GetHistoryType(str, Enum):
    TEXT = "text"
    IMPORT = "import"
    COMMENT = "comment"

    def __str__(self) -> str:
        return str(self.value)
