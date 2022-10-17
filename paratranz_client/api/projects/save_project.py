from typing import Any, Dict

import httpx

from ...client import Client
from ...models.project import Project
from ...types import Response


def _get_kwargs(
    project_id: int,
    *,
    client: Client,
    json_body: Project,
) -> Dict[str, Any]:
    url = "{}/projects/{projectId}".format(client.base_url, projectId=project_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    project_id: int,
    *,
    client: Client,
    json_body: Project,
) -> Response[Any]:
    """更新项目

     通过ID更新项目信息

    Args:
        project_id (int):
        json_body (Project): 项目

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    project_id: int,
    *,
    client: Client,
    json_body: Project,
) -> Response[Any]:
    """更新项目

     通过ID更新项目信息

    Args:
        project_id (int):
        json_body (Project): 项目

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
