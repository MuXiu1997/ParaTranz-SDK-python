# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from paratranz_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PROJECT = "project"
    STRING = "string"
    FILE = "file"
    HISTORY = "history"
    TERM = "term"
    ARTIFACT = "artifact"
    USER = "user"
    ISSUE = "issue"
    MAIL = "mail"
    SCORE = "score"
