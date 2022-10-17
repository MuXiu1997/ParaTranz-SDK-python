from enum import Enum


class GetScoresOperation(str, Enum):
    TRANSLATE = "translate"
    EDIT = "edit"
    REVIEW = "review"

    def __str__(self) -> str:
        return str(self.value)
