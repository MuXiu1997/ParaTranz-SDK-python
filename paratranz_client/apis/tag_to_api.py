import typing_extensions

from paratranz_client.apis.tags import TagValues
from paratranz_client.apis.tags.project_api import ProjectApi
from paratranz_client.apis.tags.string_api import StringApi
from paratranz_client.apis.tags.file_api import FileApi
from paratranz_client.apis.tags.history_api import HistoryApi
from paratranz_client.apis.tags.term_api import TermApi
from paratranz_client.apis.tags.artifact_api import ArtifactApi
from paratranz_client.apis.tags.user_api import UserApi
from paratranz_client.apis.tags.issue_api import IssueApi
from paratranz_client.apis.tags.mail_api import MailApi
from paratranz_client.apis.tags.score_api import ScoreApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PROJECT: ProjectApi,
        TagValues.STRING: StringApi,
        TagValues.FILE: FileApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.TERM: TermApi,
        TagValues.ARTIFACT: ArtifactApi,
        TagValues.USER: UserApi,
        TagValues.ISSUE: IssueApi,
        TagValues.MAIL: MailApi,
        TagValues.SCORE: ScoreApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PROJECT: ProjectApi,
        TagValues.STRING: StringApi,
        TagValues.FILE: FileApi,
        TagValues.HISTORY: HistoryApi,
        TagValues.TERM: TermApi,
        TagValues.ARTIFACT: ArtifactApi,
        TagValues.USER: UserApi,
        TagValues.ISSUE: IssueApi,
        TagValues.MAIL: MailApi,
        TagValues.SCORE: ScoreApi,
    }
)
