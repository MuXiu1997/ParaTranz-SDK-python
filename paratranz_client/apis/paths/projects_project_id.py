from paratranz_client.paths.projects_project_id.get import ApiForget
from paratranz_client.paths.projects_project_id.put import ApiForput
from paratranz_client.paths.projects_project_id.delete import ApiFordelete


class ProjectsProjectId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
