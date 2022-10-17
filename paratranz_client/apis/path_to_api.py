import typing_extensions

from paratranz_client.paths import PathValues
from paratranz_client.apis.paths.history import History
from paratranz_client.apis.paths.projects import Projects
from paratranz_client.apis.paths.projects_project_id import ProjectsProjectId
from paratranz_client.apis.paths.projects_project_id_files import ProjectsProjectIdFiles
from paratranz_client.apis.paths.projects_project_id_files_file_id import ProjectsProjectIdFilesFileId
from paratranz_client.apis.paths.projects_project_id_files_revisions import ProjectsProjectIdFilesRevisions
from paratranz_client.apis.paths.projects_project_id_strings import ProjectsProjectIdStrings
from paratranz_client.apis.paths.projects_project_id_strings_string_id import ProjectsProjectIdStringsStringId
from paratranz_client.apis.paths.projects_project_id_terms import ProjectsProjectIdTerms
from paratranz_client.apis.paths.projects_project_id_terms_term_id import ProjectsProjectIdTermsTermId
from paratranz_client.apis.paths.projects_project_id_terms_term_id_history import ProjectsProjectIdTermsTermIdHistory
from paratranz_client.apis.paths.projects_project_id_artifacts import ProjectsProjectIdArtifacts
from paratranz_client.apis.paths.projects_project_id_artifacts_download import ProjectsProjectIdArtifactsDownload
from paratranz_client.apis.paths.projects_project_id_issues import ProjectsProjectIdIssues
from paratranz_client.apis.paths.projects_project_id_issues_issue_id import ProjectsProjectIdIssuesIssueId
from paratranz_client.apis.paths.projects_project_id_scores import ProjectsProjectIdScores
from paratranz_client.apis.paths.mails import Mails
from paratranz_client.apis.paths.mails_conversations_user_id import MailsConversationsUserId
from paratranz_client.apis.paths.users_user_id import UsersUserId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.HISTORY: History,
        PathValues.PROJECTS: Projects,
        PathValues.PROJECTS_PROJECT_ID: ProjectsProjectId,
        PathValues.PROJECTS_PROJECT_ID_FILES: ProjectsProjectIdFiles,
        PathValues.PROJECTS_PROJECT_ID_FILES_FILE_ID: ProjectsProjectIdFilesFileId,
        PathValues.PROJECTS_PROJECT_ID_FILES_REVISIONS: ProjectsProjectIdFilesRevisions,
        PathValues.PROJECTS_PROJECT_ID_STRINGS: ProjectsProjectIdStrings,
        PathValues.PROJECTS_PROJECT_ID_STRINGS_STRING_ID: ProjectsProjectIdStringsStringId,
        PathValues.PROJECTS_PROJECT_ID_TERMS: ProjectsProjectIdTerms,
        PathValues.PROJECTS_PROJECT_ID_TERMS_TERM_ID: ProjectsProjectIdTermsTermId,
        PathValues.PROJECTS_PROJECT_ID_TERMS_TERM_ID_HISTORY: ProjectsProjectIdTermsTermIdHistory,
        PathValues.PROJECTS_PROJECT_ID_ARTIFACTS: ProjectsProjectIdArtifacts,
        PathValues.PROJECTS_PROJECT_ID_ARTIFACTS_DOWNLOAD: ProjectsProjectIdArtifactsDownload,
        PathValues.PROJECTS_PROJECT_ID_ISSUES: ProjectsProjectIdIssues,
        PathValues.PROJECTS_PROJECT_ID_ISSUES_ISSUE_ID: ProjectsProjectIdIssuesIssueId,
        PathValues.PROJECTS_PROJECT_ID_SCORES: ProjectsProjectIdScores,
        PathValues.MAILS: Mails,
        PathValues.MAILS_CONVERSATIONS_USER_ID: MailsConversationsUserId,
        PathValues.USERS_USER_ID: UsersUserId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.HISTORY: History,
        PathValues.PROJECTS: Projects,
        PathValues.PROJECTS_PROJECT_ID: ProjectsProjectId,
        PathValues.PROJECTS_PROJECT_ID_FILES: ProjectsProjectIdFiles,
        PathValues.PROJECTS_PROJECT_ID_FILES_FILE_ID: ProjectsProjectIdFilesFileId,
        PathValues.PROJECTS_PROJECT_ID_FILES_REVISIONS: ProjectsProjectIdFilesRevisions,
        PathValues.PROJECTS_PROJECT_ID_STRINGS: ProjectsProjectIdStrings,
        PathValues.PROJECTS_PROJECT_ID_STRINGS_STRING_ID: ProjectsProjectIdStringsStringId,
        PathValues.PROJECTS_PROJECT_ID_TERMS: ProjectsProjectIdTerms,
        PathValues.PROJECTS_PROJECT_ID_TERMS_TERM_ID: ProjectsProjectIdTermsTermId,
        PathValues.PROJECTS_PROJECT_ID_TERMS_TERM_ID_HISTORY: ProjectsProjectIdTermsTermIdHistory,
        PathValues.PROJECTS_PROJECT_ID_ARTIFACTS: ProjectsProjectIdArtifacts,
        PathValues.PROJECTS_PROJECT_ID_ARTIFACTS_DOWNLOAD: ProjectsProjectIdArtifactsDownload,
        PathValues.PROJECTS_PROJECT_ID_ISSUES: ProjectsProjectIdIssues,
        PathValues.PROJECTS_PROJECT_ID_ISSUES_ISSUE_ID: ProjectsProjectIdIssuesIssueId,
        PathValues.PROJECTS_PROJECT_ID_SCORES: ProjectsProjectIdScores,
        PathValues.MAILS: Mails,
        PathValues.MAILS_CONVERSATIONS_USER_ID: MailsConversationsUserId,
        PathValues.USERS_USER_ID: UsersUserId,
    }
)
