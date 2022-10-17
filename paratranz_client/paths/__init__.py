# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from paratranz_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    HISTORY = "/history"
    PROJECTS = "/projects"
    PROJECTS_PROJECT_ID = "/projects/{projectId}"
    PROJECTS_PROJECT_ID_FILES = "/projects/{projectId}/files"
    PROJECTS_PROJECT_ID_FILES_FILE_ID = "/projects/{projectId}/files/{fileId}"
    PROJECTS_PROJECT_ID_FILES_REVISIONS = "/projects/{projectId}/files/revisions"
    PROJECTS_PROJECT_ID_STRINGS = "/projects/{projectId}/strings"
    PROJECTS_PROJECT_ID_STRINGS_STRING_ID = "/projects/{projectId}/strings/{stringId}"
    PROJECTS_PROJECT_ID_TERMS = "/projects/{projectId}/terms"
    PROJECTS_PROJECT_ID_TERMS_TERM_ID = "/projects/{projectId}/terms/{termId}"
    PROJECTS_PROJECT_ID_TERMS_TERM_ID_HISTORY = "/projects/{projectId}/terms/{termId}/history"
    PROJECTS_PROJECT_ID_ARTIFACTS = "/projects/{projectId}/artifacts"
    PROJECTS_PROJECT_ID_ARTIFACTS_DOWNLOAD = "/projects/{projectId}/artifacts/download"
    PROJECTS_PROJECT_ID_ISSUES = "/projects/{projectId}/issues"
    PROJECTS_PROJECT_ID_ISSUES_ISSUE_ID = "/projects/{projectId}/issues/{issueId}"
    PROJECTS_PROJECT_ID_SCORES = "/projects/{projectId}/scores"
    MAILS = "/mails"
    MAILS_CONVERSATIONS_USER_ID = "/mails/conversations/{userId}"
    USERS_USER_ID = "/users/{userId}"
